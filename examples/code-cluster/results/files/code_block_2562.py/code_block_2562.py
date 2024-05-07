test_merged['Assortment']=test_merged['Assortment'].map({'a':1,'b':2,'c':3})
test_merged['Assortment']=test_merged['Assortment'].astype(int)
test_merged['StoreType']=test_merged['StoreType'].map({'a':1,'b':2,'c':3,'d':4})
test_merged['StoreType']=test_merged['StoreType'].astype(int)
map_promo={'Jan,Apr,Jul,Oct':1,'Feb,May,Aug,Nov':2,'Mar,Jun,Sept,Dec':3}
test_merged['PromoInterval']=test_merged['PromoInterval'].map(map_promo)