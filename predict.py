import joblib

# Load the pre-trained model when the Flask application starts
model_custom = joblib.load('trained_model.joblib')
mse = joblib.load('mse_custom.joblib')

def predict(X_test):
    y_pred_custom = model_custom.predict(X_test)
    return y_pred_custom

print(mse)


