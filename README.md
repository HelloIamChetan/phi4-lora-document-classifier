# Fine-tuning Phi-4 Mini with LoRA for document classification

This project demonstrates an end-to-end fine-tuning workflow for classifying mixed personal and work documents. A LoRA adapter was trained on Microsoft Phi-4 Mini Instruct to return a document category and a 1–5 long-term retention score.

The public repository contains sanitized code, fictional examples, aggregate metrics, and deployment documentation. It intentionally excludes source documents, extracted text, real paths, labels tied to individual files, and model weights.

## Outcome

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

These results support a human review workflow, not automatic file deletion or irreversible organization.

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

The original dataset contains sensitive document classes, including finance, medical, identity, immigration, and legal material. Those files, their contents, and their paths are deliberately absent from this repository. The classifier should suggest labels for a person to review; it must not delete, move, or overwrite documents.

## License

The repository code and documentation are released under the [MIT License](LICENSE). Microsoft Phi-4 Mini Instruct has its own model license and terms.
