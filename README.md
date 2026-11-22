# Local document classification with Phi-4 Mini and LoRA

## Problem

People sorting mixed personal documents need a way to prioritize what to review and retain without sending their files to a remote service.

## Decision

Fine-tune a local model to suggest one category and a 1–5 retention score. Route suggestions to a review queue so a person can confirm or correct the proposed metadata.

## Proof

The tuned model reached **58.3% category accuracy on 60 held-out documents**. That result supports using the model to suggest labels for review. **[See an illustrative review queue entry](REVIEW-EXAMPLE.md)** or read the [training report](docs/training-report.md).

## Next

Run a [same-test-set comparison](docs/evaluation-plan.md) against the prompted base model to measure the contribution of the LoRA adapter.

## Held-out results

The model returns structured JSON such as:

```json
{"category":"Finance","importance":4}
```

| Final held-out test measure | Result |
| --- | ---: |
| Documents | 60 |
| Valid JSON responses | 60 / 60 |
| Category accuracy | 58.3% |
| Category macro F1 | 53.2% |
| Exact importance accuracy | 45.0% |
| Importance within one point | 93.3% |

## What I built

- A reviewed, 400-document master dataset.
- A 20-category taxonomy and a documented importance scale.
- Group-aware splits so related records did not leak between training and testing.
- A 280 / 60 / 60 training, validation, and final-test split.
- LoRA fine-tuning, evaluation, adapter conversion, and a safely merged standalone model.
- A Windows deployment plan that extracts text from documents and produces Excel/CSV review reports.

## Model and training

| Setting | Value |
| --- | --- |
| Base model | `microsoft/Phi-4-mini-instruct` |
| Method | LoRA supervised fine-tuning |
| LoRA rank | 8 |
| LoRA alpha | 128 |
| Trained layers | Final four transformer layers |
| Trainable parameters | 1.442M / 3.836B (0.038%) |
| Training iterations | 400 |

See [the model card](docs/model-card.md) and [the training report](docs/training-report.md) for the methodology and limitations.

## Run the sanitized example

This repository does not include weights. After obtaining an authorized local copy of the merged model, install dependencies:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts\run_inference.py examples\fictional-insurance-policy.txt --model D:\LoRA\Windows_Phi4_Mini_Document_Classifier\model
```

The model is local-only. The inference script receives plain extracted text; a complete application should extract text and OCR from PDFs, office documents, spreadsheets, and images before inference.

## Repository layout

```text
docs/       Training report and model card
examples/   Fictional, non-personal documents
prompts/    Classification system prompt
results/    Aggregate held-out test metrics
scripts/    Local inference example
```

## Privacy and safety

The public repository contains sanitized code, fictional examples, aggregate metrics, and deployment documentation. Source documents, extracted text, real paths, per-file labels, and model weights stay in the authorized local environment. The classifier should suggest labels for a person to review; it must not delete, move, or overwrite documents.

## License

The repository code and documentation are released under the [MIT License](LICENSE). Microsoft Phi-4 Mini Instruct has its own model license and terms.
