import pandas as pd

file_path = "Iris.csv"
df = pd.read_csv(file_path)

print("First 8 rows of the dataset:")
print(df.head(8))

print("\nColumn names:")
print(df.columns.tolist())

df_filled = df.fillna(df.mean(numeric_only=True))
df_cleaned = df_filled.dropna()
grouped_by_species = df_cleaned.groupby("Species")

sepal_length_mean = df_cleaned["SepalLengthCm"].mean()
sepal_length_min = df_cleaned["SepalLengthCm"].min()
sepal_length_max = df_cleaned["SepalLengthCm"].max()

print("\nSepalLengthCm Statistics:")
print(f"Mean: {sepal_length_mean}")
print(f"Min: {sepal_length_min}")
print(f"Max: {sepal_length_max}")
