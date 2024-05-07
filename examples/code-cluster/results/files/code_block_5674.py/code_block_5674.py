sum_df = pd.pivot_table(train_data, values=['ConfirmedCases','Fatalities'], index=['Date'],aggfunc=np.sum)
display(sum_df.max())