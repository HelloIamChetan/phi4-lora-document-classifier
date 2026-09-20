# Model card: Phi-4 Mini LoRA document classifier

## Intended use

Classify extracted document text into a fixed category and suggest an importance score for human review. The model is designed for local, privacy-conscious document triage.

## Output taxonomy

The supported categories are AI & Software, AI Skills & Markdowns, Education, Employment & Career, Family & Civil Records, Finance, Health & Medical, ID Cards, Immigration & Travel, Insurance, Legal & Property, Music & Hobbies, Passport, Personal Planning, Photos & Signatures, Reference & Manuals, System & Temporary, Vehicle Records, Work & Projects, and Writing.

Importance ranges from 1 for transient or replaceable content to 5 for essential identity, ownership, immigration, passport, or legal records.

## Limitations

- Evaluation covers 60 held-out documents and is not a guarantee of accuracy for new collections.
- OCR and text-extraction quality directly affect predictions.
- Category and importance predictions can be wrong, especially for rare classes or ambiguous documents.
- The model should never be the sole basis for deleting, moving, sharing, or retaining sensitive files.
- Duplicate detection is a separate task and should not be inferred from one document in isolation.

## Privacy

The public project contains no original training documents, extracted text, file paths, or model weights.
