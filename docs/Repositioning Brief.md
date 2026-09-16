# Repositioning Brief: From Inventory System to Decision Agent

**Project:** LogicSynapse AI
**Course:** BSE 4100, Year 4 Semester 1
**Prepared:** 16 September 2026
**For:** Jonathan Katongole, Dev Johnson, Bridget Bataringaya, Isaac Mwesigwa

---

## 1. Why this brief exists

The concept paper as written describes the project as an inventory control system. The course coordinator's BSE 4100 Overview deck, slide 12, titled "PROJECTS YOU MUST NOT DO", lists "Inventory management" explicitly. Slide 11 adds that a project must not consist of "only basic data entry and retrieval", and that information systems must show data analytics.

This is a disqualification risk, not a branding concern. Slide 4 states that a student who fails BSE 4100 must not proceed to BSE 4200.

The project itself is sound and is not an inventory management system. It has simply been described in inventory vocabulary. This brief fixes the description. **No part of the project is being changed or dropped.**

---

## 2. The single change that fixes everything

The project was named after its **data source** instead of its **decision**.

Inventory is the input. The output is a capital commitment decision. Those are two different projects, and only one of them appears on the banned list.

| Currently described as | Should be described as |
|---|---|
| Tracking stock levels across distribution centres | Deciding how much capital to commit, and when |
| Preventing stockouts | Preventing irreversible over-commitment and missed seasonal windows |
| Inventory optimisation platform | Procurement decision agent with human authorisation |
| Generic SKUs across regional hubs | Textbook print runs against school term deadlines |

---

## 3. Promote the vertical from example to identity

In the meeting of 16 September 2026 the team chose book publishing and paper supply as a "running example." It should stop being an example and become the identity of the project.

Textbook publishing is not a generic inventory problem. It is a **discrete, irreversible, high-value commitment made months ahead of demand, against a hard seasonal deadline, using imported inputs on long lead times.**

Why that matters, stated plainly:

- A publisher decides in one moment how many copies to print. There is no incremental reorder. It is one large, binding commitment.
- The deadline is fixed by the school term. Missing it does not delay the sale, it destroys the sale, because a textbook that arrives after the term started has lost that term's cohort entirely.
- Paper is imported, so lead times are long and variable, and costs are exposed to currency movement before any revenue arrives.
- Demand is **non-stationary**. A curriculum revision can reduce demand for a title to zero overnight.

That last property is a genuine statistical difficulty, and the brief's recommendation is to make it explicit rather than hide it. A project that identifies a hard property of its domain and designs around it is stronger than one that assumes well-behaved data.

---

## 4. Title

The current title, "Autonomous Supply Chain Resilience and Procurement Orchestration Platform", is nine words that describe an architecture, name no beneficiary, and state no outcome. The word "platform" is the strongest single signal of over-engineering in the whole package.

Recommended academic title:

> **Print Run Intelligence: An Explainable Agentic AI System for Autonomous Procurement Decisions in Ugandan Publishing**

Product name stays **LogicSynapse AI**.

Naming principle, drawn from how project catalogues index work: name the outcome achieved and the technique used, never the architecture.

---

## 5. The one-line pitch

Replace the current executive summary opening with this:

> Ugandan publishers commit to a print run months before they know demand. Print too many and the cash is pulped. Print too few and you lose an entire school term, because there is no second chance at a term. LogicSynapse is an AI agent that makes that call, shows its reasoning line by line, and waits for a human to approve before a single shilling is spent.

Fifteen seconds, names the beneficiary, names the money, names the consequence, and contains no banned vocabulary.

---

## 6. Add a section: "Why this is not an inventory management system"

Pre-empting the objection is stronger than hoping it is not raised. Include this table in the concept paper and on a presentation slide.

| Inventory management system | LogicSynapse AI |
|---|---|
| Records what is currently held | Decides what to commit to in future |
| Human reads a dashboard and decides | Agent decides and reasons, human authorises |
| Reactive alert at a fixed threshold | Forecast-driven, lead-time aware, seasonally adjusted |
| Output is a report | Output is a purchase order, a supplier email, and a full reasoning trace |
| Satisfies no analytics requirement | Forecasting, optimisation, and multi-step agent reasoning |
| Data entry and retrieval | Autonomous action under human authority |

---

## 7. Draw the algorithmic line clearly

Slide 9 requires that a project "tests acquired knowledge such as algorithms." A supervisor will reasonably ask what the team engineered versus what the language model provided. Answer it before it is asked.

**The team's engineering work:**
- Depletion forecasting from sales velocity
- Dynamic reorder point incorporating lead time variance
- Safety stock computation under seasonal demand
- Economic order quantity adapted to discrete, indivisible print runs
- Curriculum-change risk as an explicit input to the decision

**The language model's role:**
- Orchestrating multi-step tool calls
- Selecting among suppliers given the computed constraints
- Drafting the natural-language purchase order and supplier email

The decision mathematics is classical, implementable, and examinable. The language model wraps it. Stating this division explicitly converts a perceived weakness into a demonstrated strength.

---

## 8. Replace the four-layer architecture

The four-layer table reads as enterprise architecture theatre. Replace it everywhere a non-technical reader will look with five verbs:

**Sense → Forecast → Decide → Explain → Approve**

Same system, no jargon, and the human is visibly the final step rather than buried inside "Layer 4". Keep the layered table in the technical appendix if it is useful there.

---

## 9. Promote the Activity Log from feature to thesis

The Live Agent Activity Log is currently positioned as a "key differentiator." It should be positioned as the research question of the project.

The interesting question is not whether stock can be forecast. That is solved and unremarkable. The question is:

> **What must an autonomous agent show a human before that human will delegate spending authority to it?**

This is a live and unsolved question in human-AI collaboration, and it gives the project an evaluation metric that is genuinely original.

**Proposed evaluation metrics:**

| Metric | What it measures |
|---|---|
| Override rate over time | Whether the manager's trust in the agent grows as it explains itself |
| Decision latency | Time from signal existing in data to action taken, agent versus manual baseline |
| Forecast accuracy versus naive baseline | Whether the modelling earns its complexity |
| Working capital released | Days of capital freed from stock that should not have been committed |

The override rate is the most valuable of these, because it measures the actual research question rather than a routine engineering one.

---

## 10. What to cut, and what to move

**Cut from anything a human reads:**
- The words "orchestration platform"
- "Model Context Protocol" in prose (keep it in the technology stack table)
- "Four-layer architecture" as framing
- The claim of an 80 percent reduction in procurement overhead. This was read from a Gemini autogenerated summary during the team meeting and has no source. Delete it, or restate it as a target to be measured.

**Move to an appendix labelled "Phase 2, BSE 4200":**
- The eight-week development roadmap and its milestones

Rationale: slide 2 states the BSE 4100 objectives are to find a problem, propose a solution, and document requirements. Slide 14 lists the deliverables as the concept paper, the data collection tool, the SRS, and the report. The build belongs to BSE 4200. A development roadmap in the front matter consumes space that should describe the problem and the beneficiaries, and it reinforces the impression of over-engineering.

**Add:**
- Environmental impact. Overprinting means pulped books, wasted imported paper, and wasted energy. This is quantifiable and aligns with the SDG sector listed on slide 10.
- Currency and import exposure on paper as a named constraint, which is local knowledge that no foreign ERP models.

---

## 11. Risks and what to do about them

| Risk | Severity | Action |
|---|---|---|
| No beneficiary data by Friday 18 September | Critical | Contact three publishers, not one. Fountain Publishers is currently a single point of failure. Document the outreach itself, since slide 9 requires evidence of requirements from actual beneficiaries. |
| Supervisor pattern-matches the title to slide 12 | High | Rename and rewrite the summary today, before the paper is read. |
| Repositioning read as evasion rather than substance | High | Be able to explain, on demand, why an irreversible discrete print run months ahead of a fixed deadline is a different decision class from reordering stock. The defence must be substantive, not linguistic. |
| A past cohort already did an inventory project | Medium | Slide 11 requires checking library books and the shared spreadsheets of past projects. Nobody has done this check yet. Do it, and be ready to name the difference. |
| Curriculum change breaks forecasting | Medium | Do not hide it. Make it an explicit input to the agent's reasoning and a discussion point in the report. |

---

## 12. Immediate actions

1. **Today.** Rewrite the title, executive summary and problem statement in the shared Google Doc, so that Isaac's polish pass works on the corrected version rather than the old one.
2. **Before Friday 18 September.** Outreach to three publishers, with the outreach record kept as part of the data collection deliverable.
3. **This week.** Check the college library and the shared past-project spreadsheets for prior inventory projects, and write down precisely how this project differs.
4. **Before the recording.** Add the "Why this is not an inventory management system" slide to the presentation deck.

---

## 13. Course criteria, and how the repositioned project meets each

Drawn from slide 9, "Qualities of a good ICT project".

| Criterion | How the repositioned project satisfies it |
|---|---|
| Originality and innovation | Agentic, action-taking AI under human authorisation, as distinct from a single model that outputs a prediction and stops |
| Extension of existing work | Builds on established inventory theory (reorder point, economic order quantity) and applies it to discrete print run commitment |
| Does not reinvent the wheel | Uses existing model and framework infrastructure rather than rebuilding it |
| Benefits communities | Protects publisher working capital, reduces paper waste, and protects access to textbooks within the term they are needed |
| Requirements from actual beneficiaries | Publisher outreach, with the data collection tool as the instrument |
| Problem supported by evidence | Publisher transactional data plus documented interviews |
| Within skill set, budget and time | Requirements and SRS this semester, build in BSE 4200 |
| Tests acquired knowledge such as algorithms | Forecasting, reorder point, safety stock, and order quantity optimisation are implemented by the team |
| Produces an artifact | Software agent plus review dashboard |
