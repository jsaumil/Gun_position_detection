import os

# Specify the folder where your images are stored
folder_path = 'C:\\Users\\chavd\\Downloads\\38a653c9-9dc9-45ac-a51b-5ee493a5336a'

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a .png
    if filename.endswith('.png'):
        # Get the full file path
        png_file_path = os.path.join(folder_path, filename)
        
        # Generate the new .jpg file path
        jpg_file_path = os.path.join(folder_path, filename.replace('.png', '.jpg'))
        
        # Rename the file
        os.rename(png_file_path, jpg_file_path)
        print(f"Renamed: {filename} -> {filename.replace('.png', '.jpg')}")