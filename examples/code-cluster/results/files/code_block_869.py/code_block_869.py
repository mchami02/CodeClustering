usa = train[train['Country_Region'] == "US"]
usa_latest = usa[usa['Date'] == max(usa['Date'])]
usa_latest = usa_latest.groupby('Province_State')['ConfirmedCases', 'Fatalities'].max().reset_index()
fig = px.bar(usa_latest.sort_values('ConfirmedCases', ascending=False)[:10][::-1], 
             x='ConfirmedCases', y='Province_State', color_discrete_sequence=['#D63230'],
             title='Confirmed Cases in USA', text='ConfirmedCases', orientation='h')
fig.show()'