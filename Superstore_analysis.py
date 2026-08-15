import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_excel("Superstore.csv.xls")

# Load data
df = pd.read_excel("Superstore.csv.xls")

# Data inspection
print("Dataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe())

# Remove duplicate rows
df = df.drop_duplicates()

# Export cleaned data
df.to_excel("cleaned_superstore.xlsx", index=False)
print("Cleaned data exported successfully!")