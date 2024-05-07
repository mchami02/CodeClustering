fig = plt.figure(figsize=(7, 4))
sns.barplot(x = df_gender_age_train.gender.value_counts().index, y=df_gender_age_train.gender.value_counts().values, ax=fig.gca())
sns.despine()
plt.title('Gender distribution')