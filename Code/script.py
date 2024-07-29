import cv2
import numpy as np

def resize_and_combine(image_path, scale_factor):
    # تحميل الصورة
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # تقسيم الصورة إلى 4 أجزاء
    top_left = image[0:height//2, 0:width//2]
    top_right = image[0:height//2, width//2:width]
    bottom_left = image[height//2:height, 0:width//2]
    bottom_right = image[height//2:height, width//2:width]

    # تغيير حجم كل جزء
    top_left_resized = cv2.resize(top_left, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    top_right_resized = cv2.resize(top_right, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    bottom_left_resized = cv2.resize(bottom_left, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    bottom_right_resized = cv2.resize(bottom_right, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

    # دمج الأجزاء مرة أخرى
    top_row = np.hstack((top_left_resized, top_right_resized))
    bottom_row = np.hstack((bottom_left_resized, bottom_right_resized))
    combined_image = np.vstack((top_row, bottom_row))

    # حساب الحجم الجديد للصورة المدمجة
    new_height, new_width, _ = combined_image.shape

    # ضبط نافذة العرض لتكون مرنة
    window_name = 'Combined Image'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, new_width, new_height)

    # عرض الصورة
    cv2.imshow(window_name, combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# استخدام الدالة
resize_and_combine('OIP.jpg', scale_factor=3.0)
