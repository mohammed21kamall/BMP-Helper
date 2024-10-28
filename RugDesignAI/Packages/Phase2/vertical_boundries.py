import cv2
import numpy as np

class MergingPatternVertical:

    @staticmethod
    def create_repeated_image_with_vertical(image_repeat_path, output_path, num_repeats):
        # Load both images
        image_repeat = cv2.imread(image_repeat_path)

        # Get dimensions of the images
        height_repeat, width_repeat, _ = image_repeat.shape

        # Determine the maximum width
        max_width = max(0, width_repeat)

        # Resize images to have the same width
        if width_repeat != max_width:
            image_repeat = cv2.resize(image_repeat, (max_width, height_repeat), interpolation=cv2.INTER_AREA)

        # Create a new image with the appropriate size
        new_height = (height_repeat * num_repeats)
        new_image = np.zeros((new_height, max_width, 3), dtype=np.uint8)

        # Paste the repeated image multiple times
        for i in range(num_repeats):
            new_image[i * height_repeat:(i + 1) * height_repeat, 0:max_width] = image_repeat
    

        # Save and show the new image
        cv2.imwrite(output_path, new_image)

    @staticmethod
    def create_repeated_image_with_vertical_flip(image_repeat_path, output_path, num_repeats):
        # Load the image
        image_repeat = cv2.imread(image_repeat_path)

        # Get dimensions of the image
        height_repeat, width_repeat, _ = image_repeat.shape

        # Determine the maximum width
        max_width = max(0, width_repeat)

        # Resize images to have the same width
        if width_repeat != max_width:
            image_repeat = cv2.resize(image_repeat, (max_width, height_repeat), interpolation=cv2.INTER_AREA)

        # Create a new image with the appropriate size
        new_height = height_repeat * num_repeats
        new_image = np.zeros((new_height, max_width, 3), dtype=np.uint8)

        # Paste the repeated image multiple times with flipping alternation
        for i in range(num_repeats):
            if i % 2 == 1:  # Flip the image every other repeat
                flipped_image = cv2.flip(image_repeat, 0)  # Vertical flip
                new_image[i * height_repeat:(i + 1) * height_repeat, 0:max_width] = flipped_image
            else:
                new_image[i * height_repeat:(i + 1) * height_repeat, 0:max_width] = image_repeat

        # Save and show the new image
        cv2.imwrite(output_path, new_image)
