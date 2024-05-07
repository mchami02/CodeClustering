plt.figure(figsize=(8,6))
sns.distplot(df_train1['Horizontal_Distance_To_Hydrology'], fit = stats.norm)
fig = plt.figure(figsize=(8,6))
res = stats.probplot(df_train1['Horizontal_Distance_To_Hydrology'], plot=plt)