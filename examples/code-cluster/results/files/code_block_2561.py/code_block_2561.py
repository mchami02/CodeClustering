test_merged['Open']=test_merged['Open'].fillna(1)
test_merged['Date']=pd.to_datetime(test_merged['Date'],format='%Y-%m-%d')
test_merged['day']=test_merged['Date'].dt.day
test_merged['month']=test_merged['Date'].dt.month
test_merged['year']=test_merged['Date'].dt.year


test_merged['StateHoliday']=test_merged['StateHoliday'].map({'0':0,'a':1})
test_merged['StateHoliday']=test_merged['StateHoliday'].astype(int)
test_merged.isna().sum()