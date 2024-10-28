import cv2
import numpy as np

class SizeWhiteSpace:
    @staticmethod
    def getHeightAndWidthWhiteArea(image_path):
        # قراءة الصورة بالألوان
        image = cv2.imread(image_path)

        # تحويل الصورة إلى الفضاء اللوني HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # تحديد نطاق اللون الأبيض في HSV
        lower_white = np.array([0, 0, 200])
        upper_white = np.array([180, 30, 255])

        # إنشاء قناع للون الأبيض
        mask = cv2.inRange(hsv, lower_white, upper_white)

        # تطبيق عمليات مورفولوجية لتنظيف القناع
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        # البحث عن الكونتورات
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if not contours:
            return 0, 0  # إذا لم يتم العثور على أي منطقة بيضاء

        # اختيار أكبر كونتور (يفترض أنه المنطقة البيضاء الرئيسية)
        largest_contour = max(contours, key=cv2.contourArea)

        # الحصول على المستطيل المحيط
        _, _, w, h = cv2.boundingRect(largest_contour)

        return h, w


