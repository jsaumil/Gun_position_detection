# import cv2
# import os
# import numpy as np
# from ultralytics import YOLO

# # Load the pretrained YOLOv8 model
# model = YOLO("lmg_best.pt")

# # Define keypoint names and skeleton connections
# keypoint_names = [
#     "butt", "pistol grip", "trigger", "cover", "rear sight",
#     "barrel jacket", "left bipod", "right bipod"
# ]

# skeleton = [
#     (0, 3),  # Butt -> Cover
#     (3, 2),  # Cover -> Trigger
#     (3, 4),  # Cover -> Rear Sight
#     (3, 1),  # Cover -> Pistol Grip
#     (4, 5),  # Rear Sight -> Barrel Jacket
#     (5, 6),  # Barrel Jacket -> Left Bipod
#     (5, 7)   # Barrel Jacket -> Right Bipod
# ]

# # Input and output folder paths
# input_folder = r"TestVideos\LMG"
# output_folder = r"Outputs"

# # Create output folder if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)

# # Process each video in the input folder
# for video_file in os.listdir(input_folder):
#     if not video_file.endswith((".mp4", ".avi", ".mov", ".MOV")):
#         continue

#     input_video_path = os.path.join(input_folder, video_file)
#     output_video_path = os.path.join(output_folder, f"annotated_{video_file}")

#     # Open the input video
#     cap = cv2.VideoCapture(input_video_path)
#     if not cap.isOpened():
#         print(f"Error: Could not open video {input_video_path}")
#         continue

#     # Get video properties
#     fps = int(cap.get(cv2.CAP_PROP_FPS))
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')

#     # Initialize VideoWriter
#     out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

#     # Process each frame
#     frame_count = 0
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Perform inference
#         results = model.predict(source=frame, conf=0.2, device='cpu', save=True)
#         result = results[0]  # Assume single frame

#         # Draw bounding boxes and keypoints if detected
#         if result.boxes is not None:
#             for box in result.boxes:
#                 # Draw bounding box
#                 x1, y1, x2, y2 = map(int, box.xyxy[0])
#                 cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

#                 # Draw label
#                 label = f"{box.cls_name} ({box.conf:.2f})"
#                 cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

#         if result.keypoints is not None and len(result.keypoints.xy) > 0:
#             keypoints = result.keypoints.xy  # Keypoint coordinates
#             for kp_set in keypoints:  # Loop over detected objects
#                 kp_set = np.array(kp_set)

#                 # Draw keypoints
#                 for idx, (x, y) in enumerate(kp_set):
#                     cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 0), -1)
#                     cv2.putText(frame, keypoint_names[idx], (int(x), int(y) - 10),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

#                 # Draw skeleton connections
#                 for connection in skeleton:
#                     # Ensure keypoints exist before drawing skeleton lines
#                     if len(kp_set) > max(connection):
#                         pt1 = kp_set[connection[0]]
#                         pt2 = kp_set[connection[1]]
#                         if not np.isnan(pt1).any() and not np.isnan(pt2).any():
#                             cv2.line(frame, (int(pt1[0]), int(pt1[1])), (int(pt2[0]), int(pt2[1])),
#                                      (0, 0, 255), 2)

#         # Write the frame to the output video
#         out.write(frame)

#         # Display the frame in a window
#         # cv2.imshow("Output", frame)

#         frame_count += 1
#         print(f"Processed frame {frame_count} in video {video_file}")

#         # Exit the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release resources for the current video
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()

#     print(f"Finished processing video {video_file}. Output saved to {output_video_path}")

# print("All videos processed.")

import os
import cv2
from ultralytics import YOLO

# Load the pretrained YOLOv8 model
model = YOLO("lmg_best.pt")

# Define input and output directories
input_dir = r"TestVideos\LMG"
output_dir = r"Outputs"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

def process_video(video_path, output_path, model):
    """Process a single video, apply the model, convert to grayscale, and save the output."""
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Apply the model prediction (assuming it works on single frames)
        predicted_frame = model.predict(frame)  # Replace with your actual model prediction logic

        # Convert the predicted frame to grayscale
        grayscale_frame = cv2.cvtColor(predicted_frame, cv2.COLOR_BGR2GRAY)

        # Convert grayscale back to 3 channels to save as a video
        grayscale_frame = cv2.cvtColor(grayscale_frame, cv2.COLOR_GRAY2BGR)

        # Initialize VideoWriter with the same dimensions as the input frame
        if out is None:
            height, width, _ = grayscale_frame.shape
            out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (width, height))

        # Write the grayscale frame to the output video
        out.write(grayscale_frame)

    cap.release()
    if out:
        out.release()

# Iterate over all videos in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mov"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"output_{filename}")

        print(f"Processing: {filename}")
        process_video(input_path, output_path, model)

print("Processing complete!")