import shutil
import os
import subprocess

def copy_images(image_list, source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    for image in image_list:
        source_image = os.path.join(source_folder, image)
        shutil.copy(source_image, destination_folder)
        print(f"Image copied: {image}")

def git_push(commit_message="Added new images batch"):
    try:
        subprocess.run(["git", "add", "*"], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed to Git repository.")
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")

if __name__ == "__main__":
    source_folder = r"E:\Github\New folder (2)\data\photos\AK 47\V3"  # Update this path
    destination_folder = r"E:\Github\Gun_position_detection\AK 47\dataset\photos\V3"  # Update this path
    
    images = sorted(os.listdir(source_folder))
    mid_index = len(images) // 2
    
    first_half = images[:mid_index]
    second_half = images[mid_index:]
    
    # Process first half
    copy_images(first_half, source_folder, destination_folder)
    git_push(commit_message="Added first half of images")
    
    # Process second half
    copy_images(second_half, source_folder, destination_folder)
    git_push(commit_message="Added second half of images")
