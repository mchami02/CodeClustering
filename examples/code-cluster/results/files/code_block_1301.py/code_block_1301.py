mask = dftest["ConfirmedCases"].isnull()
print(mask.sum())
errors = dftest.loc[mask]
print(errors)
mask = dftest["Fatalities"].isnull()
print(mask.sum())
errors = dftest.loc[mask]
print(errors)
dftest.drop(['Province_State','Country_Region','Date'],axis=1,inplace=True)
print("dftest columns =",dftest.columns)
'