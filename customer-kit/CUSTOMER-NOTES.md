# Our simulated customer agreement

This is fictional customer practice, not a real client interview. One file per
team. Replace Pending only after a real team decision or observed result.

- Team members / shared repository: Anya, Dhruvi, Shree · this repository.
- Selected scenario file and customer: **Agreed** — `scenarios/repair-shop.md`, Maya Chen (Bench & Bolt).
- Current stage / next conversation: Review 1 · Plan done. Next conversation: the one bounded change, after our first slice works.
- Authoritative spec link: [../SPEC.md](../SPEC.md)
- Protected finishing week starts: Pending; check the section schedule.

## Discovery and scope

- Customer need / intended user: the shop coordinator needs one queue with an honest status for each repair inquiry.
- Two scope options compared: A · Staff intake vs B · Rider intake — comparison table in [SPEC §1](../SPEC.md#1--agile-work-plan).
- Selected option: **Agreed** — A · Staff intake. B (rider form) is deferred.
- Why we chose Bench & Bolt and Option A (team's words): This is a realistic problem for many businesses, especially when they're just starting out. Staff intake gives us a practical way to help a shop track its orders.
- Agreed user stories (**Agreed**; one user — the coordinator; acceptance checks in [SPEC §1 Backlog](../SPEC.md#backlog)):
  - **S1 · Intake** — As the coordinator, I want to create a repair inquiry so I can track upcoming work.
  - **S2 · Queue** — As the coordinator, I want to see saved inquiries so the shop can work on them.
  - **S3 · Decision** — As the coordinator, I want to accept, decline and close (complete) a request so its status stays honest.
  - **S4 · Completed** — As the coordinator, I want to see how many inquiries we've completed so I can measure the shop's output.
- Status names, allowed transitions and what each status promises: from scenario — Pending review → Accepted/Declined; Accepted → Completed; Completed and Declined terminal. Accepted ≠ appointment or charge.
- Deferred features / synthetic-data boundary: rider form, extra roles (owner/repairman views), hosting/auth, booking, payment, quotes, inventory, messages, customer contact details. Synthetic rider labels only.
- Assumptions explicitly agreed, with who agreed: all stories use one role (the coordinator) — agreed by Anya, Dhruvi, Shree. "Track completed" means a count/filter of Completed inquiries, not customer records — agreed by Anya, Dhruvi, Shree.
- Open questions: edit inquiry text after creation? queue sort order? Technical details not yet discussed (Pending).
- Design/development/QA owners and cross-reviewers: Anya — intake form; Dhruvi — SQLite storage; Shree — coordinator queue. Full table and reviewers: [SPEC §1 Team table](../SPEC.md#team-ownership-and-cross-review).

## Change request: Not introduced

- First working slice and actual check links: Not yet evidenced.
- Change introduced / team impact estimate: Pending.
- Implement / defer decision and reason: Pending.
- Customer's simulated scope agreement: Pending.
- Actual implementation / check evidence: Not yet evidenced.

## Final acceptance: Pending

- Chosen revision / reproducible setup: Pending.
- Happy path, rejected action and restart evidence: Not yet evidenced.
- Simulated customer's acceptance / remaining gaps: Pending.
- Real peer issue, meaningful change and retest: Not yet evidenced; AI is not a peer.
- Each member's actual contribution and AI/starter help: Pending.

Keep proposed, agreed, implemented and checked distinct. A recorded agreement
is not a passing test. A passing test is not evidence of a real human review.
