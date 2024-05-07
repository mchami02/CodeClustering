train = train.rename(columns={"A-coref": "A", "B-coref": "B"})
train["A"] = train["A"].astype(int)
train["B"] = train["B"].astype(int)
train["NEITHER"] = 1.0 - (train["A"] + train["B"])