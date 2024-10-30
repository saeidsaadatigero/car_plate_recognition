# Car License Plate Recognition System

This project is a car license plate recognition system that leverages advanced computer vision and deep learning techniques. The system's objective is to detect and extract vehicle license plate numbers from images captured by CCTV cameras.

## Technologies Used:
- **Django**: Web framework for backend development.
- **OpenCV**: Image processing library for handling and manipulating images.
- **YOLO (You Only Look Once)**: Deep learning model for real-time license plate detection.
- **Tesseract OCR**: Optical character recognition tool for reading license plate numbers.
- **SQLite**: Lightweight database for data storage.
- **HTML/CSS**: Frontend technologies for building and styling web pages.

## Installation and Setup

To set up and run this project, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/car_plate_recognition.git
   cd car_plate_recognition

2. Create and activate a Python virtual environment:

python3 -m venv .venv
source .venv/bin/activate


3. Install the required dependencies:

pip install -r requirements.txt


4. Start the Django server:

python manage.py runserver


5. Access the web application at:

http://127.0.0.1:8000



Using the System

1. On the homepage, enter the IP address of the CCTV camera.


2. Click "Start Plate Recognition" to begin detection and recognition.


3. Recognized license plate numbers and images will be displayed and stored.



YOLO Setup Instructions

1. Download YOLO:

Visit the official YOLO website.

Download the yolov3.weights and yolov3.cfg files.


git clone https://github.com/pjreddie/darknet
cd darknet
make
wget https://pjreddie.com/media/files/yolov3.weights

Download yolov3.cfg from this link.



2. Add to Project Directory:

Move the downloaded files into the main project directory car_plate_recognition.


mv yolov3.cfg yolov3.weights ../


3. OpenCV Setup:

Ensure that OpenCV is properly installed and configured to load YOLO models.



4. Testing:

Once YOLO is set up, run the Django server and use the camera's IP address to test the system.