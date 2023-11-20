
import numpy as np
class CustomLinearRegression:
    def __init__(self):
        self.coefficients = None
        self.intercept = None

    def fit(self, X, y):
        """
        Fit the linear regression model.

        Parameters:
        - X: Input features (numpy array or pandas DataFrame)
        - y: Target variable (numpy array or pandas Series)
        """

        # Compute coefficients using the normal equation
        # theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

        # Solve linear least squares
        theta, residuals, _, _ = np.linalg.lstsq(X, y, rcond=None)

        # Extract intercept and coefficients
        self.intercept = theta[0]
        self.coefficients = theta[1:]

    def predict(self, X):
        """
        Make predictions using the fitted model.

        Parameters:
        - X: Input features for prediction (numpy array or pandas DataFrame)

        Returns:
        - Predicted values (numpy array)
        """
        return X.dot(np.concatenate([[self.intercept], self.coefficients]))

    def get_coefficients(self):
        """
        Get the coefficients of the linear regression model.

        Returns:
        - Coefficients (numpy array)
        """
        return self.coefficients

    def get_intercept(self):
        """
        Get the intercept of the linear regression model.

        Returns:
        - Intercept (float)
        """
        return self.intercept
