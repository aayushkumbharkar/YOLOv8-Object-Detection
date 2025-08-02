from torchvision.models import Weights
from ultralytics import YOLO
import cv2

model=YOLO('../Yolo-Weights/yolov8l.pt')
results = model("Kids-boarding-EV-Bus.jpg" )
annotated_frame = results[0].plot()  # This returns the image with bounding boxes drawn

# Display the image
cv2.imshow("YOLOv8 Detection", annotated_frame)
cv2.waitKey(0)