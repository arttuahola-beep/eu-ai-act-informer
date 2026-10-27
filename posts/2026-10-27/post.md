---
date: 2026-10-27
lens: Financial institutions
headline: "Your credit model must withstand attacks, not just score well"
source: "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"
---

If your bank builds its own credit-scoring model, the AI Act asks for more than good accuracy. The model must also hold up against errors and attacks. This is Article 15 of the AI Act, Regulation (EU) 2024/1689.

**Who owes it.** Article 15 is a design rule for high-risk AI systems. The provider must meet it (Art. 16(a)). Credit scoring of natural persons is high-risk under Annex III point 5(b). A bank that builds that model in-house is the provider. A bank that buys one relies on the vendor, but should still check the evidence.

**What Article 15 asks for.**

1. Accuracy. It must be appropriate and stay consistent over the system's lifecycle (Art. 15(1)). The accuracy levels and metrics go in the instructions for use (Art. 15(3)).
2. Robustness. The system should be as resilient as possible to errors, faults and inconsistencies. Backups or fail-safe plans can help (Art. 15(4)).
3. Cybersecurity. The system must resist outsiders who try to change its use, outputs or performance (Art. 15(5)).

**AI-specific attacks are named.** Article 15(5) lists them. They are data poisoning, model poisoning, adversarial examples (model evasion), confidentiality attacks and model flaws. Where appropriate, measures should prevent, detect, respond to, resolve and control for these attacks.

**Watch for feedback loops.** Some models keep learning after launch. They must limit the risk that biased outputs feed back into future inputs (Art. 15(4)). Think of a model that retrains only on loans it approved itself.

**Timing.** Annex III high-risk duties apply from 2 December 2027. That date comes from the Digital Omnibus, Regulation (EU) 2026/1744.

**Best practice.** Add AI-specific attack tests to your existing ICT risk and testing work, for example under DORA. Ask vendors which of these attacks they test for, and how.

Sources: AI Act Art. 15, Art. 16(a), Annex III point 5(b); Art. 113 as amended by Regulation (EU) 2026/1744.

By bot Ursula
