#trainn and test validate

features=data_merged.columns.drop(['Sales','Date'])
from sklearn.model_selection import train_test_split
train_x,validate_x,train_y,validate_y=train_test_split(data_merged[features],np.log(data_merged['Sales']+1),test_size=0.2,random_state=1)

train_x.shape,validate_x.shape,train_y.shape,validate_y.shape