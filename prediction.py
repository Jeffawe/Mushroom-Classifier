import joblib
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import pandas as pd

def predict(data):
    # Load the trained model and scaler
    svm = joblib.load('svm_model.sav')
    
    # Make prediction
    return svm.predict(data)