import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the dataset
cars_data = pd.read_csv("Toyota.csv", index_col=0, na_values=["??", "????"])

# Scatter plot: Age vs Price
plt.scatter(cars_data['Age'], cars_data['Price'], c='red')
plt.title('Scatter plot of Price vs Age of the Cars')
plt.xlabel('Age (months)')
plt.ylabel('Price (Euros)')
plt.show()

# Histogram: KM
plt.hist(cars_data['KM'], color='grey', edgecolor='white', bins=10)
plt.title('Histogram of Kilometer')
plt.xlabel('Kilometer')
plt.ylabel('Frequency')
plt.show()

# Bar Plot: Fuel Type
counts = cars_data['FuelType'].value_counts()
print(counts)
print(type(counts))

counts.plot(kind='bar', color=['red', 'blue', 'cyan'])
plt.title("Bar plot of fuel types")
plt.xlabel("Fuel Types")
plt.ylabel("Frequency")
plt.show()

# Pie Chart: Fuel Type
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Pie chart of fuel types")
plt.show()

# Box Plot: Price vs FuelType
car_price = cars_data.groupby('FuelType')['Price']
plt.boxplot([group.dropna().values for name, group in car_price], labels=car_price.groups.keys())
plt.title("Box plot of Car Prices by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Price (Euros)")
plt.show()
