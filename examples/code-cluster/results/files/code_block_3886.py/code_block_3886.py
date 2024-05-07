def weekend(df):
    df['weekend'] = np.zeros_like(df['holiday'])
    df['weekend'].loc[(df['workingday'] == 0) & (df['holiday'] == 0)] = 1