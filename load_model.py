import cv2

# بارگذاری مدل
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
print("مدل با موفقیت بارگذاری شد.")

# بارگذاری مدل
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# دریافت نام لایه‌ها
layer_names = net.getLayerNames()

# دریافت لایه‌های خروجی
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]


print("لایه‌های خروجی:", output_layers)
