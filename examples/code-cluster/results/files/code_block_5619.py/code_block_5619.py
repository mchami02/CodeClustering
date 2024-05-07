keys['date'] = keys['Page'].apply(lambda x: x.split('_')[-1])
keys['Page'] = keys['Page'].apply(lambda x: '_'.join(x.split('_')[:-1]))
keys['date'] = pd.to_datetime(keys['date'], format='%Y-%m-%d')