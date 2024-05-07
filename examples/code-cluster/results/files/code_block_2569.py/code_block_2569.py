OUTPUT = '/kaggle/working/'
PATH='/kaggle/input/rossmann-time-series-data-engineering/'
df = pd.read_feather(f'{PATH}df')
train_df = pd.read_feather(f'{PATH}joined2')
test_df = pd.read_feather(f'{PATH}joined2_test')
train_df.shape, test_df.shape