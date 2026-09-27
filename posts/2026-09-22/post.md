---
date: 2026-09-22
lens: Financial institutions
headline: Credit scoring is high-risk AI
source: ""
---

Under Annex III point 5(b) of the EU AI Act, AI used to evaluate a natural person’s creditworthiness or to set their credit score is high-risk. That catches personal loans, mortgages, credit-card limits, and buy-now-pay-later approvals — not only a classic bureau score.

There is one clear carve-out: AI used for detecting financial fraud. In practice, banks often blend scoring, fraud checks, and bureau data in one pipeline. If the system’s purpose includes creditworthiness, the high-risk label usually applies end to end — the fraud exception does not save a combined decisioning stack.

If you buy or license a third-party scoring model, you remain the deployer for the credit decision. That brings deployer duties (human oversight, logging, instructions for use) and, for this use case, a fundamental-rights impact assessment before putting the system into use.

Practical move: inventory every model that touches credit decisions, separate pure fraud tools from scoring where you can, and label who is the provider vs deployer for each.
