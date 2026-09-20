# Training report

## Objective

Train a compact adapter for Phi-4 Mini Instruct that reads extracted document text and predicts:

1. One category from a fixed 20-category taxonomy.
2. An importance score from 1 to 5, based on long-term retention value rather than urgency.

## Data preparation

I reviewed a collection of mixed document formats and constructed a 400-document master set. To avoid leakage, related document families were assigned to the same split. Text was extracted and shortened consistently so each prompt fit the LoRA training context budget.

| Split | Documents | Purpose |
| --- | ---: | --- |
| Training | 280 | Learn category and importance patterns |
| Validation | 60 | Track training quality |
| Final test | 60 | One-time held-out measurement |

## Fine-tuning

The training used LoRA, so only 1.442 million parameters were updated rather than the full 3.836 billion parameter model. The adapter trained the final four transformer layers, with rank 8 and alpha 128, over 400 iterations.

## Evaluation

The untouched 60-document final test set produced valid JSON for every response. Category accuracy was 58.3%, macro F1 was 53.2%, exact importance accuracy was 45.0%, and 93.3% of importance predictions were within one point of the reviewed score.

The evaluation demonstrates learned task behavior, but the results are not sufficient for autonomous file management. The intended use is a review queue with human approval.

## Deployment

The LoRA weights were converted to a portable PEFT representation, then safely merged into the pinned Microsoft Phi-4 Mini base revision. All 32 adapter tensors loaded exactly before merging. The resulting standalone Hugging Face model can be loaded locally on Windows without PEFT at inference time.
