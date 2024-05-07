features = pd.DataFrame()
features["features"] = x.columns
features["coefficient"] = model.feature_importances_

features.sort_values(by=["coefficient"], ascending=False, inplace=True)
fig,ax= plt.subplots()
fig.set_size_inches(20,20)
sns.barplot(data=features, x="coefficient", y="features");