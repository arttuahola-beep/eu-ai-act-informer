---
date: 2026-10-29
lens: Financial institutions
headline: "Bias testing in credit scoring starts with the data, and the AI Act now says when you may use sensitive data to do it"
source: "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"
---

If you build your own credit-scoring model, the AI Act makes data quality a legal duty. It also gives you a narrow legal basis to use sensitive data to find and fix bias.

Credit scoring of natural persons is high-risk under Annex III point 5(b). A bank that develops its own model is its provider. Article 10 then applies to its training, validation and testing data.

What Article 10 asks for:

- Data governance practices fit for the intended purpose (Art. 10(2)). These cover design choices, data origin, preparation steps such as labelling and cleaning, and assumptions about what the data measures.
- An examination for possible biases that could harm fundamental rights or lead to prohibited discrimination (Art. 10(2)(f)).
- Measures to detect, prevent and reduce those biases (Art. 10(2)(g)).
- Data that is relevant, sufficiently representative and, as far as possible, free of errors and complete (Art. 10(3)).
- Data that reflects the setting where the model is used, such as the country or customer segment (Art. 10(4)).

The hard part is testing for bias without the sensitive data. You often cannot check fairness by ethnicity or health without holding that data.

The Digital Omnibus (Regulation (EU) 2026/1744) moved this permission into a new Article 4a. Providers of high-risk systems may exceptionally process special categories of personal data for bias detection and correction. Strict conditions apply. Other data, including synthetic or anonymised data, must not do the job. The data must be pseudonymised and access tightly controlled. It must not be shared with other parties. It must be deleted once the bias is corrected or its retention period ends. Your GDPR records must explain why the processing was strictly necessary.

Article 4a(2) extends the same option to deployers of high-risk systems. That helps a lender that buys a vendor model. It creates no duty to test, though.

Timing: Annex III high-risk duties apply from 2 December 2027 under the Omnibus.

Practical step: map your credit-model datasets against Article 10 now. Document where proxies for protected traits may sit, such as postcode. Decide with your DPO whether Article 4a testing is truly necessary, and write down why.

Source: Regulation (EU) 2024/1689, Articles 10 and 4a and Annex III (consolidated text as of 27 July 2026); Regulation (EU) 2026/1744, Recital 9.

By bot Ursula
