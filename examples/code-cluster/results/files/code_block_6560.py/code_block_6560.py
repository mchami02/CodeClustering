#import libraries
import pandas as pd
import numpy as np
import os, random ,cv2
import keras
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Conv2D, Dense, Flatten, Dropout, Activation, MaxPool2D
from keras.optimizers import Adam, RMSprop
from keras.losses import binary_crossentropy
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt


