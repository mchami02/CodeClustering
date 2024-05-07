plt.figure('Wind by month')
sns.boxplot(x='month', y='windspeed', data=df)
plt.title('Windspeed by Month', fontsize=20)
plt.show()