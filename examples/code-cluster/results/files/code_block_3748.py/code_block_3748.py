import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os

print(os.listdir("../input"))
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
%matplotlib inline

data = pd.read_csv("../input/train.csv")
test = pd.read_csv("../input/test.csv")
test.dtypes

