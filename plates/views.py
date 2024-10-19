import cv2
import pytesseract
from django.shortcuts import render

from load_model import net
from .models import LicensePlate
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import numpy as np
from django.conf import settings

# تنظیم مسیر tesseract
pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_CMD

# بارگذاری مدل YOLO
# net = cv2.dnn.readNet(settings.YOLOV3_WEIGHTS, settings.YOLOV3_CFG)
# layer_names = net.getLayerNames()
# output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
layer_names = net.getLayerNames()
try:
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
except IndexError as e:
    print(f"خطا در پیدا کردن لایه‌ها: {e}")
    output_layers = []


def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
    return thresh

def detect_plate(frame):
    height, width, _ = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    boxes = []
    confidences = []
    class_ids = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    plate_boxes = [boxes[i] for i in indexes]

    return plate_boxes

def read_plate(image):
    processed_image = preprocess_image(image)
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    plate_number = pytesseract.image_to_string(processed_image, config=custom_config)
    return plate_number.strip()

def capture_from_ip_camera(request):
    ip_address = request.POST.get('ip_address')
    if not ip_address:
        return render(request, 'upload.html', {'error': 'لطفا آدرس IP را وارد کنید.'})

    cap = cv2.VideoCapture(ip_address)
    plate_number = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        plate_boxes = detect_plate(frame)
        if plate_boxes:
            for box in plate_boxes:
                x, y, w, h = box
                plate_image = frame[y:y+h, x:x+w]
                plate_number = read_plate(plate_image)

                if plate_number:
                    _, buffer = cv2.imencode('.jpg', plate_image)
                    image_content = ContentFile(buffer)
                    image_path = default_storage.save(f'plates/{plate_number}.jpg', image_content)
                    LicensePlate.objects.create(plate_number=plate_number, image=image_path)
                    break

    cap.release()

    if not plate_number:
        return render(request, 'upload.html', {'error': 'پلاکی شناسایی نشد.'})

    return render(request, 'result.html', {'plate_number': plate_number})


from django.shortcuts import render

def home(request):
    return render(request, 'upload.html')
# #views.py
# import cv2
# import pytesseract
# from django.shortcuts import render
# from .models import LicensePlate
# from django.core.files.base import ContentFile
# from django.core.files.storage import default_storage
# import numpy as np
#
# # بارگذاری مدل YOLO
# net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
# layer_names = net.getLayerNames()
# output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
#
# def preprocess_image(image):
#     # پیش‌پردازش تصویر
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#     _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
#     return thresh
#
# def detect_plate(frame):
#     # شناسایی پلاک با استفاده از YOLO
#     height, width, _ = frame.shape
#     blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
#     net.setInput(blob)
#     outs = net.forward(output_layers)
#
#     boxes = []
#     confidences = []
#     class_ids = []
#
#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.5:  # آستانه اطمینان
#                 center_x = int(detection[0] * width)
#                 center_y = int(detection[1] * height)
#                 w = int(detection[2] * width)
#                 h = int(detection[3] * height)
#                 x = int(center_x - w / 2)
#                 y = int(center_y - h / 2)
#
#                 boxes.append([x, y, w, h])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)
#
#     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
#     plate_boxes = []
#     for i in range(len(boxes)):
#         if i in indexes:
#             plate_boxes.append(boxes[i])
#
#     return plate_boxes
#
# def read_plate(image):
#     # خواندن شماره پلاک
#     processed_image = preprocess_image(image)
#     custom_config = r'--oem 3 --psm 6 outputbase digits'
#     plate_number = pytesseract.image_to_string(processed_image, config=custom_config)
#     return plate_number.strip()
#
# def capture_from_ip_camera(request):
#     ip_address = request.POST.get('ip_address')
#     if not ip_address:
#         return render(request, 'upload.html', {'error': 'لطفا آدرس IP را وارد کنید.'})
#
#     cap = cv2.VideoCapture(ip_address)
#     ret, frame = cap.read()
#     if not ret:
#         return render(request, 'upload.html', {'error': 'دوربین قابل دسترسی نیست.'})
#
#     plate_boxes = detect_plate(frame)
#     if plate_boxes:
#         for box in plate_boxes:
#             x, y, w, h = box
#             plate_image = frame[y:y+h, x:x+w]
#             plate_number = read_plate(plate_image)
#
#             if plate_number:
#                 # ذخیره تصویر پلاک
#                 _, buffer = cv2.imencode('.jpg', plate_image)
#                 image_content = ContentFile(buffer)
#                 image_path = default_storage.save(f'plates/{plate_number}.jpg', image_content)
#                 LicensePlate.objects.create(plate_number=plate_number, image=image_path)
#
#     cap.release()
#     return render(request, 'result.html', {'plate_number': plate_number})
#
#
# def home(request):
#     return render(request, 'upload.html')  # اطمینان حاصل کنید که فایل home.html وجود دارد
