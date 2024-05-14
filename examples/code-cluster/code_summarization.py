from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    AutoModelWithLMHead,
    SummarizationPipeline,
    AutoConfig,
    pipeline,
)


# pipeline = SummarizationPipeline(
#     model=AutoModelWithLMHead.from_pretrained("SEBIS/code_trans_t5_large_source_code_summarization_python_multitask_finetune"),
#     tokenizer=AutoTokenizer.from_pretrained("SEBIS/code_trans_t5_large_source_code_summarization_python_multitask_finetune", skip_special_tokens=True),
#     device=0
# )

# tokenized_code = '''with open ( CODE_STRING , CODE_STRING ) as in_file : buf = in_file . readlines ( )  with open ( CODE_STRING , CODE_STRING ) as out_file : for line in buf :          if line ==   " ; Include this text   " :              line = line +   " Include below  "          out_file . write ( line ) '''
# r = pipeline([tokenized_code])
# print(r)

model_name = "sagard21/python-code-explainer"

tokenizer = AutoTokenizer.from_pretrained(model_name, padding=True)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

config = AutoConfig.from_pretrained(model_name)

model.eval()

pipe = pipeline("summarization", model=model_name, config=config, tokenizer=tokenizer)

raw_code = """#Regression on everything
from sklearn.ensemble import RandomForestRegressor
import seaborn as sns
import numpy

sns.set_context(""notebook"", font_scale=1.11)
sns.set_style(""ticks"")

yTrain = Train_data['revenue'].apply(numpy.log)
Train_data = Train_data.drop([""revenue""],1)
xTrain = pd.DataFrame(Train_data)
xTest = pd.DataFrame(Test_data)
'"""

code_summary = pipe(raw_code,max_length=100)[0]["summary_text"]

print("Code Summary:")
print(code_summary)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
final_summary = summarizer(code_summary, max_length=400, min_length=5, do_sample=False)[0]["summary_text"]

print("Final Summary:")
print(final_summary)