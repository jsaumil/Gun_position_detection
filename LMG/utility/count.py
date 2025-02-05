import os

def count_files_in_folders(base_photos_dir, base_labels_dir):
    # Get all folder names in the base directories
    photo_folders = {folder for folder in os.listdir(base_photos_dir) if os.path.isdir(os.path.join(base_photos_dir, folder))}
    label_folders = {folder for folder in os.listdir(base_labels_dir) if os.path.isdir(os.path.join(base_labels_dir, folder))}
    
    # Find common folders
    common_folders = photo_folders.intersection(label_folders)
    
    for folder in common_folders:
        photos_folder = os.path.join(base_photos_dir, folder)
        labels_folder = os.path.join(base_labels_dir, folder)
        
        # Count files in each folder
        num_photos = len([file for file in os.listdir(photos_folder) if os.path.isfile(os.path.join(photos_folder, file))])
        num_labels = len([file for file in os.listdir(labels_folder) if os.path.isfile(os.path.join(labels_folder, file))])
        
        print(f"Folder: {folder}")
        print(f"  Photos: {num_photos} files")
        print(f"  Labels: {num_labels} files")

base_photos_dir = r"/home/saumil/Git/Gun_position_detection/LMG/dataset/photos"  # Replace with the base directory of your photos
base_labels_dir = r"/home/saumil/Git/Gun_position_detection/LMG/annotaions"  # Replace with the base directory of your labels

count_files_in_folders(base_photos_dir, base_labels_dir)