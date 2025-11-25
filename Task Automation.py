import os
import shutil

# Source folder (where your .jpg files are)
source_folder = r"C:\Users\Hp\Pictures\Source"

# Destination folder
destination_folder = r"C:\Users\Hp\Pictures\JPG_Files"

# Create destination folder if not exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move all .jpg files
for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        src_path = os.path.join(source_folder, file)
        dest_path = os.path.join(destination_folder, file)
        shutil.move(src_path, dest_path)
        print(f"Moved: {file}")

print("Task completed.")
