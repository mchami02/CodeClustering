# zip
import zipfile

with zipfile.ZipFile("/kaggle/input/restaurant-revenue-prediction/test.csv.zip") as zf:
    zf.extractall()
with zipfile.ZipFile("/kaggle/input/restaurant-revenue-prediction/train.csv.zip") as zf:
    zf.extractall()
     '