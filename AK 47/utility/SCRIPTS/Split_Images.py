# import os
# import shutil
# import random

# def split_images_and_labels(images_folder, labels_folder, destination_folder):
#     # Define the folder structure
#     train_folder = os.path.join(destination_folder, "Train")
#     valid_folder = os.path.join(destination_folder, "Valid")

#     # Create subfolder structure for images and labels
#     for folder in [train_folder, valid_folder]:
#         os.makedirs(os.path.join(folder, "Images"), exist_ok=True)
#         os.makedirs(os.path.join(folder, "Labels"), exist_ok=True)

#     # Get all image files in the source images folder
#     images = [file for file in os.listdir(images_folder) if file.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'tiff'))]

#     # Shuffle the images to randomize the split
#     random.shuffle(images)

#     # Calculate split sizes
#     total_images = len(images)
#     train_size = int(total_images * 0.95)

#     # Split the images
#     train_images = images[:train_size]
#     valid_images = images[train_size:]

#     def copy_files(file_list, target_folder):
#         for image in file_list:
#             # Define source paths
#             image_path = os.path.join(images_folder, image)
#             label_path = os.path.join(labels_folder, os.path.splitext(image)[0] + ".txt")

#             # Define destination paths
#             image_dest = os.path.join(target_folder, "Images", image)
#             label_dest = os.path.join(target_folder, "Labels", os.path.splitext(image)[0] + ".txt")

#             # Copy image
#             shutil.copy(image_path, image_dest)

#             # Copy corresponding label if it exists
#             if os.path.exists(label_path):
#                 shutil.copy(label_path, label_dest)

#     # Copy files to respective folders
#     copy_files(train_images, train_folder)
#     copy_files(valid_images, valid_folder)

#     print(f"Total images: {total_images}")
#     print(f"Train images: {len(train_images)}")
#     print(f"Validation images: {len(valid_images)}")

# # Example usage
# images_folder = r"/home/rohan/Gun_position_detection/data/photos/LMG/project,1"
# labels_folder = r"/home/rohan/Gun_position_detection/data/Labels/LMG/project,1"
# destination_folder = r"/home/rohan/Gun_position_detection/training test"
# split_images_and_labels(images_folder, labels_folder, destination_folder)

import os
import shutil
import random

def split_images_and_labels(images_folder, labels_folder, destination_folder):
    # Ensure source folders exist
    if not os.path.exists(images_folder) or not os.path.exists(labels_folder):
        print(f"❌ ERROR: One or both source folders do not exist: {images_folder} | {labels_folder}")
        return

    folder_prefix = os.path.basename(images_folder).replace(" ", "_")

    train_folder = os.path.join(destination_folder, "Train")
    valid_folder = os.path.join(destination_folder, "Valid")

    for folder in [train_folder, valid_folder]:
        os.makedirs(os.path.join(folder, "Images"), exist_ok=True)
        os.makedirs(os.path.join(folder, "Labels"), exist_ok=True)

    images = [file for file in os.listdir(images_folder) if file.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'tiff'))]

    if len(images) == 0:
        print(f"⚠️ WARNING: No images found in {images_folder}")
        return

    # Ensure consistent dataset split
    random.seed(42)
    random.shuffle(images)

    train_size = int(len(images) * 0.95)
    train_images = images[:train_size]
    valid_images = images[train_size:]

    def copy_files(file_list, target_folder):
        for idx, image in enumerate(file_list):
            image_path = os.path.join(images_folder, image)
            label_path = os.path.join(labels_folder, os.path.splitext(image)[0] + ".txt")

            new_filename = f"{folder_prefix}_{idx+1:04d}{os.path.splitext(image)[1]}"
            new_labelname = f"{folder_prefix}_{idx+1:04d}.txt"

            image_dest = os.path.join(target_folder, "Images", new_filename)
            label_dest = os.path.join(target_folder, "Labels", new_labelname)

            print(f"📂 Copying {image_path} -> {image_dest}")
            try:
                shutil.copy(image_path, image_dest)
            except Exception as e:
                print(f"❌ ERROR copying image: {e}")

            if os.path.exists(label_path):
                print(f"📂 Copying {label_path} -> {label_dest}")
                shutil.copy(label_path, label_dest)
            else:
                print(f"⚠️ WARNING: No label found for {image}")

    copy_files(train_images, train_folder)
    copy_files(valid_images, valid_folder)

    print(f"✅ Processed: {images_folder}")
    print(f"Total images: {len(images)}")
    print(f"Train images: {len(train_images)}")
    print(f"Validation images: {len(valid_images)}\n")


# Example usage with multiple folders
image_folders = [
    "/home/rohan/Gun_position_detection/data/photos/LMG/project,1",
    "/home/rohan/Gun_position_detection/data/photos/LMG/project.2",
    "/home/rohan/Gun_position_detection/data/photos/LMG/project.3",
    "/home/rohan/Gun_position_detection/data/photos/LMG/project.4",
    "/home/rohan/Gun_position_detection/data/photos/LMG/project.6",
    "/home/rohan/Gun_position_detection/data/photos/LMG/V1"
]
label_folders = [
    "/home/rohan/Gun_position_detection/data/Labels/LMG/project,1",
    "/home/rohan/Gun_position_detection/data/Labels/LMG/project.2",
    "/home/rohan/Gun_position_detection/data/Labels/LMG/project.3",
    "/home/rohan/Gun_position_detection/data/Labels/LMG/project.4",
    "/home/rohan/Gun_position_detection/data/Labels/LMG/project.6",
    "/home/rohan/Gun_position_detection/data/Labels/LMG/V1"
]
destination_folder = "/home/rohan/Gun_position_detection/training_test"

for img_folder, lbl_folder in zip(image_folders, label_folders):
    split_images_and_labels(img_folder, lbl_folder, destination_folder)
