import numpy as np
import pandas as pd
data = {"name": ["Alice", "Bob", "Charlie", "David", "Eve"], 
        "age": [25, 30, 35, 40, 45], 
        "education": ["Bachelor", "Master", "PhD", "Bachelor", "Master"], 
        "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"], 
        "phone number": ["123-456-7890", "987-654-3210", "555-555-5555", "111-222-3333", "444-555-6666"],
        "gpa": [3.5, 3.8, 3.9, 3.2, 3.7], 
        "weight": [150, 180, 160, 170, 155], 
        "height": [60, 70, 65, 68, 62]}

df = pd.DataFrame(data)
print(df)
print("=== describe() ===")
print(df.describe(include='all'))
print("=== quantile() ===")
numeric_cols = df.select_dtypes(include=[np.number]).columns
print(df[numeric_cols].quantile([0.25, 0.5, 0.75]))
print("=== value_counts() ===")
print("=== kurtosis() ===")
print(df[numeric_cols].kurtosis())
print("=== skew() ===")
print(df[numeric_cols].skew())
