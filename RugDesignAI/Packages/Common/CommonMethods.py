from sklearn.neighbors import KDTree
import numpy as np
import cv2

class Method:
    @staticmethod
    def apply_kd_tree_to_image(image, original_colors):
        pixels = image.reshape(-1, 3)
        kd_tree = KDTree(original_colors)
        distances, indices = kd_tree.query(pixels, k=1)
        final_colors = original_colors[indices.flatten()]
        return final_colors.reshape(image.shape)

    @staticmethod
    def interpolation_image(image, new_width, new_height):
        return cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

    @staticmethod
    def fix_uncolored_pixels(final_image, resized_image, original_colors):
        for y in range(final_image.shape[0]):
            for x in range(final_image.shape[1]):
                if np.array_equal(final_image[y, x], [255, 255, 255]):  # إذا كان اللون أبيض (غير ملون)
                    closest_color_index = np.argmin(np.linalg.norm(original_colors - resized_image[y, x], axis=1))
                    final_image[y, x] = original_colors[closest_color_index]
        return final_image

