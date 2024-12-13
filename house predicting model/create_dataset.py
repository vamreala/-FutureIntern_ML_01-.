import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv('data/housing_data.csv')

# Prepare features and target
X = data[['square_feet', 'bedrooms', 'bathrooms', 'garage']]
y = data['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open('app/model/house_price_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved successfully!")
