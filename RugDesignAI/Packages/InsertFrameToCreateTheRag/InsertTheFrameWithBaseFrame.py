import cv2
from PIL import Image

class RugDesign:
    @staticmethod
    def MergedTheFrames(base_image_path, overlay_images, output_image_path, use_white_space=True):
        if not base_image_path or not overlay_images:
            return "Error: Please provide a base image and overlay images."

        try:
            base_image = cv2.imread(base_image_path)
            if base_image is None:
                return f"Error: Unable to load base image from {base_image_path}"

            if use_white_space:
                overlay_image = cv2.imread(overlay_images)
                if overlay_image is None:
                    return f"Error: Unable to load overlay image from {overlay_images}"

                gray_base_image = cv2.cvtColor(base_image, cv2.COLOR_BGR2GRAY)
                _, binary_image = cv2.threshold(gray_base_image, 240, 255, cv2.THRESH_BINARY)
                contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                if contours:
                    for contour in contours:
                        x, y, w, h = cv2.boundingRect(contour)
                        overlay_h, overlay_w = overlay_image.shape[:2]

                        if overlay_w < w or overlay_h < h or overlay_w > w or overlay_h > h:
                            overlay_image = cv2.resize(overlay_image, (w, h), interpolation=cv2.INTER_NEAREST_EXACT)
                            overlay_h, overlay_w = overlay_image.shape[:2]

                        base_image[y:y + overlay_h, x:x + overlay_w] = overlay_image

                    pil_image = Image.fromarray(cv2.cvtColor(base_image, cv2.COLOR_BGR2RGB))
                    pil_image.save(output_image_path, format='BMP')
                    return f"Success: Image saved to: {output_image_path}"

                return "Warning: No suitable white space found for the overlay image."

            else:
                for idx, overlay_path in enumerate(overlay_images):
                    overlay_image = cv2.imread(overlay_path)
                    if overlay_image is None:
                        return f"Error: Unable to load overlay image from {overlay_path}"

                    h, w = base_image.shape[:2]
                    frame_w, frame_h = w // 3, h // 2
                    x, y = (idx % 3) * frame_w, (idx // 3) * frame_h

                    overlay_resized = cv2.resize(overlay_image, (frame_w, frame_h))
                    base_image[y:y + frame_h, x:x + frame_w] = overlay_resized

                cv2.imwrite(output_image_path, base_image)
                return f"Carpet design saved to: {output_image_path}"

        except Exception as e:
            return f"Error: An error occurred: {str(e)}"