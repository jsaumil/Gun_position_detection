import os
import cv2
import numpy as np

# Paths to the folders
image_folder = 'path_to_images_folder'
coordinates_folder = 'path_to_keypoints_annotations_folder'
output_image_folder = 'path_to_output_images_folder'
output_coordinates_folder = 'path_to_output_keypoints_annotations_folder'

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


# Flip the image vertically
def flip_image_vertically(image_path, output_path):
    image = cv2.imread(image_path)
    flipped_image = cv2.flip(image, 0)
    cv2.imwrite(output_path, flipped_image)


# Flip keypoints vertically
def flip_keypoints_vertically_txt(annotation_path, output_path):
    flipped_annotations = []
    with open(annotation_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        class_label = parts[0]
        flipped_coords = [class_label]

        for i in range(1, len(parts), 2):
            x = float(parts[i])
            y = float(parts[i + 1])
            flipped_y = 1.0 - y  # Flip normalized y-coordinate vertically
            flipped_coords.extend([f"{x:.6f}", f"{flipped_y:.6f}"])

        flipped_annotations.append(' '.join(flipped_coords))

    with open(output_path, 'w') as f:
        for annotation in flipped_annotations:
            f.write(f"{annotation}\n")


# Flip the image horizontally
def flip_image_horizontally(image_path, output_path):
    image = cv2.imread(image_path)
    flipped_image = cv2.flip(image, 1)
    cv2.imwrite(output_path, flipped_image)


# Flip keypoints horizontally
def flip_keypoints_horizontally_txt(annotation_path, output_path):
    flipped_annotations = []
    with open(annotation_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        class_label = parts[0]
        flipped_coords = [class_label]

        for i in range(1, len(parts), 2):
            x = float(parts[i])
            y = float(parts[i + 1])
            flipped_x = 1.0 - x  # Flip normalized x-coordinate horizontally
            flipped_coords.extend([f"{flipped_x:.6f}", f"{y:.6f}"])

        flipped_annotations.append(' '.join(flipped_coords))

    with open(output_path, 'w') as f:
        for annotation in flipped_annotations:
            f.write(f"{annotation}\n")


# Rotate the image
def rotate_image(image_path, output_path, rotation_flag):
    image = cv2.imread(image_path)
    rotated_image = cv2.rotate(image, rotation_flag)
    cv2.imwrite(output_path, rotated_image)


def rotate_keypoints_clockwise(annotation_path, output_path, original_width, original_height):
    """
    Rotate keypoints by 90 degrees clockwise and save the transformed annotations.
    """
    transformed_annotations = []
    with open(annotation_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        class_label = parts[0]
        transformed_coords = [class_label]

        for i in range(1, len(parts), 2):
            x = float(parts[i])
            y = float(parts[i + 1])

            # Step 1: Rotate 90 degrees clockwise
            rotated_x = y  # Original y becomes new x
            rotated_y = 1.0 - x  # 1 - Original x becomes new y

            # Step 2: Flip across both axes
            flipped_x = 1.0 - rotated_x
            flipped_y = 1.0 - rotated_y

            # Append transformed coordinates
            transformed_coords.extend([f"{flipped_x:.6f}", f"{flipped_y:.6f}"])

        transformed_annotations.append(' '.join(transformed_coords))

    # Save the transformed annotations
    with open(output_path, 'w') as f:
        f.write('\n'.join(transformed_annotations) + '\n')


# Rotate keypoints counterclockwise (90 degrees)
def rotate_keypoints_counterclockwise(annotation_path, output_path, image_width, image_height):
    rotated_annotations = []
    with open(annotation_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        class_label = parts[0]
        rotated_coords = [class_label]

        for i in range(1, len(parts), 2):
            x = float(parts[i])
            y = float(parts[i + 1])

            # Step 1: Apply counterclockwise rotation
            rotated_x = 1.0 - y  # New x is 1 - original y
            rotated_y = x  # New y is the original x

            # Step 2: Flip coordinates
            flipped_x = 1.0 - rotated_x  # Flip horizontally
            flipped_y = 1.0 - rotated_y  # Flip vertically

            # Append the flipped coordinates
            rotated_coords.extend([f"{flipped_x:.6f}", f"{flipped_y:.6f}"])

        rotated_annotations.append(' '.join(rotated_coords))

    # Save the rotated and flipped annotations
    with open(output_path, 'w') as f:
        f.write('\n'.join(rotated_annotations) + '\n')


# Rotate keypoints 180 degrees
def rotate_keypoints_180(annotation_path, output_path):
    rotated_annotations = []
    with open(annotation_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        class_label = parts[0]
        rotated_coords = [class_label]

        for i in range(1, len(parts), 2):
            x = float(parts[i])
            y = float(parts[i + 1])
            rotated_x = 1.0 - x  # Flip x
            rotated_y = 1.0 - y  # Flip y
            rotated_coords.extend([f"{rotated_x:.6f}", f"{rotated_y:.6f}"])

        rotated_annotations.append(' '.join(rotated_coords))

    with open(output_path, 'w') as f:
        f.write('\n'.join(rotated_annotations) + '\n')


# Adjust saturation, brightness, and exposure
def adjust_saturation(image, scale):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * scale, 0, 255)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


def adjust_brightness(image, scale):
    return np.clip(image * scale, 0, 255).astype(np.uint8)


def adjust_exposure(image, scale):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    lab[:, :, 0] = np.clip(lab[:, :, 0] * scale, 0, 255)
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)


def apply_color_transformation_and_save_annotations(image_path, annotation_path, transformation_func, output_image_path,
                                                    prefix):
    image = cv2.imread(image_path)
    transformed_image = transformation_func(image)
    cv2.imwrite(output_image_path, transformed_image)

    # Copy annotations as-is
    annotation_output_path = os.path.join(output_coordinates_folder, f"{prefix}_{os.path.basename(annotation_path)}")
    with open(annotation_path, 'r') as src, open(annotation_output_path, 'w') as dst:
        dst.writelines(src.readlines())


# Process images and annotations
for filename in os.listdir(image_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Handle image file extensions
        image_path = os.path.join(image_folder, filename)

        annotation_filename = filename.rsplit('.', 1)[0] + '.txt'
        annotation_path = os.path.join(coordinates_folder, annotation_filename)

        if os.path.exists(annotation_path):  # Ensure the annotation file exists
            save_original(image_path, annotation_path)

            image = cv2.imread(image_path)
            height, width = image.shape[:2]

            # Flips
            flip_image_vertically(image_path, f"{output_image_folder}/flipped_vertical_{filename}")
            flip_keypoints_vertically_txt(annotation_path,
                                          f"{output_coordinates_folder}/flipped_vertical_{annotation_filename}")

            flip_image_horizontally(image_path, f"{output_image_folder}/flipped_horizontal_{filename}")
            flip_keypoints_horizontally_txt(annotation_path,
                                            f"{output_coordinates_folder}/flipped_horizontal_{annotation_filename}")

            # Rotations
            rotate_image(image_path, f"{output_image_folder}/rotated_90_clockwise_{filename}", cv2.ROTATE_90_CLOCKWISE)
            rotate_keypoints_clockwise(annotation_path,
                                       f"{output_coordinates_folder}/rotated_90_clockwise_{annotation_filename}",
                                       width, height)

            rotate_image(image_path, f"{output_image_folder}/rotated_90_counterclockwise_{filename}",
                         cv2.ROTATE_90_COUNTERCLOCKWISE)
            rotate_keypoints_counterclockwise(annotation_path,
                                              f"{output_coordinates_folder}/rotated_90_counterclockwise_{annotation_filename}",
                                              width, height)

            rotate_image(image_path, f"{output_image_folder}/rotated_180_{filename}", cv2.ROTATE_180)
            rotate_keypoints_180(annotation_path, f"{output_coordinates_folder}/rotated_180_{annotation_filename}")

            # Saturation
            apply_color_transformation_and_save_annotations(
                image_path, annotation_path, lambda img: adjust_saturation(img, 0.6),
                os.path.join(output_image_folder, f"saturation_minus_40_{filename}"), "saturation_minus_40")

            apply_color_transformation_and_save_annotations(
                image_path, annotation_path, lambda img: adjust_saturation(img, 1.4),
                os.path.join(output_image_folder, f"saturation_plus_40_{filename}"), "saturation_plus_40")

            # Brightness
            apply_color_transformation_and_save_annotations(
                image_path, annotation_path, lambda img: adjust_brightness(img, 0.85),
                os.path.join(output_image_folder, f"brightness_minus_15_{filename}"), "brightness_minus_15")

            apply_color_transformation_and_save_annotations(
                image_path, annotation_path, lambda img: adjust_brightness(img, 1.15),
                os.path.join(output_image_folder, f"brightness_plus_15_{filename}"), "brightness_plus_15")

            # Exposure
            apply_color_transformation_and_save_annotations(
                image_path, annotation_path, lambda img: adjust_exposure(img, 0.85),
                os.path.join(output_image_folder, f"exposure_minus_15_{filename}"), "exposure_minus_15")

            apply_color_transformation_and_save_annotations(
                image_path, annotation_path, lambda img: adjust_exposure(img, 1.15),
                os.path.join(output_image_folder, f"exposure_plus_15_{filename}"), "exposure_plus_15")
