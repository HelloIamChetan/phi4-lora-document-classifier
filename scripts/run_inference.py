"""Classify a UTF-8 document-text file with an authorized local merged model."""
import argparse
import json
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


ROOT = Path(__file__).resolve().parents[1]
PROMPT = (ROOT / "prompts" / "classification-system-prompt.txt").read_text()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("document", type=Path, help="UTF-8 extracted text")
    parser.add_argument("--model", required=True, type=Path, help="Local merged Phi-4 Mini folder")
    args = parser.parse_args()

    text = args.document.read_text(errors="replace")[:7000]
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model, trust_remote_code=True, local_files_only=True, torch_dtype=dtype
    ).to(device).eval()
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": json.dumps({"document_text": text})},
    ]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.inference_mode():
        generated = model.generate(**inputs, max_new_tokens=100, do_sample=False, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(generated[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True).strip()
    print(response)


if __name__ == "__main__":
    main()
