# Hillshade_Noon
fig = plt.figure(figsize=(8,6))
sns.distplot(df_train1['Hillshade_Noon'],fit=stats.norm)
fig = plt.figure(figsize=(8,6))
res = stats.probplot(df_train1['Hillshade_Noon'],plot=plt)