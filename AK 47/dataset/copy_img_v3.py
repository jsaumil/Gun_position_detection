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

def git_commit(commit_message="Added new images batch"):
    try:
        subprocess.run(["git", "add", "*"], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print("Changes committed to Git repository.")
    except subprocess.CalledProcessError as e:
        print(f"Git commit error: {e}")

def git_push():
    try:
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed to Git repository.")
    except subprocess.CalledProcessError as e:
        print(f"Git push error: {e}")

if __name__ == "__main__":
    source_folder = r"E:\Github\New folder (2)\data\photos\AK 47\V4"  # Update this path
    destination_folder = r"E:\Github\Gun_position_detection\AK 47\dataset\photos\V4"  # Update this path
    
    images = sorted(os.listdir(source_folder))
    batch_size = 500
    
    for i in range(0, len(images), batch_size):
        batch = images[i:i+batch_size]
        copy_images(batch, source_folder, destination_folder)
        git_commit(commit_message=f"Added batch {i//batch_size + 1} of images")
        git_push()
