categoryweather=df.groupby("holiday").nunique()
print(categoryweather)
df1=pd.get_dummies(df['weather'])
df1.head()'