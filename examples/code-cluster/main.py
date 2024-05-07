import subprocess
import zipfile
import json
import pandas as pd

def cluster_code():
    jplag_path = 'C:/Users/rasan/Documents/Rasan/Zürich/ETHZ/MA2/AI_Center_Project/JPlag/cli/target/jplag-5.0.0-jar-with-dependencies.jar'
    bandwidth = 20
    max_runs = 100
    results_path = 'C:/Users/rasan/Documents/Rasan/Zürich/ETHZ/MA2/AI_Center_Project/JPlag/cli/target/results'
    code_files_path = 'C:/Users/rasan/Documents/Rasan/Zürich/ETHZ/MA2/AI_Center_Project/JPlag/cli/target/mini_data'
    command = f"java -jar {jplag_path} -l python3 -n=9999 --cluster-alg SPECTRAL --cluster-spectral-bandwidth={bandwidth} --cluster-spectral-max-runs={max_runs} -r {results_path} {code_files_path}"
    subprocess.call(command, shell=True)
    return results_path

def extract_zip(path, out_path):
    with zipfile.ZipFile(f"{path}.zip", 'r') as zip_ref:
        zip_ref.extractall(out_path)
        
def get_data(files_path):
    with open(f"{files_path}/overview.json", 'r') as file:
        data = json.load(file)
    return data

def code_block_similarity(block1, block2, data):
    return [obj for obj in data["top_comparisons"] if (obj["first_submission"] == block1 or obj["first_submission"] == block2) and (obj["second_submission"] == block1 or obj["second_submission"] == block2)]
        
def save_to_csv(files_path, clusters):
    code_blocks = []
    cluster_labels = []

    for i, cluster in enumerate(clusters):
        for block in cluster["members"]:
            with open(f"{files_path}/files/{block}/{block}", 'r') as file:
                content = file.read()

            code_blocks.append(content)
            cluster_labels.append(i)

    df = pd.DataFrame({'Code_Block': code_blocks, 'Cluster': cluster_labels})
    csv_path = 'code_clusters.csv'
    df.to_csv(csv_path, index=False)
    return csv_path
    
if __name__ == "__main__":
    
    # results_path = cluster_code()
    files_path = "results"
    # extract_zip(results_path, files_path)

        
    print("\n-------------------------------------\n")
    data = get_data(files_path)
    clusters = data["clusters"]
    print(f"Num clusters: {len(clusters)}")
    
    csv_path = save_to_csv(files_path, clusters)