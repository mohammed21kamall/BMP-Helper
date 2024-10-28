import cv2

def find_bottom_right_white_coordinate(image_path):
    # قراءة الصورة وتحويلها إلى تدرجات الرمادي
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # تحويل الصورة إلى ثنائية (أبيض وأسود) بناءً على عتبة سطوع معينة
    _, binary_image = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)

    # العثور على الحدود الخارجية للمساحات البيضاء
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # البحث عن النقطة السفلية اليمنى
    bottom_right_point = None
    for contour in contours:
        for point in contour:
            x, y = point[0]
            if bottom_right_point is None or (x > bottom_right_point[0] or (x == bottom_right_point[0] and y > bottom_right_point[1])):
                bottom_right_point = (x, y)

    return bottom_right_point

