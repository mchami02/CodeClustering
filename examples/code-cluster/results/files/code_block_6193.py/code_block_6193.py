average_assortment = df_stores_new.groupby('Assortment')['Sales', 'Customers'].mean()

fig, (axis1,axis2) = plt.subplots(1,2,figsize=(15,4))
sns.barplot(average_assortment.index, average_assortment['Sales'], ax=axis1)
sns.barplot(average_assortment.index, average_assortment['Customers'], ax=axis2)