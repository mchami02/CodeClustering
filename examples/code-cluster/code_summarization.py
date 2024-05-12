from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    AutoConfig,
    pipeline,
)

model_name = "sagard21/python-code-explainer"

tokenizer = AutoTokenizer.from_pretrained(model_name, padding=True)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

config = AutoConfig.from_pretrained(model_name)

model.eval()

pipe = pipeline("summarization", model=model_name, config=config, tokenizer=tokenizer)

raw_code = """
def preprocess(text: str) -> str:
    text = str(text) text = text.replace("\n", " ")
    tokenized_text = text.split(" ") preprocessed_text = " ".join([token for token in tokenized_text if token])
    return preprocessed_text
"""

print(pipe(raw_code)[0]["summary_text"])