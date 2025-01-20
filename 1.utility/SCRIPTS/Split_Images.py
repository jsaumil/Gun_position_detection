import os
import shutil
import random

def split_images_and_labels(images_folder, labels_folder, destination_folder):
    # Define the folder structure
    train_folder = os.path.join(destination_folder, "Train")
    valid_folder = os.path.join(destination_folder, "Valid")

    # Create subfolder structure for images and labels
    for folder in [train_folder, valid_folder]:
        os.makedirs(os.path.join(folder, "Images"), exist_ok=True)
        os.makedirs(os.path.join(folder, "Labels"), exist_ok=True)

    # Get all image files in the source images folder
    images = [file for file in os.listdir(images_folder) if file.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'tiff'))]

    # Shuffle the images to randomize the split
    random.shuffle(images)

    # Calculate split sizes
    total_images = len(images)
    train_size = int(total_images * 0.7)

    # Split the images
    train_images = images[:train_size]
    valid_images = images[train_size:]

    def copy_files(file_list, target_folder):
        for image in file_list:
            # Define source paths
            image_path = os.path.join(images_folder, image)
            label_path = os.path.join(labels_folder, os.path.splitext(image)[0] + ".txt")

            # Define destination paths
            image_dest = os.path.join(target_folder, "Images", image)
            label_dest = os.path.join(target_folder, "Labels", os.path.splitext(image)[0] + ".txt")

            # Copy image
            shutil.copy(image_path, image_dest)

            # Copy corresponding label if it exists
            if os.path.exists(label_path):
                shutil.copy(label_path, label_dest)

    # Copy files to respective folders
    copy_files(train_images, train_folder)
    copy_files(valid_images, valid_folder)

    print(f"Total images: {total_images}")
    print(f"Train images: {len(train_images)}")
    print(f"Validation images: {len(valid_images)}")

# Example usage
images_folder = input("Enter the path to your source folder containing images: ").strip()
labels_folder = input("Enter the path to your source folder containing labels: ").strip()
destination_folder = os.path.join(os.path.dirname(images_folder), "DataSET")
split_images_and_labels(images_folder, labels_folder, destination_folder)
