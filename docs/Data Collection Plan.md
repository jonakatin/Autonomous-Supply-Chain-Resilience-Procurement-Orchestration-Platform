MAKERERE UNIVERSITY

COLLEGE OF COMPUTING AND INFORMATION SCIENCES

**DATA COLLECTION PLAN**

**Autonomous Supply Chain Resilience and Procurement Orchestration Platform**

**PROGRAM:** Software Engineering
**COURSE UNIT:** Software Engineering Project 1
**COURSE CODE:** BSE 4100
**YEAR OF STUDY:** 4
**GROUP MEMBERS:** Jonathan Katongole, Dev Johnson, Bridget Bataringaya, Isaac Mwesigwa

**Purpose:** A practical plan for collecting, protecting, preparing and using the data required to design, develop, test and evaluate the proposed system.

---

## 1. Overview of the Data Collection Plan

The project is a procurement decision agent. It forecasts demand, computes an optimal commitment quantity, drafts the resulting purchase order, and presents its reasoning to a human for authorisation. Because the system makes a financial commitment decision rather than simply recording transactions, the data required is different in kind from the data an inventory system would need. It must support forecasting, cost modelling, and the measurement of decision quality.

The engine is designed to be domain-general, applying to any production industry that commits capital to inputs ahead of known demand. For this project it is **validated on a single product line: educational textbooks and the paper used to produce them.** Data collection therefore targets that validation case.

Four complementary data sources are used.

<!-- Table: Data categories, sources and purpose -->
| Data category | What will be collected | Why it is needed | Main source or tool |
|---|---|---|---|
| Practitioner research data | How commitment decisions are made today, who approves them, what goes wrong, attitudes to delegating authority to software | Requirements gathering and problem validation | Structured interviews, questionnaire |
| Real operational data | Historical print runs, sales by term, unit costs, supplier lead times promised against actual, write-offs | Estimate the demand distribution and cost structure the decision model requires | Publisher and printer records, CSV or Excel exports |
| Synthetic data | Generated title histories seeded from the real sample, covering normal and stress scenarios | Provide volume and controlled edge cases for development and testing | Python, Pandas, NumPy |
| Prototype evaluation data | Usefulness, clarity of the reasoning trace, trust, willingness to approve | Evaluate the agent and its explainability | Usability tasks, post-test questionnaire |

> **Key principle:** collect only the operational information the decision model needs. Never request banking credentials, signatory details, customer personal data, or confidential commercial terms held with named third parties.

---

## 2. Purpose of Data Collection

To obtain reliable evidence about how production commitment decisions are currently made and mismade, and to obtain the historical demand and cost data required to estimate, calibrate and evaluate the proposed decision agent.

---

## 3. Main Data Collection Objective

To collect the practitioner, operational and evaluation data required to design, develop and evaluate an autonomous procurement decision agent, validated on educational textbook production.

---

## 4. Specific Data Collection Objectives

1. Establish how production and procurement commitment quantities are currently decided, by whom, and on what evidence.
2. Determine the frequency, cause and cost of the two failure modes: over-commitment that ties up capital, and under-commitment that misses the selling window.
3. Establish supplier and printer lead times as **distributions**, capturing promised against actual, rather than as single figures.
4. Obtain the cost structure required by the decision model: unit production cost, setup cost, selling price, and the salvage or write-off value of unsold units.
5. Obtain historical commitment quantities against realised sales, per title, over enough cycles to estimate a demand distribution.
6. Determine practitioner attitudes toward delegating commitment decisions to software, and which actions must always require human authorisation.
7. Generate realistic synthetic data, seeded from the real sample, for development and controlled edge-case testing.
8. Collect usability, trust and explainability feedback once the prototype exists.

---

## 5. Target Population and Sampling

The respondents are **organisations and the practitioners inside them**, not members of the general public. This is the most important structural difference between this plan and a consumer-facing study, and it changes the sampling approach entirely.

Target organisation types:

- Educational publishers, being the primary beneficiary
- Commercial printers who execute print runs
- Paper suppliers and importers, being the upstream input
- Distributors and bookshops, who hold demand signal
- School procurement officers, who generate the demand

Target roles inside those organisations:

- Production or print managers, who make or recommend the quantity decision
- Procurement or purchasing officers
- Finance managers, who feel the working capital consequence
- Warehouse or stock controllers, who see the write-offs
- Sales or distribution managers, who see the missed demand

### 5.1 Proposed Sample Targets

Sample sizes are deliberately small and expert-weighted. The population of educational publishers in Uganda is limited, so a mass survey is neither achievable nor appropriate. Depth substitutes for volume, and this must be stated explicitly in the report so that the small sample reads as a considered design choice rather than a shortfall.

<!-- Table: Proposed sample targets by activity -->
| Activity | Practical target | Reason |
|---|---|---|
| Organisations engaged | 5 to 8; aim for 6 | Enough to show the problem is not specific to one firm |
| Semi-structured interviews | 12 to 20; aim for 15 | Two to three roles per organisation gives cross-checked accounts |
| Questionnaire respondents | 30 to 60 | Broader validation across smaller publishers, printers and bookshops |
| Organisations providing operational data | 2 to 4; aim for 3 | Enough to estimate demand distributions and compare cost structures |
| Historical period per title | 3 to 5 years, or at least 6 selling cycles | Needed to estimate seasonality and a demand distribution |
| Titles covered | 20 to 50 per contributing publisher | Enough for per-title modelling and ABC classification |
| Synthetic titles | 500 to 2,000 | Scalable development and testing |
| Synthetic commitment cycles | 10,000 or more | Controlled edge cases and stress scenarios |
| Prototype evaluation participants | 8 to 15 practitioners | Evidence on trust, clarity and willingness to approve |

### 5.2 Sampling Approach

**Purposive expert sampling** is used throughout, since the value of a respondent depends entirely on whether they participate in commitment decisions. Convenience sampling is used only as a secondary route to reach smaller printers and bookshops for the questionnaire.

**Snowball sampling** is expected to be productive: the publishing and printing community in Kampala is small and interconnected, so each interviewee should be asked to refer one further contact. This is the most realistic route to reaching the target of 6 organisations.

---

## 6. Data Collection Tools and Where to Use Them

<!-- Table: Data collection tools and their use -->
| Task | Recommended tool | How and where it will be used |
|---|---|---|
| Organisation outreach | Formal letter, email, physical visit | Introductory letter on university letterhead, followed by a visit. Physical visits are expected to substantially outperform email in this sector |
| Outreach tracking | Google Sheets contact log | Record every approach, date, outcome and follow-up. This log is itself a required deliverable, see section 7 |
| Interviews | Face to face, preferably on site | 30 to 45 minutes, semi-structured. On-site visits allow observation of the warehouse and current records |
| Interview capture | Notebook and Microsoft Word | Notes by default. Audio only with explicit permission |
| Questionnaire | Google Forms | Distributed to smaller publishers, printers and bookshops through associations and referrals |
| Operational data request | Excel template supplied by the team | A one-page template lowers the effort for the contributing organisation, which materially raises the response rate |
| Data exchange format | CSV | Machine readable, simple for the contributor to export |
| Data cleaning | Python and Pandas | Normalise titles, reconcile editions, handle missing cycles |
| Synthetic generation | Python, Pandas, NumPy | Seeded from the real sample so generated patterns remain realistic |
| Modelling and analysis | Jupyter Notebook, VS Code | Forecasting, newsvendor optimisation, backtesting |
| Application database | PostgreSQL | Structured storage during development |
| Code and documents | GitHub | Code, scripts, synthetic data and templates only. Never raw commercial data |
| Prototype evaluation | Guided task session and Google Forms | Post-test ratings and open comment |

---

## 7. Phase 1: Organisation Outreach and Evidence of Approach

This phase has no equivalent in a consumer study and is placed first because it is the binding constraint on the entire project. Access to a publisher determines whether real data exists at all.

The course requires that the project result from requirements gathered from actual beneficiaries and that the problem be supported by evidence. **The outreach record is therefore part of the evidence, independent of whether any single organisation agrees to participate.** A refusal that is documented still demonstrates a genuine attempt and still yields a finding.

### 7.1 Outreach Contact Log

Maintain this log from the first approach. Include it as an appendix in the final report.

<!-- Table: Fields recorded in the outreach contact log -->
| Field | Purpose |
|---|---|
| Organisation | Name of publisher, printer, supplier or distributor |
| Contact person and role | Who was approached |
| Date of first contact | Establishes the timeline of effort |
| Channel | Letter, email, phone, physical visit |
| Outcome | No response, declined, agreed to interview, agreed to share data |
| Reason given if declined | Often a finding in itself, for example commercial sensitivity |
| Follow-up date | Evidence of persistence |
| Data received | What was actually obtained, and when |

### 7.2 Outreach Rule

**Approach a minimum of three publishers, not one.** A single contact is a single point of failure for the entire project. Approaches should be staggered but concurrent, so that a slow response from one does not consume the schedule.

### 7.3 What to Offer in Return

Access improves markedly when the request is reciprocal. Offer, in writing:

- A written summary of the analysis of their own data, returned to them
- Anonymity in the report, with the organisation referred to by a code such as Publisher A
- A demonstration of the prototype once it exists
- A confidentiality undertaking signed by all four team members

---

## 8. Phase 2: Semi-Structured Interviews

### 8.1 Interview Guide

Questions are ordered to move from current practice, through failure, to attitudes about delegation. Ask for specific recent instances rather than general opinions, since general opinions are unreliable and specific incidents are checkable.

**Current practice**
1. Walk me through how you decided the quantity for your most recent print run.
2. Who proposes that number, and who has to approve it before money is committed?
3. What information is in front of you when you make that decision?
4. How long does it take from realising a decision is needed to the order being placed?

**Failure modes**
5. Tell me about a title where you printed too many. What happened to the unsold copies?
6. Tell me about a title where you printed too few. What did that cost you?
7. Which of those two mistakes is more expensive for you, and why?
8. How often does a supplier deliver later than promised, and what do you do when that happens?
9. Has a curriculum change ever left you holding stock you could not sell?

**Cost structure**
10. What goes into the cost of a copy, and how does that change with the size of the run?
11. What happens financially to a copy that is never sold?

**Delegation and trust**
12. If software proposed a print quantity, what would you need to see before you trusted it?
13. Which decisions could software prepare for you, and which must a person always approve?
14. What would make you stop using such a system?

**Close**
15. Who else should we be speaking to?

Recommended length is 30 to 45 minutes. Use written notes by default. Request permission explicitly before any recording.

---

## 9. Phase 3: Real Operational Data

### 9.1 The Three Priority Requests

If an organisation will share only a little, these three items matter most, because without them the decision model cannot be calibrated and degenerates into arithmetic on a guess.

1. **Historical print run quantities against realised sales, per title, across several cycles.** Without this there is no demand distribution.
2. **Unit production cost at realistic run sizes, including setup cost.**
3. **Selling price, and what happens financially to unsold copies.**

### 9.2 Core Datasets

**Title master**

<!-- Table: Title master dataset -->
| Field | Example | Priority | Purpose |
|---|---|---|---|
| title_id | T001 | Required | Anonymous identifier for the title |
| subject | Mathematics | Required | Grouping and comparison |
| level | Senior 3 | Required | Links demand to school cohort size |
| curriculum_code | NCDC-S3-MATH | Useful | Detects exposure to curriculum revision |
| edition | 4th | Required | Editions reset the demand history |
| edition_date | 2024-01 | Required | Marks where a history becomes non-comparable |
| pages_per_copy | 240 | Useful | Converts overprint into paper weight |
| paper_weight_gsm | 70 | Useful | Same, and supports the waste measure |
| status | Active | Required | Distinguishes live titles from withdrawn ones |

**Print run history**, the central dataset for the decision model

<!-- Table: Print run history dataset -->
| Field | Example | Priority | Purpose |
|---|---|---|---|
| run_id | R0451 | Required | Identifies the commitment |
| title_id | T001 | Required | Links to the title |
| decision_date | 2025-06-14 | Required | When the commitment was made |
| quantity_committed | 10,000 | Required | The decision actually taken, the baseline the model is compared against |
| unit_production_cost | 8500.00 | Required | Overage cost input |
| setup_cost | 1200000.00 | Useful | Supports order quantity optimisation |
| printer_id | P003 | Required | Links to supplier performance |
| delivery_promised | 2025-07-20 | Required | Lead time promised |
| delivery_actual | 2025-08-02 | Required | Lead time realised, giving the variance |

**Sales history**

<!-- Table: Sales history dataset -->
| Field | Example | Priority | Purpose |
|---|---|---|---|
| title_id | T001 | Required | Links to the title |
| period | 2025-T3 | Required | Term or month, the unit of the seasonal cycle |
| units_sold | 8,750 | Required | The realised demand signal |
| unit_selling_price | 25000.00 | Required | Underage cost input |
| channel | Direct to school | Useful | Separates demand streams |

**Stock and write-off**

<!-- Table: Stock and write-off dataset -->
| Field | Example | Priority | Purpose |
|---|---|---|---|
| title_id | T001 | Required | Links to the title |
| date | 2026-03-31 | Required | Point of observation |
| units_on_hand | 1,250 | Required | Measures over-commitment |
| units_written_off | 300 | Required | Quantifies realised waste |
| write_off_reason | Curriculum change | Required | Distinguishes causes of loss |
| salvage_value_per_unit | 500.00 | Required | Completes the overage cost |

**Supplier and input**

<!-- Table: Supplier and input dataset -->
| Field | Example | Priority | Purpose |
|---|---|---|---|
| supplier_id | P003 | Required | Anonymous identifier |
| input_type | Printing | Required | Printing, paper or other |
| lead_time_promised_days | 30 | Required | Baseline |
| lead_time_actual_days | 43 | Required | Yields the lead time distribution |
| minimum_order_quantity | 5,000 | Useful | Constrains the optimisation |
| price_break_schedule | See note | Useful | Makes the cost curve non-linear and realistic |
| origin_country | Kenya | Useful | Import exposure |

### 9.3 Minimum Viable Record

Where records are incomplete, the smallest dataset that still supports the model is: title identifier, period, quantity committed, units sold, unit production cost, unit selling price, and lead time promised against actual.

### 9.4 If No Organisation Shares Data

This contingency must be stated in the plan rather than improvised later.

1. Use interview testimony to establish **plausible ranges** for each cost and lead time parameter, and record who gave each range.
2. Use published sources for the demand anchor, since enrolment statistics by class level are a matter of public record and give a defensible upper bound on textbook demand.
3. Generate the dataset synthetically from those ranges, documenting every assumption and its source.
4. State the limitation plainly in the evaluation chapter. A documented synthetic dataset with sourced parameters is acceptable work. An undocumented one is not.

---

## 10. Data Needed for Each Analytical Component

<!-- Table: Data required by each analytical component -->
| Component | Data required | Output |
|---|---|---|
| Demand forecasting | Sales history by term over several cycles, per title | Forecast mean and variance |
| Seasonal decomposition | At least two full annual cycles | Term-cycle seasonal index |
| Lead time modelling | Promised against actual delivery dates | Lead time mean and standard deviation |
| Safety stock | Demand variance and lead time variance | Buffer quantity for a target service level |
| Newsvendor optimisation | Unit production cost, selling price, salvage value, demand distribution | Optimal commitment quantity |
| Supplier selection | Cost, lead time reliability, minimum order quantity | Ranked supplier recommendation |
| Decision quality evaluation | Historical quantity committed against units sold | Comparison of the model against what the humans actually did |
| Waste measure | Units written off, pages per copy, paper weight | Kilograms of paper not wasted |

The final row is the only environmental claim the project makes. It is a **computed output** derived from data collected for other purposes, not an assertion. No unquantified environmental claim should appear anywhere in the project documents.

---

## 11. Phase 4: Synthetic Data

Synthetic data is **seeded from the real sample** so that generated patterns remain realistic. It is never a substitute for having spoken to real practitioners.

### 11.1 Scenarios to Generate

<!-- Table: Synthetic data scenarios -->
| Scenario | Why it is needed |
|---|---|
| Stable title with clean seasonality | Baseline case |
| New title with no history | Tests the cold-start path |
| Title hit by a curriculum revision mid-life | Tests the non-stationary case |
| Supplier who chronically delivers late | Tests lead time variance handling |
| Demand spike from an unexpected adoption | Tests under-commitment behaviour |
| Long slow decline toward withdrawal | Tests over-commitment behaviour |
| Sharp input cost movement between decision and delivery | Tests cost sensitivity |
| Missing and erroneous records | Tests data quality handling |

---

## 12. Data Cleaning and Preprocessing Plan

1. Normalise title names and reconcile them to a single identifier, since the same book often appears under several spellings.
2. Treat a new edition as a **break in the series**. Demand history does not carry across an edition boundary without adjustment, and ignoring this is the most likely source of a silently wrong forecast.
3. Align all periods to a consistent term calendar.
4. Reconcile units sold against units produced and written off, and investigate any title where the three do not balance.
5. Record every correction in a cleaning log, so the report can state what was changed and why.
6. Flag, rather than silently drop, titles with too few cycles to model.

---

## 13. Data Labelling, Splits and Leakage

The ground truth for this project is the **realised demand** for each title and cycle, together with the quantity that was actually committed. That pairing allows the model's recommendation to be compared against the human decision.

Splitting must be **chronological, never random.** A random split would place a future term in the training set and a past term in the test set, which leaks information forward and produces an accuracy figure that cannot be reproduced in practice.

Use **walk-forward validation**: train on cycles up to term N, predict term N plus one, advance, repeat. Report accuracy as MAPE and RMSE against a naive seasonal baseline such as "the same as the equivalent term last year".

---

## 14. Confidentiality, Consent and Ethics

This project handles **commercially sensitive business data** and a limited amount of personal data. Both require care, for different reasons.

### 14.1 Information That Must Not Be Collected

- Banking credentials, signatory details or payment authorisations of any kind
- Personal data of the publisher's own customers, including pupils, parents and teachers
- Confidential contract terms held with named third parties
- Any document the organisation has not knowingly agreed to release

### 14.2 Commercial Confidentiality

- Provide a written confidentiality undertaking signed by all four members before requesting data.
- Anonymise organisations in every document, referring to them as Publisher A, Printer B and so on.
- Apply the same treatment to cost figures where an organisation asks for it, using index values relative to a base rather than absolute figures.
- Raw commercial data is never committed to GitHub. Only synthetic data, templates and code are.

### 14.3 Personal Data

Interview participants are identifiable individuals, so the **Data Protection and Privacy Act, 2019** applies to their personal data. In practice this means collecting only the role and organisation rather than personal contact details beyond what is needed, obtaining consent before recording, and not publishing names without permission.

### 14.4 Sample Consent Statement

> We are final year Software Engineering students at Makerere University. We are studying how production and procurement quantity decisions are made, in order to design a system that supports those decisions. Participation is voluntary and you may stop at any time or decline any question. Your organisation will not be named in our report. Any figures you share will be used only for this academic project, will be stored securely, and will not be shared outside our team and our supervisor. We will send you a summary of our analysis of your data.

---

## 15. Data Storage and Access Control

<!-- Table: Data storage locations and access control -->
| Data type | Location | Access |
|---|---|---|
| Raw commercial data | Restricted shared drive folder | Four team members and the supervisor only |
| Anonymised working data | Project working folder | Team |
| Synthetic data | Repository | Public, since it contains nothing real |
| Interview notes | Restricted folder, anonymised on entry | Team |
| Consent records and outreach log | Restricted folder | Team |
| Code and templates | GitHub | Public |

A `.gitignore` must exclude raw data folders, credentials and any file containing real commercial figures, and it must be in place **before** the first real dataset arrives, not after.

---

## 16. Data Quality Assurance

- Cross-check figures given in interview against the figures in the supplied records, and investigate discrepancies rather than averaging them.
- Have a second team member review every cleaning decision that changes a value.
- Verify that units sold never exceeds units produced plus opening stock.
- Check lead time records for impossible values such as negative durations.
- Confirm each title has enough cycles to model before including it, and record those excluded.

---

## 17. Data Analysis Plan

### 17.1 Interview Analysis

Thematic analysis. Code transcripts against the decision stages: how the quantity is set, what evidence is used, what goes wrong, what approval is required, and what would earn trust. Report the frequency with which each theme appears across organisations, so that a single strong opinion is not mistaken for a pattern.

### 17.2 Questionnaire Analysis

Descriptive statistics with cross-tabulation by organisation size and role, since a finance manager and a production manager are expected to weigh over-commitment and under-commitment differently. That difference, if it appears, is a finding worth reporting.

### 17.3 Operational Data Analysis

1. Per-title demand distribution, with mean, variance and distributional shape.
2. Seasonal decomposition across the term cycle.
3. Lead time distribution per supplier, promised against actual.
4. Estimation of underage and overage cost from the cost structure.
5. Newsvendor optimal quantity per historical decision point.
6. **Back-comparison against the human decision**, being the headline result: for each historical print run, what the model would have committed against what was committed, and the cost difference.
7. Forecast accuracy under walk-forward validation, against a naive seasonal baseline.

Item 6 is the most persuasive output the project can produce, because it uses the organisation's own history to show what the system would have changed.

---

## 18. Phase 5: Prototype Evaluation

Participants are practitioners, not students, because the question being tested is whether a person who actually holds this authority would delegate part of it.

### 18.1 Tasks

1. Review a recommended commitment and decide whether to approve, modify or reject it.
2. Find the reason the agent recommended that quantity.
3. Identify which supplier the agent selected and why.
4. Override a recommendation and record a reason.

### 18.2 Post-Test Statements, Five-Point Scale

1. I understood why the system recommended this quantity.
2. The reasoning shown was sufficient for me to make a decision.
3. I would be comfortable approving this recommendation in my actual work.
4. The system made clear what it could not know.
5. I always felt in control of the final decision.
6. I would trust this system more after using it for a season.

### 18.3 Key Metric

**Override rate over time**, being how often a practitioner overrules the agent, tracked across repeated sessions. A falling override rate is direct evidence of earned trust and is the project's most original measurement.

---

## 19. Timeline

<!-- Table: Data collection timeline -->
| Period | Dates | Activity | Expected output |
|---|---|---|---|
| Week 1 | 16 to 20 September 2026 | Finalise this plan, the interview guide, the data request template and the consent statement. Send first outreach letters to three organisations. | Instruments ready, outreach begun |
| Week 2 | 21 to 27 September 2026 | Physical visits and follow-up. Pilot the questionnaire with 5 respondents. | First interviews secured |
| Week 3 | 28 September to 4 October 2026 | Conduct first interviews. Distribute the questionnaire. | Initial qualitative findings |
| Week 4 | 5 to 11 October 2026 | Continue interviews. Submit formal data requests to willing organisations. | Requirements taking shape |
| Week 5 | 12 to 18 October 2026 | Receive and clean operational data. Escalate to the fallback in section 9.4 if nothing has arrived. | Cleaned dataset or documented fallback |
| Week 6 | 19 to 25 October 2026 | Estimate demand distributions, lead time distributions and cost parameters. | Calibrated model inputs |
| Week 7 | 26 October to 1 November 2026 | Build the synthetic generator seeded from the real sample. Run back-comparison against historical decisions. | Headline result |
| Week 8 | 2 to 8 November 2026 | Analyse, document limitations, complete the report. | Final deliverable |

**Decision point at the end of Week 5.** If no organisation has supplied operational data by 18 October 2026, invoke section 9.4 rather than continuing to wait. This date exists so that the fallback is a planned decision and not a late scramble.

---

## 20. Responsibilities

<!-- Table: Allocation of data responsibilities -->
| Member | Primary responsibility | Shared responsibility |
|---|---|---|
| Dev Johnson | Organisation outreach, visits and relationship management, given existing contacts in the sector | Interview participation, contact log upkeep |
| Jonathan Katongole | Data request design, intake, cleaning and the data dictionary | Modelling and back-comparison analysis |
| Bridget Bataringaya | Alternative and fallback sources, questionnaire distribution and analysis | Interview notes and thematic coding |
| Isaac Mwesigwa | Consent, confidentiality undertakings, documentation and the outreach log | Synthetic data scenarios, report assembly |

All four members must understand the full data lifecycle and the confidentiality rules. Any decision that changes a real data value is reviewed by a second member.

---

## 21. Final Recommended Data Strategy

Use practitioners to establish how the decision is really made, a small volume of real operational history to calibrate the model, synthetic data seeded from that history to provide volume and edge cases, and practitioners again to evaluate whether they would delegate the decision.

<!-- Table: Summary of the recommended data strategy -->
| Stage | Target | Main result |
|---|---|---|
| Problem understanding | 6 organisations, 15 interviews | Evidence of how commitment decisions fail, and what trust would require |
| Real operational history | 3 organisations, 3 to 5 years per title | Demand distributions, lead time distributions, cost structure |
| Development data | 500 to 2,000 synthetic titles | Controlled scenarios and edge cases |
| Evaluation | 8 to 15 practitioners | Usability, explainability, and the override rate |

> **Sequence:** Outreach → Interviews → Operational data request → Cleaning and calibration → Synthetic generation → Model development and back-comparison → Prototype evaluation → Final analysis.

---

## Appendix A: Print Run History CSV Template

<!-- Table: Print run history CSV template with worked example rows -->
| run_id | title_id | decision_date | quantity_committed | unit_production_cost | printer_id | delivery_promised | delivery_actual | period | units_sold | unit_selling_price | units_written_off | salvage_value_per_unit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R0451 | T001 | 2025-06-14 | 10000 | 8500.00 | P003 | 2025-07-20 | 2025-08-02 | 2025-T3 | 8750 | 25000.00 | 300 | 500.00 |
| R0452 | T002 | 2025-06-14 | 6000 | 7200.00 | P003 | 2025-07-20 | 2025-08-02 | 2025-T3 | 6000 | 22000.00 | 0 | 500.00 |
| R0453 | T001 | 2026-01-10 | 9000 | 8900.00 | P001 | 2026-02-15 | 2026-02-14 | 2026-T1 | 7100 | 26000.00 | 1200 | 500.00 |

---

## Appendix B: Minimum Data Collection Checklist

- [ ] Supervisor has reviewed this plan and the instruments
- [ ] Introductory letter prepared on university letterhead
- [ ] Confidentiality undertaking drafted and signed by all four members
- [ ] Minimum three organisations approached, with the contact log started
- [ ] Interview guide piloted with at least one practitioner
- [ ] Consent statement read to every participant before the interview begins
- [ ] Recording permission handled explicitly and separately
- [ ] Excel data request template prepared and kept to one page
- [ ] Anonymous organisation and title identifiers assigned
- [ ] Restricted storage location created for raw commercial data
- [ ] `.gitignore` excludes raw data and credentials, in place before any data arrives
- [ ] Data dictionary written
- [ ] Cleaning rules documented, including the edition-break rule
- [ ] Chronological, leakage-free split strategy defined
- [ ] Synthetic scenarios documented with their seed parameters
- [ ] Week 5 fallback decision point diarised for 18 October 2026
- [ ] No credentials, customer personal data or third-party contract terms requested
