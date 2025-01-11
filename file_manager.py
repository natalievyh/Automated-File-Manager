import os
import shutil

file_types = {
    'Documents': ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.ppt', '.pptx'],
    'Photos': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mmov', '.wmv'],
    'Audio': ['.mp3', '.wav'],
    'Zip': ['.zip', '.tar', '.gz', '.rar'],
}

def organize_files(path):
    if not os.path.isdir(path):
        print(f"The path {path} is not a valid directory.")
        return
    
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            filename, file_ext = os.path.splitext(file)
            moved = False
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    destination_folder = os.path.join(path, folder)
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    shutil.move(file_path, destination_folder)
                    print(f"Moved: {file} to {destination_folder}")
                    moved = True
                    break
            if not moved:
                print(f"Unknown file type: {file}, not moved.")


input_path = input('Enter the path to the directory you would like to organize: ').strip()

organize_files(input_path)

