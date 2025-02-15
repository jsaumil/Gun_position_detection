from ultralytics import YOLO

model=YOLO('LMG/model/runs/pose/yolov8n_keypoints2/weights/best.pt')
model.predict('LMG/WhatsApp Video 2025-01-17 at 16.12.55_d3de4649.mp4',save=True)