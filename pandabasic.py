import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'Education': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Master'],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'phone number': ['123-456-7890', '987-654-3210', '555-555-5555', '111-222-3333', '444-555-6666']}

df = pd.DataFrame(data)
print(df)
print("Data Types:\n", df.dtypes)
print("Summary Statistics:\n", df.describe())
print("Unique Cities:\n", df['City'].unique())
print("Average Age:", df['Age'].mean())
print("Median Age:", df['Age'].median())
print("Age Grouping:\n", pd.cut(df['Age'], bins=[0, 30, 40, 50], labels=['Young', 'Middle-aged', 'Senior']))
print("Education Level Counts:\n", df['Education'].value_counts())
print("City Counts:\n", df['City'].value_counts())
print("DataFrame Info:\n", df.info())

df_cleaned = df.dropna()
print("Cleaned DataFrame:\n", df_cleaned)   
df_sorted = df.sort_values(by='Age')
print("Sorted DataFrame:\n", df_sorted)
df_final = df.sort_values(by='Age').reset_index(drop=True)
print("Final DataFrame:\n", df_final)
