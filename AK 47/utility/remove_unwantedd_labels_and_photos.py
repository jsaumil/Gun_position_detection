import os

def delete_unmatched_files_in_folders(base_photos_dir, base_labels_dir):
    # List all folder names in the base directories
    photo_folders = {folder for folder in os.listdir(base_photos_dir) if os.path.isdir(os.path.join(base_photos_dir, folder))}
    label_folders = {folder for folder in os.listdir(base_labels_dir) if os.path.isdir(os.path.join(base_labels_dir, folder))}
    
    # Find common folder names
    common_folders = photo_folders.intersection(label_folders)
    
    for folder in common_folders:
        photos_folder = os.path.join(base_photos_dir, folder)
        labels_folder = os.path.join(base_labels_dir, folder)
        
        print(f"Processing folder: {folder}")
        
        # Get file names (without extensions) from both folders
        photo_files = {os.path.splitext(file)[0] for file in os.listdir(photos_folder)}
        label_files = {os.path.splitext(file)[0] for file in os.listdir(labels_folder)}
        
        # Find unmatched files
        unmatched_photos = photo_files - label_files
        unmatched_labels = label_files - photo_files
        
        # Delete unmatched photos
        for photo in os.listdir(photos_folder):
            photo_name, ext = os.path.splitext(photo)
            if photo_name in unmatched_photos:
                os.remove(os.path.join(photos_folder, photo))
                print(f"Deleted photo: {photo} in {photos_folder}")
        
        # Delete unmatched labels
        for label in os.listdir(labels_folder):
            label_name, ext = os.path.splitext(label)
            if label_name in unmatched_labels:
                os.remove(os.path.join(labels_folder, label))
                print(f"Deleted label: {label} in {labels_folder}")
    
    # Report folders without counterparts
    extra_photo_folders = photo_folders - label_folders
    extra_label_folders = label_folders - photo_folders
    
    if extra_photo_folders:
        print("Folders in photos but not in labels:", extra_photo_folders)
    if extra_label_folders:
        print("Folders in labels but not in photos:", extra_label_folders)

# Example usage
base_photos_dir = r"/home/rohan/Gun_position_detection/data/photos/LMG"  # Replace with the base directory of your photos
base_labels_dir = r"/home/rohan/Gun_position_detection/data/Labels/LMG"  # Replace with the base directory of your labels

delete_unmatched_files_in_folders(base_photos_dir, base_labels_dir)
