df_gender_age_train.groupby('group').device_id.size().sort_index(ascending=False).plot.barh(title='Age Gender Group Distribution')
sns.despine()