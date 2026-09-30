import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



# Load data from CSV file
data = pd.read_csv('home_dataset.csv')

# Extract features and target variable
house_sizes = data['HouseSize'].values
house_prices = data['HousePrice'].values

# Visualise the data
plt.scatter(house_sizes, house_prices, marker='o', color='#8dd3c7')
plt.title('House Prices vs. House Size')
plt.xlabel('House Size (sq.ft)')
plt.ylabel('House Price ($)')
#plt.savefig('houses-data.png', dpi=300, bbox_inches='tight')
plt.show()


# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(house_sizes, house_prices, test_size=0.2, random_state=42)

# Reshape the data for NumPy
x_train = x_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)

# Create and then train the model
model = LinearRegression()
model.fit(x_train, y_train)


# Predict prices for the test set
predictions = model.predict(x_test)

# Visualize the predictions
plt.scatter(x_test, y_test, marker='o', color='#8dd3c7', label='Actual Prices')
plt.plot(x_test, predictions, color='#bebada', linewidth=2, label='Predicted Prices')
plt.title('Property Price Prediction with Linear Regression')
plt.xlabel('House Size (sq.ft)')
plt.ylabel('House Price (millions $)')
plt.legend()
#plt.savefig('houses-linear-regression.png', dpi=300, bbox_inches='tight')
plt.show()

