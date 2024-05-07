df_test = pd.read_csv("../input/test.csv",sep=',', parse_dates=['Date']
                       , date_parser=str_to_date,
                       low_memory = False)
print ("The Test dataset has {} Rows and {} Variables".format(str(df_test.shape[0]),str(df_test.shape[1])))'