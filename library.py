import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing  # or whichever part of sklearn you need
import scipy

#here i will make functions to then import into my jupyter notebook. 
#1: create a function to load the data.
def loading_data():
    return pd.read_csv(r"C:\Users\lopke\Downloads\NVidia_stock_history.csv")
data = loading_data()
#2 plotting the distribution of all columns in the dataframe
def plot_dist(data):
    for col in data.columns:
        plt.figure(figsize=(10,5))
        sns.histplot(data[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()

# plot_dist(data)




                    