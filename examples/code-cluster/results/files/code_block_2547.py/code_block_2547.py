store['Promo2SinceYear'].mode()
data_merged=data.merge(store,on='Store',how='left')
print(data.shape)
print(data_merged.shape)
#just have a  look over the missing value after merging the data over store data/sometimes there is missing value after the merge
print(data_merged.isna().sum().sum())
