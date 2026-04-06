import pandas as pd
df = pd.read_excel(r'e:\5prog_1experience.xlsx')
print("Data Overview:")
print(df.head())
print("\nData Types:")
print(df.dtypes)
print("\nSummary Statistics:")
print(df.describe())
print("\nCentral Tendencies and Dispersion Measures:")
for column in df.select_dtypes(include=['number']).columns:
    print(f"\nColumn: {column}")
    print(f"Mean: {df[column].mean()}")
    print(f"Median: {df[column].median()}")
    print(f"Mode: {df[column].mode().tolist()}")
    print(f"Variance: {df[column].var()}")
    print(f"Standard Deviation: {df[column].std()}")
    print(f"Range: {df[column].max() - df[column].min()}")
    print(f"Interquartile Range (IQR): {df[column].quantile(0.75) - df[column].quantile(0.25)}")

if 'score' in df.columns:
    centraltendency = df['score'].mean()
    print(f"\nMean of 'score' column: {centraltendency}")
else:
    print("\n'score' column not found in the data.")
