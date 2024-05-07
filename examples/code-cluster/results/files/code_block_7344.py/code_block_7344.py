%matplotlib inline
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from fastai.structured import *
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.ensemble import RandomForestRegressor
from IPython.core.debugger import set_trace
from sklearn.model_selection import KFold

import os
print(os.listdir("../input"))
PATH = "../input/"