# import os
# import shutil

# def copy_only_wanted_files(base_photos_dir, base_labels_dir):
#     # List all folder names in the base directories
#     photo_folders = {folder for folder in os.listdir(base_photos_dir) if os.path.isdir(os.path.join(base_photos_dir, folder))}
#     label_folders = {folder for folder in os.listdir(base_labels_dir) if os.path.isdir(os.path.join(base_labels_dir, folder))}
    
#     # Find common folder names
#     common_folders = photo_folders.intersection(label_folders)
    
    
#     for folder in common_folders:
#         photos_folder = os.path.join(base_photos_dir, folder)
#         labels_folder = os.path.join(base_labels_dir, folder)
        
#         print(f"Processing folder: {folder}")
        
#         # Get file names (without extensions) from both folders
#         photo_files = {os.path.splitext(file)[0] for file in os.listdir(photos_folder)}
#         label_files = {os.path.splitext(file)[0] for file in os.listdir(labels_folder)}
        

#         common_files = photo_files & label_files
#         if not common_files:
#             print(f"No common files found in folder: {folder}")
#             continue
        
#         destination_dir = "split_data"
#         os.makedirs(destination_dir, exist_ok=True)
        
#         file_count = 0
#         for file_name in os.listdir(photos_folder):
#             base_name, ext = os.path.splitext(file_name)
#             if base_name in common_files:
#                 src_path = os.path.join(photos_folder, file_name)
#                 dest_path = os.path.join(destination_dir, f"frame_{file_count:05}{ext}")
#                 shutil.copy(src_path, dest_path)
#                 print(f"Copied photo: {file_name} -> {dest_path}")
#                 file_count += 1
        
#         file_count=0
#         for file_name in os.listdir(labels_folder):
#             base_name, ext = os.path.splitext(file_name)
#             if base_name in common_files:
#                 src_path = os.path.join(labels_folder, file_name)
#                 dest_path = os.path.join(destination_dir, f"frame_{file_count:05}{ext}")
#                 shutil.copy(src_path, dest_path)
#                 print(f"Copied label: {file_name} -> {dest_path}")
#                 file_count += 1
                
    
# base_photos_dir = r"data/Labels/LMG"  # Replace with the base directory of your photos
# base_labels_dir = r"data/photos/LMG"

# copy_only_wanted_files(base_photos_dir, base_labels_dir)

import os
import shutil

def copy_common_folders(label_dir, photo_dir, target_dir):
    label_folders = set(os.listdir(label_dir))
    photo_folders = set(os.listdir(photo_dir))
    common_folders = label_folders.intersection(photo_folders)
    os.makedirs(target_dir, exist_ok=True)

    for folder in common_folders:
        label_folder_path = os.path.join(label_dir, folder)
        photo_folder_path = os.path.join(photo_dir, folder)
        target_folder_path = os.path.join(target_dir, folder)
        os.makedirs(target_folder_path, exist_ok=True)

        # Copy files from label folder
        if os.path.isdir(label_folder_path):
            for file in os.listdir(label_folder_path):
                src = os.path.join(label_folder_path, file)
                dst = os.path.join(target_folder_path, file)
                try:
                    if os.path.isfile(src):
                        shutil.copy(src, dst)
                        print(f"Copied {src} to {dst}")
                except Exception as e:
                    print(f"Error copying {src}: {e}")

        # Copy files from photo folder
        if os.path.isdir(photo_folder_path):
            for file in os.listdir(photo_folder_path):
                src = os.path.join(photo_folder_path, file)
                dst = os.path.join(target_folder_path, file)
                try:
                    if os.path.isfile(src):
                        shutil.copy(src, dst)
                        print(f"Copied {src} to {dst}")
                except Exception as e:
                    print(f"Error copying {src}: {e}")

    print(f"Copied all common folders to {target_dir}")

# Paths
label_dir = r"/home/rohan/Gun_position_detection/data/Labels/LMG/V1"
photo_dir = r"/home/rohan/Gun_position_detection/data/photos/LMG/V1"
target_dir = r"/home/rohan/Gun_position_detection/training test"

copy_common_folders(label_dir, photo_dir, target_dir)
