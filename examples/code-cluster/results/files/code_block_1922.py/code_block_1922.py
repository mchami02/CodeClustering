df_train['Year'] = df_train['Date'].apply(lambda x: int(x[0:4]))
df_train['Month'] = df_train['Date'].apply(lambda x: int(x[5:7]))
df_train['Day'] = df_train['Date'].apply(lambda x: int(x[8:10]))
df_test['Year'] = df_test['Date'].apply(lambda x: int(x[0:4]))
df_test['Month'] = df_test['Date'].apply(lambda x: int(x[5:7]))
df_test['Day'] = df_test['Date'].apply(lambda x: int(x[8:10]))