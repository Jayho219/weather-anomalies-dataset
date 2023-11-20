from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

from utilities.download_csv_from_current_directory import download_csv_from_current_directory
from utilities.print_data_samples import print_sample
from utilities.label_encoding import label_encoding
from utilities.custom_linear_regression import CustomLinearRegression


df = download_csv_from_current_directory()
# print_sample(df, 5)


label_encoding(df)
# print_sample(df, 5)

# Add a new column 'avg_temp' with the average of 'max_temp' and 'min_temp'
def add_avg_temp_column(df):
    df['avg_temp'] = (df['max_temp'] + df['min_temp'])
add_avg_temp_column(df)


from sklearn.model_selection import train_test_split

X = df.drop(['avg_temp'], axis=1) 
y = df['avg_temp'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the shapes of the resulting sets
# print("X_train shape:", X_train.shape)
# print("X_test shape:", X_test.shape)
# print("y_train shape:", y_train.shape)
# print("y_test shape:", y_test.shape)


# Create and train the custom Linear Regression model
model_custom = CustomLinearRegression()
model_custom.fit(X_train, y_train)

# Create and train the scikit-learn Linear Regression model
model_sklearn = LinearRegression()
model_sklearn.fit(X_train, y_train)

# Make predictions
y_pred_custom = model_custom.predict(X_test)
y_pred_sklearn = model_sklearn.predict(X_test)

# Print Mean Squared Error for both models
mse_custom = mean_squared_error(y_test, y_pred_custom)
mse_sklearn = mean_squared_error(y_test, y_pred_sklearn)
print("Mean Squared Error (Custom):", mse_custom)
print("Mean Squared Error (Scikit-learn):", mse_sklearn)


# Save the trained model to a file
joblib.dump(model_custom, 'trained_model.joblib')
joblib.dump(mse_custom,  'mse_custom.joblib')
