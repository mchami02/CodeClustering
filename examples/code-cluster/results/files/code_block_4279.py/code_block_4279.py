train=data=pd.read_csv('/kaggle/input/bike-sharing-demand/train.csv')
test=pd.read_csv('/kaggle/input/bike-sharing-demand/test.csv')
train.info()
Y1train=train['casual']
Y2train=train['registered']
Ytrain=train['count']
