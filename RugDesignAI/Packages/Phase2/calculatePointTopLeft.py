import cv2

def find_leftmost_white_coordinate(image_path):
    # قراءة الصورة وتحويلها إلى تدرجات الرمادي
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # تحويل الصورة إلى ثنائية (أبيض وأسود) بناءً على عتبة سطوع معينة
    _, binary_image = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)

    # العثور على الحدود الخارجية للمساحات البيضاء
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # البحث عن أقصى نقطة على اليسار (الشمال)
    leftmost_point = None
    for contour in contours:
        for point in contour:
            x, y = point[0]
            if leftmost_point is None or x < leftmost_point[0]:
                leftmost_point = (x, y)

    return leftmost_point

