import cv2
import numpy as np

class MergeType:
    @staticmethod
    def merge_with_matched_rows(image_path, output_path):
        image = cv2.imread(image_path)
        flipped_image = cv2.flip(image, 0)

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        flipped_image_rgb = cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB)

        last_row = image_rgb[-1, :]
        first_row = flipped_image_rgb[0, :]

        if np.array_equal(last_row, first_row):
            merged_image_rgb = np.vstack((flipped_image_rgb, image_rgb))
            merged_image = cv2.cvtColor(merged_image_rgb, cv2.COLOR_RGB2BGR)
            height, width, _ = image.shape
            padded_image = np.zeros((height * 2, width, 3), dtype=np.uint8)
            padded_image[:merged_image.shape[0], :merged_image.shape[1]] = merged_image

            save_path = output_path
            cv2.imwrite(save_path, padded_image)
            print(f"The Design with padding was saved in : {save_path}")
        else:
            print("ERROR !!!")

    @staticmethod
    def merge_with_left_right_patterns(image_path, pattern_path, output_path):
        image = cv2.imread(image_path)
        pattern = cv2.imread(pattern_path)
        flipped_image = cv2.flip(image, 0)

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        flipped_image_rgb = cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB)
        pattern_rgb = cv2.cvtColor(pattern, cv2.COLOR_BGR2RGB)

        image_height, image_width, _ = image_rgb.shape
        pattern_height, pattern_width, _ = pattern_rgb.shape

        padded_pattern = np.ones((pattern_height, image_width, 3), dtype=np.uint8) * 255  # White background

        padded_pattern[:, :pattern_width] = pattern_rgb

        rotated_pattern_rgb = cv2.rotate(pattern_rgb, cv2.ROTATE_180)

        padded_pattern[:, image_width - pattern_width:] = rotated_pattern_rgb

        merged_image_rgb = np.vstack((flipped_image_rgb, padded_pattern, image_rgb))

        merged_image = cv2.cvtColor(merged_image_rgb, cv2.COLOR_RGB2BGR)

        cv2.imwrite(output_path, merged_image)
        print(f"The design with patterns on the left and right with white padding was saved in: {output_path}")






