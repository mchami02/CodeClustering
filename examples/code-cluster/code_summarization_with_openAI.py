import os
from openai import OpenAI
import pandas as pd

# Set your OpenAI API key
client = OpenAI()

def generate_summary(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a developer tasked with understanding and summarizing code. Generate a concise summary that captures the core functionality and common patterns across the given code cluster. Separate each sentence by a newline",
            },
            {
                "role": "user",
                "content": f"Here are summaries of some pieces of code that have been analyzed and clustered based on their similar functionalities. Please provide a comprehensive summary that encapsulates the shared features and primary purpose of this code cluster: {text}",
            },
        ],
        max_tokens=100,
    )
    return response.choices[0].message.content



# Read the code clusters from the CSV file
code_clusters = pd.read_csv("examples/code-cluster/public/code_clusters_9999.csv")

# Group the code blocks by cluster
grouped_clusters = code_clusters.groupby("Cluster")

i = 1
summaries = []

# Iterate through each cluster
for cluster, group in grouped_clusters:
    # Select at most 10 code blocks from the cluster
    code_blocks = group["Code_Block"].head(10).tolist()
    
    # Aggregate the code blocks into a single string
    code_summary = "Code Summary:\n" + "\n".join(code_blocks)
    print("*" * 50)
    print(code_summary)
    print("*" * 50)
    # Generate the summary using the code_summary string
    summary = generate_summary(code_summary)
    
    # Store the summary in a list to update the DataFrame later
    summaries.extend([(index, summary) for index in group.index])

    # Do something with the summary
    # print("*" * 50)
    # print(f"Cluster {i}:")
    # print(summary)
    i += 1

# Update the DataFrame with the generated summaries
for index, summary in summaries:
    code_clusters.at[index, "Summary"] = summary

# Save the modified DataFrame back to the CSV file
code_clusters.to_csv("examples/code-cluster/public/code_clusters_9999.csv", index=False)
