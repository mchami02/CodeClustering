plt.figure(figsize=(13,12))

sns.barplot(x=best_month['month'], y=best_month['revenue'])
plt.xticks(rotation=60)