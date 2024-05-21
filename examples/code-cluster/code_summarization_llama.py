import transformers
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

access_token = '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'
model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    token=access_token
)
pipeline = transformers.pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto", token=access_token)
pipeline("Hey how are you doing today?")