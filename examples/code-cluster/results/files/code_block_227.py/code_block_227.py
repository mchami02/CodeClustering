for date in dates:
    k = k-1
    i = i+1
    test.loc[(test['Country_Region']=='Italy')&(test['Date']==date),
            'ConfirmedCases_x']=last_amount.values[0] + i*(5000-(100*i))
    test.loc[(test['Country_Region']=='Italy')&(test['Date']==date),
             'Fatalities_x'] =  last_fat.values[0]+i*(800-(10*i))