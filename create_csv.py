import pandas as pd
import numpy as np


def main():
    np.random.seed(42)
    data = {
        "CodeID": [f"Code_{i}" for i in np.random.randint(100, 200, size=10)],
        "IT": np.random.randint(1, 11, size=10),  # 10 random types between 1 and 10
        "Distance": np.random.uniform(0, 10, size=10)
    }
    df = pd.DataFrame(data)
    print(df)
    df.to_csv("clustering_data.csv", index=False)

    # implementation_types = {
    #     "ImplementationID": np.arange(1, 11),
    #     "ImplementationType": [f"Type_{i}" for i in np.arange(1, 11)]
    # }
    # df = pd.DataFrame(data)
    # df.to_csv("clustering_data.csv", index=False)
    # print(df)
    # print(df_imp)

if __name__ == "__main__":
    main()