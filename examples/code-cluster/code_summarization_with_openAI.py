import os
from openai import OpenAI
import pandas as pd

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-proj-AJdqWWBZ7DD5vgLP4Lr6T3BlbkFJeZPIlHLQKqoPCNilZdGA"

client = OpenAI()

def generate_summary(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a developer who wants to understand the code implementation.",
            },
            {
                "role": "user",
                "content": f"I'll give you 10 summary of code implemetation that have been clustered together. Do a summarization of the code cluster. {text}",
            },
        ],
        max_tokens=200,
    )
    return response.choices[0].message.content


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