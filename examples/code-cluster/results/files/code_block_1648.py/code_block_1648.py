# add Life expectancy
# Life expectancy at birth obtained from http://hdr.undp.org/en/data
df_life = pd.read_csv("../input/smokingstats/Life expectancy at birth.csv")
tmp = df_life.iloc[:,1].values.tolist()
df_life = df_life[['Country', '2018']]
def func(x):
    x_new = 0
    try:
        x_new = float(x.replace(",", ""))
    except:
#         print(x)
        x_new = np.nan
    return x_new
    
df_life['2018'] = df_life['2018'].apply(lambda x: func(x))
df_life.head()'