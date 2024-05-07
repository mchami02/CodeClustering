df_store['PromoInterval'] = df_store['PromoInterval'].map({'Jan,Apr,Jul,Oct':1 , 'Feb,May,Aug,Nov':2 , 'Mar,Jun,Sept,Dec':3})
df_store['PromoInterval'] = df_store['PromoInterval'].astype(int)