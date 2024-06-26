import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

# Load the dataset
housing_data = pd.read_csv('Housing.csv')

# Target variable (price)
features = housing_data.drop('price', axis=1)
target = housing_data['price']

# Categorical columns
categorical_columns = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus','bathrooms','area','stories','bedrooms']

# Define preprocessor
preprocessor = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), categorical_columns)], remainder='passthrough')

# Add linear regression to preprocessor
model = Pipeline(steps=[('preprocessor', preprocessor), ('scaler', StandardScaler()), ('regressor', LinearRegression())])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.4, random_state=42)

# Fit the model
model.fit(X_train, y_train)

# Save the model to a file
pickle_file = "housing_model.pkl"
with open(pickle_file, 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as housing_model.pkl")
