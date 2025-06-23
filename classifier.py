import os
import shutil
import sys

def classify_files_by_extension(source_folder, target_extension):
    # Normalize extension format (remove dot if given)
    if target_extension.startswith('.'):
        target_extension = target_extension[1:]
    
    # Create destination folder
    destination_folder = os.path.join(source_folder, target_extension + "_files")
    os.makedirs(destination_folder, exist_ok=True)

    # Scan all files in the source folder
    files_moved = 0
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)
        
        # Check if it's a file and matches the extension
        if os.path.isfile(file_path) and file_name.lower().endswith(f".{target_extension.lower()}"):
            shutil.move(file_path, os.path.join(destination_folder, file_name))
            files_moved += 1

    print(f" ->  Moved {files_moved} file(s) to {destination_folder}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python file_classifier.py <folder_path> <extension>")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    extension = sys.argv[2]
    
    classify_files_by_extension(folder_path, extension)

