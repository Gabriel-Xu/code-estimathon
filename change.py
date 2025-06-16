import os

# Set the folder where the files are stored
folder = "txtFiles (1 - 100000)"  # Replace with the correct folder name if different

# Loop through all numbers from 1 to 100000
for i in range(1, 100001):
    old_name = f"{i}.txt"
    new_name = f"FILE-{i}.txt"
    
    old_path = os.path.join(folder, old_name)
    new_path = os.path.join(folder, new_name)

    # Rename if the file exists
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
