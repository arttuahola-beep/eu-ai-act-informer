---
date: 2026-11-10
lens: Financial institutions
headline: If your bank builds its own credit-scoring AI, the system must keep its own logs
source: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
---

If your bank builds its own credit-scoring AI, the system must record its own events automatically. This is Article 12 of the EU AI Act. It is a design duty. The logging has to be built into the system, not added later.

**Why it applies.** Credit scoring of natural persons is high-risk under Annex III point 5(b). A bank that puts its own model into service under its own name is the provider (Art. 3(3)). Providers must make sure the system meets the high-risk requirements, including Article 12 (Art. 16(a)).

**What the logs are for.** Article 12(1) says the system must technically allow the automatic recording of events over its whole lifetime. Article 12(2) says the logs must help with three things:

- spotting situations where the system may present a risk under Article 79(1), or where it has gone through a substantial modification;
- supporting the provider's post-market monitoring under Article 72;
- supporting the deployer's monitoring of the system under Article 26(5).

**No fixed field list for credit scoring.** The Act's detailed minimum list in Article 12(3) applies only to remote biometric identification. For a credit model, the bank decides what to log. The choice should fit the system's intended purpose.

**How long to keep them.** Under Article 19(1), providers keep the logs that are under their control. The period must fit the intended purpose. The minimum is six months. Other EU or national law can set a different rule, especially data protection law.

**The bank shortcut.** Article 19(2) helps financial institutions. A bank that is subject to internal-governance rules under EU financial services law keeps these logs as part of the documentation it already keeps under that law. It does not need a separate archive. A bank that only uses a vendor's system is a deployer. Its log duty sits in Article 26(6), which has a similar shortcut.

**Timing.** After the Digital Omnibus (Regulation (EU) 2026/1744), these duties apply to Annex III systems from 2 December 2027.

**What to do now.** Decide which events the model should record. One sensible starting set is the inputs used, the score, the model version, the time, and any human override. Link the logs to your existing record-keeping. Then check the retention period against the GDPR storage-limitation principle (GDPR Art. 5(1)(e)).

Sources: Regulation (EU) 2024/1689, Articles 3(3), 12, 16(a), 19 and 26(6), and Annex III point 5(b); Regulation (EU) 2026/1744 (Digital Omnibus) for the timeline.
