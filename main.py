"""
File Organizer Script

This program organizes files inside a selected folder into subfolders
based on file type, such as images, documents, videos, compressed files,
3D models, shortcuts, and more.
"""

import os
import shutil
from datetime import datetime


# Returns a category name based on the file extension
def get_category(extension):
    extension = extension.lower()

    if extension in [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"]:
        return "Images"
    elif extension in [".pdf"]:
        return "PDF"
    elif extension in [".xlsx", ".xls", ".csv"]:
        return "Excel"
    elif extension in [".docx", ".doc", ".txt", ".pptx", ".ppt"]:
        return "Documents"
    elif extension in [".mp4", ".mkv", ".avi", ".mov"]:
        return "Videos"
    elif extension in [".zip", ".rar", ".7z"]:
        return "Compressed"
    elif extension in [".stl", ".3mf", ".step", ".obj"]:
        return "3D_Models"
    elif extension in [".svg", ".ai"]:
        return "Design_Files"
    elif extension in [".url", ".lnk"]:
        return "Shortcuts"
    elif extension in [".iso"]:
        return "Disk_Images"
    else:
        return "Others"


# Generates a new file path if a file with the same name already exists
def get_unique_path(destination_folder, file_name):
    base_name, extension = os.path.splitext(file_name)
    new_path = os.path.join(destination_folder, file_name)
    counter = 1

    while os.path.exists(new_path):
        new_file_name = f"{base_name}_{counter}{extension}"
        new_path = os.path.join(destination_folder, new_file_name)
        counter += 1

    return new_path


# Writes a message to the log file with a timestamp
def write_log(folder_path, message):
    log_path = os.path.join(folder_path, "organizer_log.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")


# Organizes files inside a folder into category-based subfolders
def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Error: the path does not exist.")
        return

    if not os.path.isdir(folder_path):
        print("Error: the provided path is not a folder.")
        return

    write_log(folder_path, "Organization process started.")

    files = os.listdir(folder_path)
    moved_files = 0
    created_categories = set()

    for file_name in files:
        full_path = os.path.join(folder_path, file_name)

        # Process only files and ignore subfolders
        if os.path.isfile(full_path):
            _, extension = os.path.splitext(file_name)
            category = get_category(extension)

            destination_folder = os.path.join(folder_path, category)

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
                created_categories.add(category)

            new_path = get_unique_path(destination_folder, file_name)
            shutil.move(full_path, new_path)

            moved_files += 1
            final_file_name = os.path.basename(new_path)

            if final_file_name != file_name:
                print(f"Moved: {file_name} -> {category} (renamed to {final_file_name})")
                write_log(folder_path, f"Moved: {file_name} -> {category} | Renamed to: {final_file_name}")
            else:
                print(f"Moved: {file_name} -> {category}")
                write_log(folder_path, f"Moved: {file_name} -> {category}")

    print("\nOrganization completed.")
    print(f"Total files moved: {moved_files}")
    print(f"Categories created: {len(created_categories)}")

    write_log(folder_path, f"Organization completed. Total files moved: {moved_files}")


while True:
    folder_path = input("\nEnter the folder path to organize (or type 'exit' to quit): ")

    if folder_path.lower() == "exit":
        print("Exiting program...")
        break

    organize_files(folder_path)