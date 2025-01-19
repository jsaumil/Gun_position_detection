# import os
# os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


import torch
print(torch.cuda.is_available())  # Should print True if CUDA is available
print(torch.cuda.device_count())  # Should show number of CUDA devices

from ultralytics import YOLO

# Load YOLOv8 Nano Pose Model
model = YOLO("yolov8n-pose.pt")  # The Nano variant for pose/keypoint detection
# model.overrides["kpt_shape"] = [8, 3]

# Train the model
results = model.train(
    data="/home/rohan/New folder/data.yaml",  # Path to your custom dataset YAML
    epochs=25,                    # Number of epochs
    imgsz=640,                    # Image size
    batch=16,                     # Batch size
    name="yolov8n_keypoints",     # Experiment name
    device=0                      # Use GPU (0) or CPU (-1)
)

# Validate the model
results.plot()

model.save() 
# Export the model
# model.export(format="onnx")  # Optional: Export to ONNX for deployment
