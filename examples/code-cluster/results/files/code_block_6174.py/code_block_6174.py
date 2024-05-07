df_train['Year'] = df_train['Date'].apply(lambda x: int(x[:4]))
df_train['Month'] = df_train['Date'].apply(lambda x: int(x[5:7]))
df_train['Day'] = df_train['Date'].apply(lambda x: int(x[8:]))