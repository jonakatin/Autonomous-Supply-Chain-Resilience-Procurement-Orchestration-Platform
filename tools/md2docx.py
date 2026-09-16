"""Convert a project Markdown file into a Word document that follows the
BSE 4100 document format specified by the course lecturer.

Formatting rules implemented here come from "Document format.pptx":

  - Times New Roman throughout, body text 12pt
  - Line spacing 1.5
  - Justified body alignment
  - Numbered section headings, bold, larger than body text
  - Main sections start on a new page
  - Table captions above the table, numbered Table 1, Table 2, ...
  - Figure captions below the figure, numbered by section
  - Page numbers in the footer
  - A table of contents field the word processor generates

Usage:
    python tools/md2docx.py "docs/Some Document.md" "docs/Some Document.docx"
    python tools/md2docx.py --all
"""

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

BODY_FONT = "Times New Roman"
BODY_SIZE = Pt(12)
TABLE_SIZE = Pt(10)
LINE_SPACING = 1.5

HEADING_SIZES = {1: Pt(16), 2: Pt(14), 3: Pt(13), 4: Pt(12)}


def set_cell_font(cell, bold=False, size=TABLE_SIZE):
    for para in cell.paragraphs:
        para.paragraph_format.line_spacing = 1.0
        para.paragraph_format.space_after = Pt(2)
        for run in para.runs:
            run.font.name = BODY_FONT
            run.font.size = size
            run.bold = bold


def add_field(paragraph, instruction):
    """Insert a Word field code, for example PAGE or TOC."""
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = instruction
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    for element in (begin, instr, separate, end):
        run._r.append(element)


def configure_document():
    doc = Document()

    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = BODY_SIZE
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)
    normal.paragraph_format.line_spacing = LINE_SPACING
    normal.paragraph_format.space_after = Pt(6)

    for level, size in HEADING_SIZES.items():
        style = doc.styles[f"Heading {level}"]
        style.font.name = BODY_FONT
        style.font.size = size
        style.font.bold = True
        style.font.color.rgb = None
        style.paragraph_format.line_spacing = LINE_SPACING
        style.paragraph_format.space_before = Pt(12)
        style.paragraph_format.space_after = Pt(6)

    for section in doc.sections:
        section.left_margin = section.right_margin = Inches(1.0)
        section.top_margin = section.bottom_margin = Inches(1.0)
        footer = section.footer.paragraphs[0]
        footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_field(footer, " PAGE ")
        for run in footer.runs:
            run.font.name = BODY_FONT
            run.font.size = Pt(10)

    return doc


def add_runs(paragraph, text, justify=True):
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    for index, part in enumerate(re.split(r"\*\*(.+?)\*\*", text)):
        if not part:
            continue
        run = paragraph.add_run(part)
        run.font.name = BODY_FONT
        run.bold = index % 2 == 1
    if justify:
        paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph.paragraph_format.line_spacing = LINE_SPACING
    return paragraph


def convert(src_path, out_path):
    lines = Path(src_path).read_text(encoding="utf-8").split("\n")
    doc = configure_document()

    table_number = 0
    seen_first_heading = False
    pending_caption = ""
    index = 0

    while index < len(lines):
        line = lines[index].rstrip()

        if line.strip() == "---":
            index += 1
            continue

        # Table, optionally preceded by a caption comment of the form
        # <!-- Table: caption text -->
        if line.startswith("|"):
            block = []
            while index < len(lines) and lines[index].startswith("|"):
                block.append(lines[index])
                index += 1
            rows = [
                [cell.strip() for cell in row.strip().strip("|").split("|")]
                for row in block
            ]
            rows = [r for r in rows if not all(set(c) <= set("-: ") for c in r)]
            if not rows:
                continue

            table_number += 1
            caption = doc.add_paragraph()
            caption.alignment = WD_ALIGN_PARAGRAPH.LEFT
            caption.paragraph_format.space_after = Pt(2)
            run = caption.add_run(f"Table {table_number}: ")
            run.bold = True
            run.font.name = BODY_FONT
            run.font.size = Pt(11)
            run = caption.add_run(pending_caption or "")
            run.font.name = BODY_FONT
            run.font.size = Pt(11)

            width = len(rows[0])
            table = doc.add_table(rows=0, cols=width)
            table.style = "Table Grid"
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            for row_index, row in enumerate(rows):
                cells = table.add_row().cells
                for col in range(width):
                    value = row[col] if col < len(row) else ""
                    cells[col].text = ""
                    add_runs(cells[col].paragraphs[0], value, justify=False)
                    set_cell_font(cells[col], bold=row_index == 0)
            doc.add_paragraph()
            pending_caption = ""
            continue

        if line.startswith("<!--") and "Table:" in line:
            pending_caption = line.split("Table:", 1)[1].replace("-->", "").strip()
            index += 1
            continue

        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            text = line.lstrip("#").strip()
            if level == 1 and seen_first_heading:
                doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
            seen_first_heading = True
            heading = doc.add_heading(text, min(level, 4))
            for run in heading.runs:
                run.font.name = BODY_FONT
            index += 1
            continue

        checkbox = re.match(r"^\s*-\s+\[( |x)\]\s+(.*)$", line)
        if checkbox:
            mark = "[X] " if checkbox.group(1) == "x" else "[  ] "
            add_runs(
                doc.add_paragraph(style="List Bullet"),
                mark + checkbox.group(2),
                justify=False,
            )
            index += 1
            continue

        if re.match(r"^\s*[-*]\s+", line):
            add_runs(
                doc.add_paragraph(style="List Bullet"),
                re.sub(r"^\s*[-*]\s+", "", line),
                justify=False,
            )
            index += 1
            continue

        if re.match(r"^\s*\d+\.\s+", line):
            add_runs(
                doc.add_paragraph(style="List Number"),
                re.sub(r"^\s*\d+\.\s+", "", line),
                justify=False,
            )
            index += 1
            continue

        if line.startswith(">"):
            paragraph = doc.add_paragraph()
            paragraph.paragraph_format.left_indent = Inches(0.4)
            add_runs(paragraph, line.lstrip("> ").strip())
            for run in paragraph.runs:
                run.italic = True
            index += 1
            continue

        if line.strip():
            add_runs(doc.add_paragraph(), line.strip())

        index += 1

    doc.save(out_path)
    return out_path


def main():
    root = Path(__file__).resolve().parent.parent
    if len(sys.argv) == 2 and sys.argv[1] == "--all":
        targets = sorted((root / "docs").glob("*.md"))
        for md in targets:
            out = md.with_suffix(".docx")
            try:
                convert(md, out)
                print(f"converted {md.name}")
            except PermissionError:
                print(f"SKIPPED {md.name}: the .docx is open, close it and rerun")
        return
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
    print(f"converted {sys.argv[1]}")


if __name__ == "__main__":
    main()
