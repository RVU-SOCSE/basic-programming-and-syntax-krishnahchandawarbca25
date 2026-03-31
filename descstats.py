import numpy as np
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'Education': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Master'],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'phone number': ['123-456-7890', '987-654-3210', '555-555-5555', '111-222-3333', '444-555-6666']}

GPA = [3.5, 3.8, 3.9, 3.2, 3.7]
data['GPA'] = GPA
weight = [150, 180, 160, 170, 155]
data['Weight'] = weight 
height = [60, 70, 65, 68, 62]
data['Height'] = height

df = pd.DataFrame(data)
print("Mean age:", df['Age'].mean())
print("Mean GPA:", df['GPA'].mean())
print("Mean weight:", df['Weight'].mean())
print("Mean height:", df['Height'].mean())
print("Median age:", df['Age'].median())
print("Median GPA:", df['GPA'].median())    
print("Median weight:", df['Weight'].median())
print("Median height:", df['Height'].median())
print("Standard Deviation of age:", df['Age'].std())
print("Standard Deviation of GPA:", df['GPA'].std())
print("Standard Deviation of weight:", df['Weight'].std())
print("Standard Deviation of height:", df['Height'].std())
print("Variance of age:", df['Age'].var())
print("Variance of GPA:", df['GPA'].var())
print("Variance of weight:", df['Weight'].var())
print("Variance of height:", df['Height'].var())
print("Minimum age:", df['Age'].min())
print("Minimum GPA:", df['GPA'].min())
print("Minimum weight:", df['Weight'].min())