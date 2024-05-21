import requests
import pandas as pd
import os

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
headers = {"Authorization": "Bearer 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"}


def query(codes):
    message = ""
    # model_setup = "The following are your instructions on how to answer me : \n"
    # model_setup = "System : You are an assistant that summarizes code blocks. Your task is to explain the code blocks provided to you. Anwser concisely in less than 50 words. For example, for some cluster you would write : Transforms the data using a specific scaler and then trains it and tests it.\n"
    
    # model_setup += "\n\n"
    # model_setup = "What do the code snippets in the cluster do? Answer me in less than 50 words \n"
    code_snippets = "I am going to give you a cluster of multiple code blocks. Your task is to analyze these code blocks and summarize what they are collectively about and why they are grouped together. Specifically, identify the common functionality, purpose, or theme that unites these code blocks. Provide a concise explanation that captures the essence of the cluster. \n"
    for i, c in enumerate(codes):
        code_snippets += f"Code block {i} : \n"
        code_snippets += c
        code_snippets += "\n"

    # message += model_setup
    message += code_snippets
    message += "\n\n"
    response = requests.post(API_URL, headers=headers, json={"inputs" : message})
    return response.json()


current_file = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(current_file, "public/code_clusters_9999.csv")
code_clusters = pd.read_csv(data_file)


# Group the code blocks by cluster
grouped_clusters = code_clusters.groupby("Cluster")

i = 1
# Iterate through each cluster
for cluster, group in grouped_clusters:
    # Select at most 10 code blocks from the cluster
    code_blocks = group["Code_Block"].head(10).tolist()
    # Generate the summary using the code_summary string
    summary = query(code_blocks)
    
    # Do something with the summary
    print("*"*50)
    print(f"Cluster {i} ({len(code_blocks)} snippets):")

    # print("Code blocks:")
    # for e, c in enumerate(code_blocks):
    #     print(f"Code {e}\n")
    #     print(c)

    print("Summary:")
    print(summary[0]['generated_text'].split('\n')[-5:])
    i += 1
    # if i > 6 : break
    

