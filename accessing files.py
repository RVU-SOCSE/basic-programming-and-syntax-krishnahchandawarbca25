import os

file_path = r"C:\Users\chand\Downloads\py.csv"

if os.path.exists(file_path):
    print("File found! Ready for operations.")
else:
    print("File not found. Please check the path.")

