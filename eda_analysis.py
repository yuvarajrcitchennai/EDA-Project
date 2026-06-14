import pandas as pd

df = pd.read_csv("dataset.csv")

print("Dataset Info")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

print("\nCorrelation Matrix")
print(df.corr())
