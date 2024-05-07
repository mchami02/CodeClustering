df = pd.read_json('../input/train.json')
df_test = pd.read_json('../input/test.json')
df['created'] = pd.to_datetime(df.created)
df_test['created'] = pd.to_datetime(df_test.created)