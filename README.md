![Screenshot from 2024-10-19 17-41-46](https://github.com/user-attachments/assets/a2117319-10dd-452a-9c67-82276d164984)


# Car License Plate Recognition System

This project is a car license plate recognition system using advanced computer vision and deep learning technologies. The goal of the system is to detect and extract vehicle license plate numbers from images captured by CCTV cameras.

## Technologies Used:
- **Django**: Web framework for server-side development.
- **OpenCV**: Image processing library to handle images.
- **YOLO (You Only Look Once)**: Deep learning model for license plate detection.
- **Tesseract OCR**: Text recognition tool for reading license plate numbers.
- **SQLite**: Lightweight database to store data.
- **HTML/CSS**: For creating and styling web pages.

## Installation and Setup

To run this project, follow these steps:

1. Clone the project repository:
   ```bash
   git clone https://github.com/yourusername/car_plate_recognition.git
   cd car_plate_recognition
   ```

2. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Django server:
   ```bash
   python manage.py runserver
   ```

5. Access the web application at:
   ```
   http://127.0.0.1:8000
   ```

## Using the System
1. Navigate to the homepage and enter the IP address of the CCTV camera.
2. Click the "Start Plate Recognition" button to initiate the plate detection and recognition process.
3. The recognized license plate numbers will be displayed, and the plate images will be saved.


# YOLO Download and Setup Instructions

1. **Download YOLO**:
   - Visit the [official YOLO website](https://pjreddie.com/darknet/yolo/).
   - Download the `yolov3.weights` and `yolov3.cfg` files.

   ### Run the following commands in the terminal:
   ```bash
   git clone https://github.com/pjreddie/darknet
   cd darknet
   make
   wget https://pjreddie.com/media/files/yolov3.weights