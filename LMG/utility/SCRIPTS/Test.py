from ultralytics import YOLO

# Load the pretrained YOLOv8 Nano model
model = YOLO("best.pt")  # Load the pretrained weights directly

# Define keypoint names based on your data
keypoint_names = [
    "butt", "pistol grip", "trigger", "cover", "rear sight", 
    "barrel jacket", "left bipod", "right bipod"
]

# Perform inference on an image
image_path =   # Ask the user for the image path
results = model.predict(image_path)  # Perform inference (returns a list of results)

# Process results
for result in results:  # Loop through the results (even if it's just one result)
    # Check if keypoints are detected
    if result.keypoints is not None and result.keypoints.xy is not None and result.keypoints.conf is not None:
        keypoints = result.keypoints.xy  # Extract keypoint coordinates
        scores = result.keypoints.conf  # Extract confidence scores for keypoints

        print("\nKeypoints Detected:")
        for idx, (point, score) in enumerate(zip(keypoints, scores)):
            name = keypoint_names[idx] if idx < len(keypoint_names) else f"point_{idx}"
            print(f"Index {idx}: {name} - Coordinates: {point.tolist()}, Confidence: {score.item():.2f}")
    else:
        print("No keypoints detected in the image.")

# Search for keypoint names by index
try:
    search_idx = int(input("\nEnter index to check keypoint name: "))
    if search_idx < len(keypoint_names):
        print(f"Keypoint at index {search_idx}: {keypoint_names[search_idx]}")
    else:
        print("Index out of range!")
except ValueError:
    print("Please enter a valid integer index.")
