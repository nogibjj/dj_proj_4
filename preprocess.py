### preprocess data
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

def read_training_data(data):
    df = pd.read_csv(data)
    

if __name__ == "__main__":
    data = "train.csv"
    read_training_data(data)

