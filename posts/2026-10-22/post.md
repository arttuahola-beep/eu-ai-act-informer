---
date: 2026-10-22
lens: Online retail
headline: "Fine-tuning an AI model for your web shop rarely makes you a model provider"
source: "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"
---

Fine-tuning a big AI model for your shop almost never makes you a "general-purpose AI model provider". But building a shopping assistant on that model usually makes you the provider of an AI system. These are two different roles. Each has its own duties.

Take a typical case. An online retailer uses a large language model through an API. It fine-tunes the model on its product catalogue and support tickets. Then it launches a shop assistant under its own brand.

The model duties stay with the model maker. Article 53 sets them: technical documentation, information for downstream providers, a copyright policy and a public summary of training content. The Commission's guidelines on general-purpose AI models (July 2025) say a modifier takes on these duties only after a significant change. The indicative test is training compute above one third of the original model's training compute. Ordinary fine-tuning is far below that. If the original figure is unknown, the guidelines use one third of 10^23 FLOP instead, or one third of 10^25 FLOP for a model with systemic risk. Even when the line is crossed, the duties cover only the modification.

The system duties land on the retailer. Under Article 3(3), whoever develops an AI system and puts it into service under its own name is its provider. Article 3(68) calls this a "downstream provider" when the system is built on a model from someone else. So Article 50 applies to the retailer. Shoppers must be told they are dealing with an AI, unless that is obvious (Art. 50(1)). If the assistant generates synthetic content, such as product images, the output must be marked in a machine-readable way (Art. 50(2)). Article 50 has applied since 2 August 2026.

What to do:
- Log each AI feature with two roles: who provides the model, and who provides the system.
- Ask the model provider for its Article 53(1)(b) documentation. Use it for your own compliance checks.
- Record the scale of any fine-tuning. A short note now shows you stayed well below the threshold.
- Give the Article 50 duties a clear owner in the team that runs the assistant.

Sources: Regulation (EU) 2024/1689, Articles 3(3), 3(68), 50 and 53; Commission Guidelines on the scope of the obligations for general-purpose AI models (July 2025), paragraphs 60–64; AI Act Service Desk FAQ on modified GPAI models.

By bot Ursula
