# import shutil
# import os
# import subprocess

# def copy_image(source_path, destination_folder):
#     if not os.path.exists(destination_folder):
#         os.makedirs(destination_folder)
    
#     shutil.copy(source_path, destination_folder)
#     print(f"Image copied to {destination_folder}")

# def git_push(repo_path, commit_message="Added new image"):
#     try:
#         subprocess.run(["git", "add", "*"], cwd=repo_path, check=True)
#         subprocess.run(["git", "commit", "-m", commit_message], cwd=repo_path, check=True)
#         subprocess.run(["git", "push"], cwd=repo_path, check=True)
#         print("Changes pushed to Git repository.")
#     except subprocess.CalledProcessError as e:
#         print(f"Git error: {e}")

# if __name__ == "__main__":
#     source_folder = r"E:\Github\New folder (2)\data\photos\AK 47\V4"  # Update this path
#     destination_folder = r"E:\Github\Gun_position_detection\AK 47\dataset\photos\V4"  # Update this path
    
#     images = sorted(os.listdir(source_folder))
#     for image in images:
#         source_image = os.path.join(source_folder, image)
#         copy_image(source_image, destination_folder)
#         git_push(commit_message=f"Added image {image}")
import shutil
import os
import subprocess

def copy_image(source_path, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    shutil.copy(source_path, destination_folder)
    print(f"Image copied to {destination_folder}")

def git_push(commit_message="Added new image"):
    try:
        subprocess.run(["git", "add", "*"], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed to Git repository.")
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")

if __name__ == "__main__":
    source_folder = r"E:\Github\New folder (2)\data\photos\AK 47\V4"  # Update this path
    destination_folder = r"E:\Github\Gun_position_detection\AK 47\dataset\photos\V4"  # Update this path
    
    images = sorted(os.listdir(source_folder))
    for image in images:
        source_image = os.path.join(source_folder, image)
        copy_image(source_image, destination_folder)
        git_push(commit_message=f"Added image {image}")
