import os
import shutil

# 1. Define your file path (using 'r' to handle Windows backslashes)
original_path = r"C:\Users\chand\Downloads\py.csv"
backup_folder = r"C:\Users\chand\Documents"
new_name = r"C:\Users\chand\Downloads\renamed_py.csv"

# Check if the file exists before starting
if os.path.exists(original_path):
    
    # --- PART 1: Accessing/Listing Files ---
    print("Files in Downloads:", os.listdir(r"C:\Users\chand\Downloads"))

    # --- PART 2: Copying the File ---
    # Copying to Documents folder as a backup
    shutil.copy(original_path, os.path.join(backup_folder, "py_backup.csv"))
    print(f"File copied to {backup_folder}")

    # --- PART 3: Renaming the File ---
    # Changing 'py.csv' to 'renamed_py.csv' in the Downloads folder
    os.rename(original_path, new_name)
    print(f"File renamed to: {new_name}")

    # --- PART 4: Moving the File ---
    # Moving the renamed file to the Documents folder
    shutil.move(new_name, os.path.join(backup_folder, "moved_py.csv"))
    print("File moved to Documents folder.")

else:
    print("Error: The file 'py.csv' was not found in the Downloads folder.")
