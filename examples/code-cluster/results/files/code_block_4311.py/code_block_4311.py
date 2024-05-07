from sklearn.preprocessing import MinMaxScaler

def normalize_cols(df: DataFrame, scaler) -> DataFrame:
    df = df.copy()
    return DataFrame(scaler.fit_transform(df.values), columns=df.columns, index=df.index)

x_scaler = MinMaxScaler()
x = train_data.drop(TARGET_NAME, axis=1)
x = normalize_cols(df=x, scaler=x_scaler)

y_scaler = MinMaxScaler()
y = train_data[[TARGET_NAME]]
y = normalize_cols(df=y, scaler=y_scaler)

test_data =  normalize_cols(df=test_data, scaler=x_scaler)