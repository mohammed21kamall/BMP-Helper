import cv2
import numpy as np

class MergingPatternHorizontal:
    @staticmethod
    def create_repeated_image_with_horizontal(image_repeat_path, output_path, num_repeats):
        image_repeat = cv2.imread(image_repeat_path)

        # Get dimensions of the image
        height_repeat, width_repeat, _ = image_repeat.shape

        # Determine the maximum height
        max_height = height_repeat

        # Resize images to have the same height
        if height_repeat != max_height:
            image_repeat = cv2.resize(image_repeat, (width_repeat, max_height), interpolation=cv2.INTER_AREA)

        # Create a new image with the appropriate size
        new_width = width_repeat * num_repeats
        new_image = np.zeros((max_height, new_width, 3), dtype=np.uint8)

        # Paste the repeated image multiple times
        for i in range(num_repeats):
            new_image[0:max_height, i * width_repeat:(i + 1) * width_repeat] = image_repeat

        # Save the new image using OpenCV
        cv2.imwrite(output_path, new_image)






    @staticmethod
    def create_repeated_image_with_horizontal_flip(image_repeat_path, output_path, num_repeats):
        image_repeat = cv2.imread(image_repeat_path)

        # Get dimensions of the image
        height_repeat, width_repeat, _ = image_repeat.shape

        # Determine the maximum height
        max_height = height_repeat

        # Resize images to have the same height
        if height_repeat != max_height:
            image_repeat = cv2.resize(image_repeat, (width_repeat, max_height), interpolation=cv2.INTER_AREA)

        # Create a new image with the appropriate size
        new_width = width_repeat * num_repeats
        new_image = np.zeros((max_height, new_width, 3), dtype=np.uint8)

        # Paste the repeated image multiple times with flipping alternation
        for i in range(num_repeats):
            if i % 2 == 1:  # Flip the image every other repeat
                flipped_image = cv2.flip(image_repeat, 1)  # Horizontal flip
                new_image[0:max_height, i * width_repeat:(i + 1) * width_repeat] = flipped_image
            else:
                new_image[0:max_height, i * width_repeat:(i + 1) * width_repeat] = image_repeat

        # Save the new image using OpenCV
        cv2.imwrite(output_path, new_image)

