plt.figure(figsize=(45,25))
mask = np.triu(np.ones_like(df_train.corr(), dtype=np.bool))
sns.heatmap(df_train.corr(),annot=True, mask=mask)
sns.set(font_scale=1.4)