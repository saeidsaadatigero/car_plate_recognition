# سیستم تشخیص پلاک خودرو

این پروژه یک سیستم تشخیص پلاک خودرو با استفاده از تکنولوژی‌های پیشرفته بینایی ماشین و یادگیری عمیق است. هدف این سیستم، شناسایی و استخراج شماره پلاک خودروها از تصاویر دریافت شده توسط دوربین‌های مداربسته است.

## تکنولوژی‌های استفاده شده:
- **Django**: فریم‌ورک وب برای توسعه بخش سرور.
- **OpenCV**: کتابخانه پردازش تصویر برای کار با تصاویر.
- **YOLO (You Only Look Once)**: مدل یادگیری عمیق برای شناسایی پلاک خودرو.
- **Tesseract OCR**: ابزار تشخیص متن برای خواندن شماره پلاک.
- **SQLite**: پایگاه داده سبک برای ذخیره اطلاعات.
- **HTML/CSS**: ایجاد و استایل‌دهی صفحات وب.

## نصب و راه‌اندازی

برای اجرای این پروژه، مراحل زیر را دنبال کنید:

1. ابتدا مخزن پروژه را کلون کنید:
   ```bash
   git clone https://github.com/yourusername/car_plate_recognition.git
   cd car_plate_recognition
   ```

2. محیط مجازی پایتون را ایجاد و فعال کنید:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. وابستگی‌های پروژه را نصب کنید:
   ```bash
   pip install -r requirements.txt
   ```

4. سرور Django را اجرا کنید:
   ```bash
   python manage.py runserver
   ```

5. دسترسی به وب‌اپلیکیشن از طریق آدرس زیر:
   ```
   http://127.0.0.1:8000
   ```

## استفاده از سیستم
1. وارد صفحه اصلی شده و آدرس IP دوربین مداربسته را وارد کنید.
2. با کلیک بر روی دکمه "شروع پلاک‌خوانی"، سیستم شروع به شناسایی و خواندن شماره پلاک خودرو می‌کند.
3. نتایج شناسایی در صفحه نمایش داده می‌شوند و تصاویر پلاک‌ها ذخیره می‌شوند.

---

#### English

```markdown
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


# مراحل دانلود و تنظیم YOLO

1. **دانلود YOLO**:
   - به [سایت رسمی YOLO](https://pjreddie.com/darknet/yolo/) بروید.
   - فایل‌های `yolov3.weights` و `yolov3.cfg` را دانلود کنید.
### سه دستورات زیر را در ترمینال ران کنید
   - git clone https://github.com/pjreddie/darknet
cd darknet
make
   - wget https://pjreddie.com/media/files/yolov3.weights
### از این سایت yolo3.cfg را دانلود کنید 
   - https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg

2. **اضافه کردن به دایرکتوری پروژه(پوشه settings.py)**:
   - فایل‌های دانلود شده را در دایرکتوری اصلی پروژه `car_plate_recognition` قرار دهید.
   - mv yolov3.cfg yolov3.weights ../


3. **تنظیمات OpenCV**:
   - مطمئن شوید که OpenCV به درستی نصب شده است و می‌تواند مدل‌های YOLO را بارگذاری کند.

4. **آزمایش**:
   - پس از تنظیم YOLO، سرور Django را اجرا کنید و از آدرس IP دوربین برای تست استفاده کنید.
