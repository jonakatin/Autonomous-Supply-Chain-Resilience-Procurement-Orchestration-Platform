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

The project has been **described** by its **data source** instead of by its **decision**.

Inventory is the input. The output is a capital commitment decision. Those are two different projects, and only one of them appears on the banned list.

| Currently described as | Should be described as |
|---|---|
| Tracking stock levels across distribution centres | Deciding how much capital to commit, and when |
| Preventing stockouts | Preventing irreversible over-commitment and missed seasonal windows |
| Inventory optimisation platform | Procurement decision agent with human authorisation |
| Generic SKUs across regional hubs | Textbook print runs against school term deadlines |

---

## 3. A general engine, validated on one product

The lecturer asked the team to choose a single product. The team also intends the system to serve any production industry that commits capital ahead of demand. These are not in conflict, because they describe different layers:

- **The system is domain-general.** A procurement decision engine for any production industry with supplier lead times, demand variability and irreversible capital commitment. This is the contribution.
- **The validation case is a single product.** Textbooks, and the paper behind them. This is the evidence, and it is what satisfies the lecturer's instruction and slide 9's requirement for requirements from actual beneficiaries.

State both explicitly. "A general procurement decision engine, validated on textbook print runs" is a stronger framing than either half alone, and it is how credible engineering work is normally structured. The generality is then carried in the paper by a named section on generalisability, plus future work naming the other industries the engine extends to.

Why textbooks are a good validation case rather than a limiting one:

Textbook publishing is not a generic inventory problem. It is a **discrete, irreversible, high-value commitment made months ahead of demand, against a hard seasonal deadline, using imported inputs on long lead times.** It exercises every hard property the general engine must handle, which is exactly what makes it a good test case.

- A publisher decides in one moment how many copies to print. There is no incremental reorder. It is one large, binding commitment.
- The deadline is fixed by the school term. Missing it does not delay the sale, it destroys the sale, because a textbook that arrives after the term started has lost that term's cohort entirely.
- Paper is imported, so lead times are long and variable, and costs are exposed to currency movement before any revenue arrives.
- Demand is **non-stationary**. A curriculum revision can reduce demand for a title to zero overnight.

That last property is a genuine statistical difficulty, and the brief's recommendation is to make it explicit rather than hide it. A project that identifies a hard property of its domain and designs around it is stronger than one that assumes well-behaved data.

---

## 4. Title: keep it

**Decision: the existing title stands.** "Autonomous Supply Chain Resilience and Procurement Orchestration Platform" has already been submitted and accepted by the lecturer. Changing an accepted title creates a paperwork problem, signals indecision to a supervisor, and gains nothing.

An earlier draft of this brief recommended renaming. That recommendation was wrong, for a specific reason: the title does not contain the word "inventory". It says supply chain and procurement. The title was never what exposed the project to the banned list.

**The exposure is in the body text, not the title.** Three sentences do most of the damage:

- Executive summary: "transition inventory control from passive record-keeping"
- Executive summary: "Traditional enterprise inventory software operates reactively"
- Section 2 opening: "challenges managing multi-tiered inventory"

A reader who sees only the title sees a procurement system. A reader who reaches the first paragraph sees an inventory system. Rewrite those sentences in procurement-decision language and the risk is handled, with the title untouched.

Product name stays **LogicSynapse AI**.

---

## 5. The one-line pitch

Replace the current executive summary opening with this:

> Ugandan publishers commit to a print run months before they know demand. Print too many and the cash is pulped. Print too few and you lose an entire school term, because there is no second chance at a term. LogicSynapse is an AI agent that makes that call, shows its reasoning line by line, and waits for a human to approve before a single shilling is spent.

Fifteen seconds, names the beneficiary, names the money, names the consequence, and contains no banned vocabulary.

Where the general framing is needed instead, for example when the audience is not publishing-specific, use this and then drop into the textbook case as the worked example:

> Any manufacturer has to commit money to raw materials long before it knows what demand will be. Commit too much and the capital is dead. Commit too little and you miss the window entirely. LogicSynapse is an AI agent that makes that commitment decision, shows its reasoning step by step, and waits for a human to approve before any money moves. We validate it on textbook printing, where the deadline is a school term and getting it wrong costs a publisher the whole cohort.

---

## 6. Add a section: "Why this is not an inventory management system"

Pre-empting the objection is stronger than hoping it is not raised. Include this table in the concept paper and on a presentation slide.

| Inventory management system | LogicSynapse AI |
|---|---|
| Records what is currently held | Decides what to commit to in future |
| Human reads a dashboard and decides | Agent decides and reasons, human authorises |
| Reactive alert at a fixed threshold | Forecast-driven, lead-time aware, seasonally adjusted |
| Output is a report | Output is a purchase order, a supplier email, and a full reasoning trace |
| Satisfies no analytics requirement | Descriptive, diagnostic, predictive and prescriptive analytics (see section 7b) |
| Data entry and retrieval | Autonomous action under human authority |

---

## 7. Draw the algorithmic line clearly

Slide 9 requires that a project "tests acquired knowledge such as algorithms." A supervisor will reasonably ask what the team engineered versus what the language model provided. Answer it before it is asked.

**The team's engineering work:**
- Newsvendor optimal order quantity for the single-period print run commitment
- Demand forecasting by Holt-Winters triple exponential smoothing over the term cycle
- Dynamic reorder point incorporating lead time variance
- Safety stock computation under joint demand and lead time variability
- Economic order quantity adapted to discrete, indivisible print runs
- Curriculum-change risk as an explicit input to the decision
- Forecast validation by walk-forward backtesting against a naive seasonal baseline

Section 7b sets out these analytics in full, with formulas and a worked example.

**The language model's role:**
- Orchestrating multi-step tool calls
- Selecting among suppliers given the computed constraints
- Drafting the natural-language purchase order and supplier email

The decision mathematics is classical, implementable, and examinable. The language model wraps it. Stating this division explicitly converts a perceived weakness into a demonstrated strength.

---

## 7b. The analytics layer, and how slide 11 is satisfied

Slide 11 states: "DON'T DO A PROJECT with Only Basic data entry and retrieval (Information Systems MUST Show Data analytics)."

This section exists so that the analytics can be pointed at directly rather than asserted. The analytics run in four tiers.

| Tier | Question answered | What is computed |
|---|---|---|
| Descriptive | What happened? | Sales velocity per title, term-cycle seasonal index, supplier lead time variance, stock ageing, ABC classification by revenue contribution, working capital tied per title |
| Diagnostic | Why did it happen? | Forecast error decomposed into trend, seasonal and residual components; stockout attribution to forecast error, lead time slip or under-commitment; supplier reliability attribution |
| Predictive | What will happen? | Demand forecasting by Holt-Winters triple exponential smoothing across the term cycle; depletion date projection; lead time modelled as a distribution rather than a point estimate; probability of stockout within the lead time window |
| Prescriptive | What should be done? | Newsvendor optimal order quantity, dynamic reorder point, safety stock under joint demand and lead time variance, order quantity adjusted for press setup cost and volume price breaks, multi-criteria supplier selection |

### The core model: a print run is a newsvendor problem

A print run is a single-period commitment made before demand is known, with no opportunity to reorder inside the selling window, and with asymmetric costs on either side of the error. This is exactly the problem class the newsvendor model addresses, a classical result in operations research attributed to Arrow, Harris and Marschak.

**Critical ratio** = Cu / (Cu + Co)

**Optimal quantity** Q* = F inverse (critical ratio), where F is the cumulative distribution of forecast demand.

Where Cu is the underage cost, being the margin lost on demand that could not be filled, and Co is the overage cost, being the capital sunk in units that are never sold.

**Worked example.**

| Input | Value |
|---|---|
| Print cost per copy | UGX 8,500.00 |
| Sale price to schools | UGX 25,000.00 |
| Salvage value of an unsold copy | UGX 500.00 |
| Underage cost Cu | UGX 16,500.00 |
| Overage cost Co | UGX 8,000.00 |
| Critical ratio | 0.6735 |
| Forecast demand | Normal, mean 10,000, standard deviation 2,500 |
| z at 0.6735 | 0.45 |
| **Optimal print run Q*** | **11,125 copies** |

The result is the argument in a single line. A manager estimating by eye orders 10,000, the mean. The analysis prescribes 11,125, because underage costs roughly twice what overage costs and the optimum therefore sits deliberately above the mean. That number cannot be produced by data entry and retrieval. It falls out of a cost structure combined with a demand distribution, which is precisely what slide 11 asks to see.

### Supporting formulas

**Safety stock** under both demand and lead time variability:

SS = Z × square root of ( LT_mean × sigma_d squared + d_mean squared × sigma_LT squared )

**Reorder point:**

ROP = ( d_mean × LT_mean ) + SS

**Economic order quantity**, as the continuous-replenishment baseline the print run case is compared against:

EOQ = square root of ( 2 × D × S / H )

where D is annual demand, S is setup or order cost, and H is holding cost per unit per year.

### Validating the analytics

Analytics that are never validated are assertions. The report must include:

- Forecast accuracy as MAPE and RMSE, measured against a naive seasonal baseline such as "same as the equivalent term last year"
- **Walk-forward backtesting**, so that no future term leaks into a past prediction
- An honest statement of the result. If the model does not beat the naive baseline, report that. It is still a finding, and reporting it is better science than quietly tuning until a favourable number appears.

### Making the analysis visible

A practical trap worth naming. If every screen in the dashboard is a table of rows, a reader sees data entry and retrieval regardless of the quality of the mathematics behind it. At least three screens must display analysis rather than records:

1. The demand forecast with its confidence band
2. The service level versus cost tradeoff curve, showing why Q* sits where it does
3. Supplier reliability as distributions, not as supplier records

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
| Supervisor pattern-matches the body text to slide 12 | High | Rewrite the executive summary and section 2 opening in procurement-decision language today. The title stays as submitted. |
| Repositioning read as evasion rather than substance | High | Be able to explain, on demand, why an irreversible discrete print run months ahead of a fixed deadline is a different decision class from reordering stock. The defence must be substantive, not linguistic. |
| A past cohort already did an inventory project | Medium | Slide 11 requires checking library books and the shared spreadsheets of past projects. Nobody has done this check yet. Do it, and be ready to name the difference. |
| Curriculum change breaks forecasting | Medium | Do not hide it. Make it an explicit input to the agent's reasoning and a discussion point in the report. |

---

## 12. Immediate actions

1. **Today.** Rewrite the executive summary and problem statement in the shared Google Doc, removing inventory-management vocabulary in favour of procurement-decision vocabulary. Leave the title as submitted. Do this before Isaac's polish pass, so he works on the corrected version.
2. **Before Friday 18 September.** Outreach to three publishers, with the outreach record kept as part of the data collection deliverable.
3. **This week.** Check the college library and the shared past-project spreadsheets for prior inventory projects, and write down precisely how this project differs.
4. **Before the recording.** Add the "Why this is not an inventory management system" slide to the presentation deck.

---

## 13. Course criteria, and how the repositioned project meets each

Drawn from slide 9, "Qualities of a good ICT project".

| Criterion | How the repositioned project satisfies it |
|---|---|
| Originality and innovation | Agentic, action-taking AI under human authorisation, as distinct from a single model that outputs a prediction and stops |
| Single product focus, as instructed | Textbooks and paper named as the validation product, with the engine itself kept domain-general |
| Extension of existing work | Builds on established inventory theory (reorder point, economic order quantity) and applies it to discrete print run commitment |
| Does not reinvent the wheel | Uses existing model and framework infrastructure rather than rebuilding it |
| Benefits communities | Protects publisher working capital, reduces paper waste, and protects access to textbooks within the term they are needed |
| Requirements from actual beneficiaries | Publisher outreach, with the data collection tool as the instrument |
| Problem supported by evidence | Publisher transactional data plus documented interviews |
| Within skill set, budget and time | Requirements and SRS this semester, build in BSE 4200 |
| Tests acquired knowledge such as algorithms | Forecasting, reorder point, safety stock, and order quantity optimisation are implemented by the team |
| Produces an artifact | Software agent plus review dashboard |
