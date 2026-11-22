# Compare the base model with the tuned classifier

**Question.** How much does the LoRA adapter improve document categorization and retention scoring over prompted Phi-4 Mini Instruct?

- Run both the pinned base model and the tuned model locally against the same authorized held-out inputs. Keep preprocessing, prompt, taxonomy, decoding, and JSON parsing fixed. Record the exact model revisions and settings.
- Report valid JSON, category accuracy and macro F1, exact retention-score accuracy, and retention scoring within one point. Count invalid outputs explicitly and use the full test set as the denominator for accuracy. Report directional differences and representative error categories.
- If the original 60-document test split is used, treat it as a retrospective comparison. Reserve a new group-separated holdout for any later change informed by those results.
- Report aggregate results and fictional examples. Keep the source documents, labels, extracted text, and model artifacts in the authorized local environment.

The public repository records tuned-model results. Baseline numbers are pending access to the local model and held-out documents.
