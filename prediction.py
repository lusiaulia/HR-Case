import pandas as pd
import numpy as np
import pickle
from pickle import load

#Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

features = ['Age', 'EnvironmentSatisfaction', 'DistanceFromHome', 'JobInvolvement', 
            'JobLevel', 'JobSatisfaction', 'MonthlyIncome', 'StockOptionLevel', 'YearsAtCompany', 'OverTime']

def make_predictions(input_data):
    new_data = pd.read_csv(input_data)
    # new_data["Attrition"] = new_data["Attrition"].astype(np.int64)
    new_data = new_data[features]
    predictions = model.predict(new_data)
    return predictions

if __name__ == "__main__":
    input_file = "input_data.csv" 
    predictions = make_predictions(input_file)
    print("Predictions:", predictions)
