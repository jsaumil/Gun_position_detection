import os
import cv2
import numpy as np

# Paths
image_path = r"C:\Users\hemil\OneDrive\Desktop\Gun_position\data\photos\LMG\project.6"
annotation_path = r"C:\Users\hemil\OneDrive\Desktop\Gun_position\data\Labels\LMG\project.6"
output_image_folder = r"C:\Users\hemil\OneDrive\Desktop\Gun_position\augmented_output\images"
output_coordinates_folder = r"C:\Users\hemil\OneDrive\Desktop\Gun_position\augmented_output\images"

# Ensure output folders exist
os.makedirs(output_image_folder, exist_ok=True)
os.makedirs(output_coordinates_folder, exist_ok=True)


# Flip image horizontally
def flip_image_horizontally(image):
    return cv2.flip(image, 1)


# Flip keypoints horizontally
def flip_keypoints_horizontally(annotation_path, image_width):
    flipped_annotations = []
    with open(annotation_path, 'r') as file:
        for line in file.readlines():
            parts = line.strip().split()
            class_label = parts[0]
            flipped_coords = [class_label]
            for i in range(1, len(parts), 2):
                x = float(parts[i])
                y = float(parts[i + 1])
                flipped_x = 1.0 - x  # Flip normalized x-coordinate
                flipped_coords.extend([f"{flipped_x:.6f}", f"{y:.6f}"])
            flipped_annotations.append(" ".join(flipped_coords))
    return flipped_annotations


# Rotate image 90 degrees clockwise
def rotate_image_90_clockwise(image):
    return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)


# Rotate keypoints 90 degrees clockwise
def rotate_keypoints_clockwise(annotation_path):
    rotated_annotations = []
    with open(annotation_path, 'r') as file:
        for line in file.readlines():
            parts = line.strip().split()
            class_label = parts[0]
            rotated_coords = [class_label]
            for i in range(1, len(parts), 2):
                x = float(parts[i])
                y = float(parts[i + 1])
                rotated_x = y
                rotated_y = 1.0 - x
                rotated_coords.extend([f"{rotated_x:.6f}", f"{rotated_y:.6f}"])
            rotated_annotations.append(" ".join(rotated_coords))
    return rotated_annotations


# Save annotations
def save_annotations(output_path, annotations):
    with open(output_path, 'w') as file:
        for annotation in annotations:
            file.write(annotation + "\n")


# Process single image and annotation
def process_image_and_annotation(image_path, annotation_path, output_image_folder, output_coordinates_folder):
    image_name = os.path.basename(image_path)
    annotation_name = os.path.basename(annotation_path)

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image {image_path}")
        return

    height, width = image.shape[:2]

    # Save original image and annotations
    cv2.imwrite(os.path.join(output_image_folder, f"original_{image_name}"), image)
    with open(annotation_path, 'r') as src, open(
            os.path.join(output_coordinates_folder, f"original_{annotation_name}"), 'w') as dst:
        dst.writelines(src.readlines())

    # Flip horizontally
    flipped_image = flip_image_horizontally(image)
    flipped_image_path = os.path.join(output_image_folder, f"flipped_horizontal_{image_name}")
    cv2.imwrite(flipped_image_path, flipped_image)

    flipped_annotations = flip_keypoints_horizontally(annotation_path, width)
    flipped_annotation_path = os.path.join(output_coordinates_folder, f"flipped_horizontal_{annotation_name}")
    save_annotations(flipped_annotation_path, flipped_annotations)

    # Rotate 90 degrees clockwise
    rotated_image = rotate_image_90_clockwise(image)
    rotated_image_path = os.path.join(output_image_folder, f"rotated_90_clockwise_{image_name}")
    cv2.imwrite(rotated_image_path, rotated_image)

    rotated_annotations = rotate_keypoints_clockwise(annotation_path)
    rotated_annotation_path = os.path.join(output_coordinates_folder, f"rotated_90_clockwise_{annotation_name}")
    save_annotations(rotated_annotation_path, rotated_annotations)


# Process all images in the folder
def process_folder(image_folder, coordinates_folder, output_image_folder, output_coordinates_folder):
    for filename in os.listdir(image_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(image_folder, filename)

            annotation_filename = os.path.splitext(filename)[0] + ".txt"
            annotation_path = os.path.join(coordinates_folder, annotation_filename)

            if os.path.exists(annotation_path):  # Ensure the annotation file exists
                process_image_and_annotation(image_path, annotation_path, output_image_folder,
                                             output_coordinates_folder)
            else:
                print(f"Annotation file not found for {filename}, skipping.")


# Determine if paths are directories or files
if os.path.isfile(image_path) and os.path.isfile(annotation_path):
    print("Processing single image and annotation...")
    process_image_and_annotation(image_path, annotation_path, output_image_folder, output_coordinates_folder)
elif os.path.isdir(image_path) and os.path.isdir(annotation_path):
    print("Processing folder of images and annotations...")
    process_folder(image_path, annotation_path, output_image_folder, output_coordinates_folder)
else:
    print("Error: Invalid paths provided. Please check if the paths are correct.")

print("Processing completed.")
