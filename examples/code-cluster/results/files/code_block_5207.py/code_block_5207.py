# chart for number of account created
train['date_account_created_new'] = pd.to_datetime(train['date_account_created'])
sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(10, 8)
train.date_account_created_new.value_counts().plot(kind='line', linewidth=1, color='#1F618D')
plt.xlabel('Date ', size=20)
plt.ylabel('Number of account created ', size=15)
plt.tick_params(labelsize=12)
#sns.despine()