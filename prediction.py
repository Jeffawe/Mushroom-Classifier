import joblib

def predict(data):
    # Load the trained model and scaler
    svm = joblib.load('svm_model.sav')
    
    # Make prediction
    return svm.predict(data)