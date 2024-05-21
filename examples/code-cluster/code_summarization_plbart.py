from transformers import PLBartForConditionalGeneration, PLBartTokenizer

# Read the code clusters from the CSV file
code_clusters = pd.read_csv("examples/code-cluster/public/code_clusters_9999.csv")


# Group the code blocks by cluster
grouped_clusters = code_clusters.groupby("Cluster")

i = 1
# Iterate through each cluster
for cluster, group in grouped_clusters:
    # Select at most 10 code blocks from the cluster
    code_blocks = group["Code_Block"].head(10).tolist()
    
    # Aggregate the code blocks into a single string
    code_summary = "Code Summary i " + "\n".join(code_blocks)
    
    # Generate the summary using the code_summary string
    summary = generate_summary(code_summary)
    
    # Do something with the summary
    print("*"*50)
    print(f"Cluster {i}:")
    print(summary)
    i += 1


tokenizer = PLBartTokenizer.from_pretrained("uclanlp/plbart-python-en_XX", src_lang="python", tgt_lang="en_XX")
example_python_phrase = "def maximum(a,b,c):NEW_LINE_INDENTreturn max([a,b,c])"
inputs = tokenizer(example_python_phrase, return_tensors="pt")
model = PLBartForConditionalGeneration.from_pretrained("uclanlp/plbart-python-en_XX")
translated_tokens = model.generate(**inputs, decoder_start_token_id=tokenizer.lang_code_to_id["__en_XX__"])
summary = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]

print(summary)