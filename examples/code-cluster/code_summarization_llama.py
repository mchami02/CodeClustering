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

messages = [
    {"role": "system", "content": "You are an advanced AI tasked with summarizing code clusters. Each summary should be concise, direct, and formatted as one sentence per point, focusing on core functionalities and common patterns."},
    {"role": "user", "content": "Here are summaries of 10 code segments that have been clustered by their similarities. Please provide a summary that captures the shared features and primary purpose of this cluster in a series of short, distinct sentences."},
]

prompt = pipeline.tokenizer.apply_chat_template(
        messages, 
        tokenize=False, 
        add_generation_prompt=True
)

terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = pipeline(
    prompt,
    max_new_tokens=256,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)

print(outputs[0]["generated_text"][len(prompt):])

pipeline = transformers.pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto", token=access_token)
pipeline("Hey how are you doing today?")
