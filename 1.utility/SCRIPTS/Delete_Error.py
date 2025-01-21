import os

def delete_unmatched_images(image_dir, label_dir, image_exts=(".jpg", ".jpeg", ".png"), label_ext=".txt"):
    """
    Deletes images that don't have corresponding label files in a separate directory and prints the count.

    Args:
        image_dir (str): Path to the directory containing images.
        label_dir (str): Path to the directory containing label files.
        image_exts (tuple): Tuple of valid image file extensions (e.g., '.jpg', '.jpeg', '.png').
        label_ext (str): Extension of the label files (e.g., '.txt').
    """
    # List image and label files
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(image_exts)]
    label_files = [f for f in os.listdir(label_dir) if f.lower().endswith(label_ext)]
    
    # Extract base names without extensions for comparison
    label_basenames = {os.path.splitext(f)[0] for f in label_files}
    
    # Counter for deleted images
    deleted_count = 0
    
    # Check each image and delete if no matching label is found
    for image in image_files:
        image_basename = os.path.splitext(image)[0]
        if image_basename not in label_basenames:
            image_path = os.path.join(image_dir, image)
            os.remove(image_path)
            print(f"Deleted unmatched image: {image_path}")
            deleted_count += 1
    
    # Print summary
    print(f"Total images deleted: {deleted_count}")

# Example usage
image_directory = "C:\Sahana\ML_Project\MLTRY\Split_script\Data_Error_Delete\Images"  # Replace with your images folder path
label_directory = "C:\Sahana\ML_Project\MLTRY\Split_script\Data_Error_Delete\Labels"  # Replace with your labels folder path
delete_unmatched_images(image_directory, label_directory, image_exts=(".jpg", ".jpeg", ".png"), label_ext=".txt")