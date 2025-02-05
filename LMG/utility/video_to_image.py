import cv2
import os

# # Path to your video file
# video_path = "people-detection.mp4"
video_folder = r"E:\Github\Gun_position_detection\data\video\AK47"

# Directory to save the frames
# output_dir = "frames_1fps"
# os.makedirs(output_dir, exist_ok=True)
base_output_dir = r"E:\Github\Gun_position_detection\data\photos\AK 47"

video_files = [f for f in os.listdir(video_folder) if f.lower().endswith(('.mp4', '.avi', '.mov'))]

# video_files=[]
# for f in os.listdir(video_folder):
#     if f.lower().endswith(('.mp4', '.avi', '.mov')):
#         video_files.append(f)

# Check if there are any video files
if not video_files:
    print(f"No video files found in {video_folder}.")
else:
    
    # Loop over each video file in the folder
    for video_file in video_files:
        video_path = os.path.join(video_folder, video_file)

        # Open the video file
        cap = cv2.VideoCapture(video_path)
        
        output_dir = os.path.join(base_output_dir, os.path.splitext(video_file)[0])
        os.makedirs(output_dir, exist_ok=True)

        if not cap.isOpened():
            print(f"Error: Cannot open video file '{video_path}'.")
            continue


        # Get the video FPS
        video_fps = int(cap.get(cv2.CAP_PROP_FPS))
        # frame_skip = video_fps  # For 1 FPS, skip (video FPS) frames
        # print(f"Video FPS: {video_fps}, Extracting at 1 FPS (every {frame_skip} frames).")
        print(f"Video FPS: {video_fps}")

        frame_count = 0
        frame_index = 0

        while True:
            # Read a frame from the video
            ret, frame = cap.read()
            if not ret:
                break  # Exit the loop if no more frames

            frame_filename = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved: {frame_filename}")
            frame_count += 1
            
            # Save frames at 1 FPS
            # if frame_index % frame_skip == 0:
            #     frame_filename = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")
            #     cv2.imwrite(frame_filename, frame)
            #     print(f"Saved: {frame_filename}")
            #     frame_count += 1

            frame_index += 1

        print(f"Total frames saved: {frame_count}")

        # Release the video capture object
        cap.release()
