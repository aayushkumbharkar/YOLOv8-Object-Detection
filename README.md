
# 🚀 YOLOv8 Object Detection with Python

This project performs object detection using [YOLOv8](https://github.com/ultralytics/ultralytics) by Ultralytics on:
- 🖼️ **Images**
- 🎥 **Webcam**
- 📹 **Videos**

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/aayushkumbharkar/YOLOv8-Object-Detection.git
cd YOLOv8-Object-Detection
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Download YOLOv8 Weights

YOLO model weights are not uploaded to this repo due to the large file size.
Please download them manually:

### 🔹 Download Links from Ultralytics:

* **YOLOv8n (nano - fast & small):**
  [Download yolov8n.pt](https://github.com/ultralytics/assets/releases/latest/download/yolov8n.pt)

* **YOLOv8l (large - more accurate):**
  [Download yolov8l.pt](https://github.com/ultralytics/assets/releases/latest/download/yolov8l.pt)

### 📁 After downloading:

* Place the `.pt` files (weights) into the **root directory** of the project (where `.py` files are).

---

## 🚀 How to Run

### 🖼️ Image Detection

```bash
python Yolo-images.py
```

### 🎥 Webcam Detection

```bash
python Yolo-webcam-and-videos.py
```

📌 **Press `q` to quit** the webcam window.

---

## 📁 Project Structure

```
YOLOv8-Object-Detection/
├── Yolo-images.py
├── Yolo-webcam-and-videos.py
├── yolov8n.pt
├── yolov8l.pt
├── requirements.txt
├── Media
└── README.md
```

---

## 🧠 Built With

* [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* OpenCV
* Python

---

## 🙌 Acknowledgements

Special thanks to [Ultralytics](https://github.com/ultralytics) for making YOLOv8 so accessible.

```


