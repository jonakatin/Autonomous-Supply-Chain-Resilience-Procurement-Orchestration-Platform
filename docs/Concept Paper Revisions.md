# Concept Paper Revisions

**Project:** Autonomous Supply Chain Resilience and Procurement Orchestration Platform
**Course:** BSE 4100
**Prepared:** 16 September 2026
**Purpose:** Paste-ready replacement text for the concept paper.

---

## How to use this document

The concept paper lives in the shared Google Doc owned by Isaac. Open it, set the mode selector in the top right to **Suggesting**, then work through the revisions below in order. Each revision gives the text to find and the text to replace it with. Isaac accepts or rejects each one.

The title does not change. It has already been submitted and accepted.

Tense note: a concept paper describes work not yet done, so the replacement text is written in **future tense**, in the **third person**, with no use of "we" or "I". This follows the lecturer's document format.

---

## Revision 1: Executive Summary

**Find the two paragraphs beginning** "In today's complex global market, Medium and Large Enterprises face persistent challenges managing multi-tiered inventory..."

**Replace with:**

> Manufacturers and publishers must commit capital to production inputs long before demand is known. The quantity chosen is a single, largely irreversible decision. Commit too much and working capital is locked in stock that may never sell. Commit too little and the selling window closes with demand unmet. Existing enterprise software records what has already happened and raises an alert once a fixed threshold is crossed. This leaves the forecasting, the cost reasoning and the supplier selection to human operators working under time pressure.
>
> The Autonomous Supply Chain Resilience and Procurement Orchestration Platform will address this commitment decision directly. The system will forecast demand from historical sales, model supplier lead times as distributions rather than fixed figures, and compute an optimal commitment quantity using established operations research methods. These will include the newsvendor model for single-period commitments and dynamic reorder point calculation for repeating ones. The system will then generate the resulting purchase order and draft the supplier correspondence, and will present the recommendation together with the reasoning that produced it for human authorisation. No commitment will be made without human approval.
>
> The decision engine will be domain-general, applying to any production industry that commits capital to inputs ahead of known demand. It will be validated on a single product line: educational textbooks and the paper used to produce them.

**Why:** the current opening describes the system as inventory control. The course coordinator's project guidelines list inventory management as a project type that must not be undertaken. The replacement describes the same system by the decision it makes rather than by the records it reads, and states the general engine and the single validation product together.

---

## Revision 2: Background and Problem Statement, opening

**Find the paragraph beginning** "In Uganda's rapidly expanding commercial landscape, Medium and Large Enterprises serve as critical economic anchors..."

**Replace with:**

> In Uganda's commercial landscape, medium and large enterprises operate under conditions that make production commitment decisions unusually difficult. Production inputs are frequently imported, so lead times are long and variable. Input costs are exposed to currency movement between the moment of commitment and the moment of sale. Demand is seasonal, and in the education sector it is tied to fixed school term dates that cannot be moved.
>
> Educational publishing shows the problem in its sharpest form. A publisher decides months in advance how many copies of a title to print. The decision is made once, because there is no practical opportunity to reorder within the selling window. The deadline is set by the start of the school term. A title that arrives late does not sell late. It loses that term's cohort entirely. A title printed in excess occupies warehouse space and working capital until the curriculum is revised, at which point the remaining copies are written off.

**Why:** replaces the general description of inventory blind spots with the specific decision the project addresses, and introduces the validation product early.

---

## Revision 3: Background, add after Revision 2

**Insert this paragraph immediately after the text from Revision 2:**

> Existing enterprise resource planning software does not model these conditions. Threshold-based reordering assumes that replenishment is continuous and incremental. That assumption does not describe a single binding commitment made ahead of a fixed deadline. Established systems are also priced and configured for operations considerably larger than those of a typical Ugandan medium enterprise, which places them out of practical reach.

**Why:** the current paper criticises "legacy ERP modules" without saying why they fail. This states the specific structural mismatch, which is a stronger argument than cost alone.

---

## Revision 4: Specific Objectives

**Replace the four existing specific objectives with these six.**

> 1. To determine how production commitment quantities are currently decided in Ugandan educational publishing, and to quantify the cost of over-commitment and under-commitment.
> 2. To develop a forecasting module that estimates demand as a distribution, incorporating seasonal variation and supplier lead time variability.
> 3. To implement a decision module that computes an optimal commitment quantity using the newsvendor model for single-period commitments and dynamic reorder point calculation for repeating ones.
> 4. To develop an agentic reasoning layer that selects a supplier, generates a purchase order, and drafts supplier correspondence, subject to human authorisation.
> 5. To construct an activity log that exposes the agent's reasoning, and to evaluate whether that reasoning earns practitioner trust, measured by the rate at which recommendations are overridden.
> 6. To evaluate the decision module against historical decisions, comparing the quantities it recommends with the quantities actually committed.

**Why:** the lecturer's guidance requires objectives to use action verbs that can be measured, such as determine, compare, verify, calculate and describe, and requires them to remain fixed once the work begins. The current objectives describe components to be built rather than outcomes to be measured. Objectives 1 and 6 are new and give the project measurable results.

---

## Revision 5: Proposed System Architecture

**Replace the four-layer table with this description, keeping the table afterwards as a technical appendix if preferred.**

> The system will operate as five stages.
>
> **Sense.** Ingest sales history, current stock, supplier records and cost structure from the enterprise's existing records, supporting spreadsheet and point-of-sale imports.
>
> **Forecast.** Estimate demand as a distribution rather than a single figure, decomposing seasonal variation across the term cycle, and estimate supplier lead time as a distribution from promised against actual delivery dates.
>
> **Decide.** Compute the optimal commitment quantity from the forecast distribution and the cost structure, then rank available suppliers on cost, reliability and lead time.
>
> **Explain.** Record each step of the reasoning in human-readable form, including the figures used and the assumptions made, and expose it as a live activity stream.
>
> **Approve.** Present the recommendation, the generated purchase order and the drafted correspondence to the responsible manager, who approves, modifies or rejects it. No action is dispatched without that authorisation.

**Why:** the four-layer table describes an architecture rather than a behaviour, and reads as generic enterprise structure. The five stages describe what the system does in terms a non-technical reader follows immediately, and make the human approval step visible rather than burying it in a layer.

---

## Revision 6: New section, to be inserted after the architecture section

**Insert a new numbered section titled "Analytical Methods".**

> The system will apply analysis at four levels.
>
> **Descriptive analysis** will establish sales velocity per title, the seasonal index across the term cycle, supplier lead time variance, stock ageing, classification of titles by revenue contribution, and working capital committed per title.
>
> **Diagnostic analysis** will decompose forecast error into trend, seasonal and residual components, and will attribute each failure to forecast error, supplier delay or an incorrect commitment quantity.
>
> **Predictive analysis** will forecast demand using Holt-Winters triple exponential smoothing across the term cycle, will model lead time as a distribution, and will estimate the probability that demand is not met within the commitment window.
>
> **Prescriptive analysis** will compute the optimal commitment quantity, the dynamic reorder point, and safety stock under combined demand and lead time variability, and will rank suppliers against those constraints.
>
> The central model is the newsvendor model, which addresses a single-period commitment made before demand is known, where the cost of committing too little differs from the cost of committing too much. A print run has exactly this structure. The optimal quantity is given by the critical ratio:
>
> Critical ratio = Cu / (Cu + Co)   ... (1)
>
> Q\* = F⁻¹(critical ratio)   ... (2)
>
> where Cu is the underage cost, being the margin lost on demand that cannot be met, Co is the overage cost, being the capital sunk in units never sold, and F is the cumulative distribution of forecast demand.
>
> Forecast accuracy will be evaluated using mean absolute percentage error and root mean square error, measured against a naive seasonal baseline, using walk-forward validation so that no future period influences a prediction of an earlier one.

**Why:** the project guidelines state that a project consisting only of basic data entry and retrieval must not be undertaken, and that information systems must demonstrate data analytics. This section makes the analytics explicit and names the algorithms, which also addresses the requirement that a project test acquired knowledge such as algorithms. Note that the lecturer's format requires every equation to be numbered, which is why equations 1 and 2 carry numbers.

---

## Revision 7: New section, to be inserted immediately after Revision 6

**Insert a new numbered section titled "Distinction from Inventory Management Systems".**

> The system is not an inventory management system. The distinction is set out below.

<!-- Table: Distinction between an inventory management system and the proposed system -->
| Inventory management system | Proposed system |
|---|---|
| Records what is currently held | Computes what should be committed in future |
| A person reads a report and decides | The system computes and reasons, a person authorises |
| Reactive alert at a fixed threshold | Forecast driven, lead time aware, seasonally adjusted |
| Output is a stock report | Output is a commitment quantity, a purchase order, supplier correspondence and a reasoning trace |
| Requires no analytical method | Applies forecasting, optimisation and multi-step agent reasoning |
| Data entry and retrieval | Autonomous decision support under human authority |

**Why:** the objection is predictable, so it is better answered in the document than raised in a review. Stating the distinction directly also demonstrates that the guidelines were read and understood.

---

## Revision 8: Agent Activity Log example

**Replace the cooking oil example with this one.**

> - 09:30:12 Monitoring: Evaluated 142 active titles against sales history for the previous three terms.
> - 09:30:14 Signal detected: Senior 3 Mathematics, title T-041. Forecast enrolment for Term 1 2027 is 11,800 pupils. Observed adoption rate is 0.74.
> - 09:30:15 Forecast: Demand estimated at 8,700 copies, standard deviation 2,100.
> - 09:30:17 Cost model: Unit print cost UGX 8,500.00. Selling price UGX 25,000.00. Salvage value UGX 500.00. Critical ratio 0.6735.
> - 09:30:18 Optimisation: Recommended commitment is 9,645 copies. This exceeds the forecast mean because under-commitment costs 2.06 times as much as over-commitment.
> - 09:30:19 Supplier: Printer P-003 selected. Quoted lead time 30 days. Observed mean 38 days, standard deviation 6 days. Commitment deadline 14 November 2026.
> - 09:30:20 Action: Purchase order PO-2026-089 generated.
> - 09:30:21 Action: Supplier correspondence drafted.
> - 09:30:22 Status: Awaiting manager authorisation.

**Why:** the existing example uses cooking oil and a fast-moving goods supplier, which contradicts the chosen validation product. The replacement also demonstrates the analysis rather than merely asserting it, since the entry at 09:30:18 shows a recommendation that a person would not have reached by estimation, and explains why.

---

## Revision 9: Expected Impact and Benefits

**Replace the four existing bullet points with these.**

> The following outcomes will be measured rather than assumed. Each is stated as a target to be tested against the historical record of a participating organisation.
>
> **Reduction in commitment error.** For each historical print run, the quantity the system recommends will be compared with the quantity actually committed, and the difference in cost calculated. This comparison, run against an organisation's own history, is the project's principal result.
>
> **Reduction in decision latency.** The interval between the point at which a commitment decision becomes necessary and the point at which the order is placed will be measured against the organisation's current practice.
>
> **Working capital released.** Capital committed to stock that the model would not have recommended will be quantified in shillings and expressed as days of working capital.
>
> **Reduction in material waste.** Copies that would not have been printed will be converted into kilograms of paper, using the page count and paper weight of each title.
>
> **Auditability.** Every recommendation will carry a complete record of the figures, assumptions and reasoning that produced it, and no order will be dispatched without recorded human authorisation.

**Why:** the current text claims an 80 percent reduction in procurement overhead. That figure has no source and was produced by a language model during an earlier drafting session. An unsupported percentage invites a question that cannot be answered. Each replacement states what will be measured and how, which is defensible under examination. The waste figure is derived from data the project already collects, which keeps the environmental claim quantified rather than rhetorical.

---

## Revision 10: Project Roadmap

**Move the eight-week development roadmap to an appendix titled "Appendix A: Implementation Plan for BSE 4200".**

**Why:** the BSE 4100 objectives are to identify a problem, propose a solution and document requirements. The listed deliverables for this semester are the concept paper, the data collection tool, the requirements specification and the report. Development belongs to BSE 4200. A development roadmap in the main body consumes space that the problem statement and beneficiary evidence need, and suggests the project is being built before its requirements are established.

---

## Revision 11: Vocabulary

**Search the whole document and replace these terms wherever they appear in prose.**

<!-- Table: Vocabulary replacements to apply throughout the concept paper -->
| Replace | With |
|---|---|
| inventory management, inventory control | procurement decision, commitment decision |
| inventory software | enterprise procurement software |
| inventory velocity | sales velocity |
| monitors inventory | monitors demand and stock position |
| reorder quantity | commitment quantity |
| orchestration platform | system |
| Model Context Protocol, MCP | remove from prose, retain in the technology stack table only |
| stockout | unmet demand within the selling window |

**Why:** the title is already free of the banned vocabulary, but the body is not. A reader who stops at the first paragraph must not conclude that the project is an inventory system. Retaining the technical terms in the technology stack table is appropriate, since a table of tools is read as specification rather than as description.

---

## Summary of changes

<!-- Table: Summary of revisions, their location and their purpose -->
| Revision | Section | Purpose |
|---|---|---|
| 1 | Executive Summary | Reframe from inventory control to commitment decision |
| 2 and 3 | Background | Specific problem conditions, and why existing software fails |
| 4 | Objectives | Measurable action verbs, add outcome objectives |
| 5 | Architecture | Five stages replacing four layers |
| 6 | New: Analytical Methods | Demonstrate analytics and named algorithms |
| 7 | New: Distinction from Inventory Management | Answer the predictable objection |
| 8 | Activity Log | Align example with the validation product |
| 9 | Expected Impact | Remove the unsupported 80 percent claim |
| 10 | Roadmap | Move development plan to an appendix |
| 11 | Throughout | Vocabulary replacement |

The title, the technology stack and the overall structure of the paper are unchanged.
