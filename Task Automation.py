# Task Automation: Move all .jpg files from one folder to another
import os
import shutil

source_folder = input("Enter source folder path: ")
destination_folder = input("Enter destination folder path: ")

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Move .jpg files
moved_files = 0
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        src = os.path.join(source_folder, filename)
        dest = os.path.join(destination_folder, filename)
        shutil.move(src, dest)
        moved_files += 1

print(f"{moved_files} .jpg files moved from {source_folder} to {destination_folder}.")
