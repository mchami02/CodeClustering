#The training Set
df_train = pd.read_csv("../input/train.csv",sep=',', parse_dates=['Date']
                       , date_parser=str_to_date,
                       low_memory = False)


#Additional Information on those stores 
df_store = pd.read_csv("../input/store.csv"
                       , low_memory = False)'