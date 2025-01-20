# 5 AUGMENTATION TECHNIQUES

# import os
# import cv2
# import numpy as np

# # Paths
# image_folder = r'C:\Sahana\ML_Project\MLTRY\Dataset\temp\Images_2000'
# coordinates_folder = r'C:\Sahana\ML_Project\MLTRY\Dataset\temp\Labels_2000'
# output_image_folder = r'C:\Sahana\ML_Project\MLTRY\AUGMENT\AUG_Images'
# output_coordinates_folder = r'C:\Sahana\ML_Project\MLTRY\AUGMENT\AUG_Labels'

# # Create output folders if they don't exist
# os.makedirs(output_image_folder, exist_ok=True)
# os.makedirs(output_coordinates_folder, exist_ok=True)

# # Save the original image and annotations
# def save_original(image_path, annotation_path):
#     original_image_path = os.path.join(output_image_folder, f"original_{os.path.basename(image_path)}")
#     original_annotation_path = os.path.join(output_coordinates_folder, f"original_{os.path.basename(annotation_path)}")

#     # Save original image
#     cv2.imwrite(original_image_path, cv2.imread(image_path))

#     # Save original annotations
#     with open(annotation_path, 'r') as src, open(original_annotation_path, 'w') as dst:
#         dst.writelines(src.readlines())

# # Rotate the image by 90°, 180°, 270°
# def rotate_image(image_path, output_path, angle):
#     image = cv2.imread(image_path)
#     if angle == 90:
#         rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
#     elif angle == 180:
#         rotated_image = cv2.rotate(image, cv2.ROTATE_180)
#     elif angle == 270:
#         rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
#     cv2.imwrite(output_path, rotated_image)

# # Rotate keypoints (90° and 270° rotations only, without flipping)
# def rotate_keypoints(annotation_path, output_path, angle):
#     transformed_annotations = []
    
#     with open(annotation_path, 'r') as f:
#         lines = f.readlines()

#     for line in lines:
#         parts = line.strip().split()
#         class_label = parts[0]
#         transformed_coords = [class_label]

#         for i in range(1, len(parts), 2):
#             x = float(parts[i])
#             y = float(parts[i + 1])

#             # Apply the correct rotation transformations based on the angle
#             if angle == 90:
#                 # Rotate 90 degrees clockwise and flip both horizontally and vertically
#                 new_x = 1.0 - y  # Flip horizontally after rotating 90 degrees
#                 new_y = x        # Vertical flip by rotating 90 degrees
#             elif angle == 180:
#                 # Rotate 180 degrees (flip both horizontally and vertically)
#                 new_x = 1.0 - x
#                 new_y = 1.0 - y
#             elif angle == 270:
#                 # Rotate 270 degrees clockwise (equivalent to 90 degrees counterclockwise) and flip both horizontally and vertically
#                 new_x = y        # Flip vertically after rotating 270 degrees
#                 new_y = 1.0 - x  # Horizontal flip by rotating 270 degrees
#             else:
#                 # If no valid angle, retain original coordinates (no rotation)
#                 new_x = x
#                 new_y = y

#             transformed_coords.extend([f"{new_x:.6f}", f"{new_y:.6f}"])

#         transformed_annotations.append(' '.join(transformed_coords))

#     # Save the transformed annotations
#     with open(output_path, 'w') as f:
#         f.write('\n'.join(transformed_annotations) + '\n')


# # Apply blur with fixed kernel size
# def blur_image(image_path, output_path, blur_size=(5, 5)):
#     image = cv2.imread(image_path)
#     blurred_image = cv2.GaussianBlur(image, blur_size, 0)
#     cv2.imwrite(output_path, blurred_image)

# # Process images and annotations
# for filename in os.listdir(image_folder):
#     if filename.endswith(('.jpg', '.jpeg', '.png')):  # Handle image file extensions
#         image_path = os.path.join(image_folder, filename)

#         annotation_filename = filename.rsplit('.', 1)[0] + '.txt'
#         annotation_path = os.path.join(coordinates_folder, annotation_filename)

#         if os.path.exists(annotation_path):  # Ensure the annotation file exists
#             save_original(image_path, annotation_path)

#             # Rotations (90°, 180°, 270°)
#             for angle in [90, 180, 270]:
#                 rotate_image(image_path, f"{output_image_folder}/rotated_{angle}_{filename}", angle)
#                 rotate_keypoints(annotation_path, f"{output_coordinates_folder}/rotated_{angle}_{annotation_filename}", angle)

#             # Blur
#             blur_image(image_path, f"{output_image_folder}/blurred_{filename}", blur_size=(5, 5))
#             # Copy annotations as-is for blurred images
#             annotation_output_path = os.path.join(output_coordinates_folder, f"blurred_{os.path.basename(annotation_path)}")
#             with open(annotation_path, 'r') as src, open(annotation_output_path, 'w') as dst:
#                 dst.writelines(src.readlines())



# 7 AUGMENTATION TECHNIQUES

import os
import cv2

# Paths
image_folder = r'Dataset\temp\FRAMES_9'
coordinates_folder = r'Dataset\temp\Frame_9'
output_image_folder = r'C:\Sahana\ML_Project\MLTRY\AUGMENT\AUG_Images'
output_coordinates_folder = r'C:\Sahana\ML_Project\MLTRY\AUGMENT\AUG_Labels'

# Create output folders if they don't exist
os.makedirs(output_image_folder, exist_ok=True)
os.makedirs(output_coordinates_folder, exist_ok=True)

# Save the original image and annotations
def save_original(image_path, annotation_path):
    original_image_path = os.path.join(output_image_folder, f"original_{os.path.basename(image_path)}")
    original_annotation_path = os.path.join(output_coordinates_folder, f"original_{os.path.basename(annotation_path)}")

    # Save original image
    cv2.imwrite(original_image_path, cv2.imread(image_path))

    # Save original annotations
    with open(annotation_path, 'r') as src, open(original_annotation_path, 'w') as dst:
        dst.writelines(src.readlines())

# Flip the image horizontally or vertically
def flip_image(image_path, output_path, flip_code):
    image = cv2.imread(image_path)
    flipped_image = cv2.flip(image, flip_code)
    cv2.imwrite(output_path, flipped_image)

# Flip keypoints horizontally or vertically with swapping
def flip_keypoints_with_swap(annotation_path, output_path, flip_code, swap_pairs=None):
    """
    Flip keypoints and optionally swap specific pairs of coordinates.

    Parameters:
    - annotation_path: Path to the input annotation file.
    - output_path: Path to save the transformed annotation file.
    - flip_code: 1 for horizontal, 0 for vertical.
    - swap_pairs: List of tuples indicating pairs of indices to swap after flipping.
    """
    transformed_annotations = []

    with open(annotation_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        class_label = parts[0]
        transformed_coords = [class_label]

        coords = []
        for i in range(1, len(parts), 2):
            x = float(parts[i])
            y = float(parts[i + 1])

            if flip_code == 1:  # Horizontal flip
                new_x = 1.0 - x
                new_y = y
            elif flip_code == 0:  # Vertical flip
                new_x = x
                new_y = 1.0 - y

            coords.append((new_x, new_y))

        # Swap specific pairs of coordinates if swap_pairs is provided
        if swap_pairs:
            for idx1, idx2 in swap_pairs:
                coords[idx1], coords[idx2] = coords[idx2], coords[idx1]

        # Flatten and format the coordinates
        for x, y in coords:
            transformed_coords.extend([f"{x:.6f}", f"{y:.6f}"])

        transformed_annotations.append(' '.join(transformed_coords))

    # Save the transformed annotations
    with open(output_path, 'w') as f:
        f.write('\n'.join(transformed_annotations) + '\n')

# Process images and annotations
for filename in os.listdir(image_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Handle image file extensions
        image_path = os.path.join(image_folder, filename)

        annotation_filename = filename.rsplit('.', 1)[0] + '.txt'
        annotation_path = os.path.join(coordinates_folder, annotation_filename)

        if os.path.exists(annotation_path):  # Ensure the annotation file exists
            save_original(image_path, annotation_path)

            # Flip operations
            # Horizontal flip
            flip_image(image_path, f"{output_image_folder}/flipped_horizontal_{filename}", 1)
            flip_keypoints_with_swap(
                annotation_path,
                f"{output_coordinates_folder}/flipped_horizontal_{annotation_filename}",
                flip_code=1,
                swap_pairs=[(8, 9)]  # Swap pair example
            )

            # Vertical flip
            flip_image(image_path, f"{output_image_folder}/flipped_vertical_{filename}", 0)
            flip_keypoints_with_swap(
                annotation_path,
                f"{output_coordinates_folder}/flipped_vertical_{annotation_filename}",
                flip_code=0,
                swap_pairs=[(8, 9)]  # Swap pair example
            )
