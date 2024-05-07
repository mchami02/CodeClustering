print(train['Label'].value_counts())

rcParams['figure.figsize'] = 10,5
sb.barplot(x = train['Label'].value_counts().index, y = train['Label'].value_counts().values)
plt.title('Label counts')
plt.show()