#Plotting distribution of the data

for x in cat:
    sns.countplot(x=x, data=df,palette='RdBu')
    plt.ylabel('Number of users')
    plt.title('Users '+ x + ' Distribution')
    plt.xticks(rotation='vertical')
    plt.show()
    plt.savefig('plot'+str(x)+'.png')
    