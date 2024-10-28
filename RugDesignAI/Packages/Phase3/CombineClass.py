import cv2
import numpy as np

class CombineClass:
    @staticmethod
    def combine_images(image1_path, image2_path, image3_path, output_path):
        # Load images
        image1 = cv2.imread(image1_path)
        image2 = cv2.imread(image2_path)
        image3 = cv2.imread(image3_path)

        # Flip image3 vertically (top to bottom)
        image3_flipped = cv2.flip(image3, 0)  # 0 flips the image vertically
        flipped_image1 = cv2.flip(image1, 1)  # 1 flips the image horizontally (left to right)

        # Check if images are loaded correctly
        if image1 is None:
            print(f"Error: Could not load image from {image1_path}")
            return
        if image2 is None:
            print(f"Error: Could not load image from {image2_path}")
            return
        if image3 is None:
            print(f"Error: Could not load image from {image3_path}")
            return

        # Get dimensions of the images
        height1, width1, _ = image1.shape
        height2, width2, _ = image2.shape
        height3, width3, _ = image3.shape
        height4, width4, _ = flipped_image1.shape

        # Determine the maximum width
        max_width = max(width1 + width2 + width4, width3)

        # Determine the maximum height between image1 and image2
        max_height12 = max(height1, height2)

        # Add padding to image1 and image2 to make them the same height
        padded_image1 = cv2.copyMakeBorder(image1, max_height12 - height1, 0, 0, 0, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        padded_image2 = cv2.copyMakeBorder(image2, max_height12 - height2, 0, 0, 0, cv2.BORDER_CONSTANT, value=[255, 255, 255])

        # Keep image3 at its original height and add padding only to the sides if needed
        padded_image3 = cv2.copyMakeBorder(image3, 0, 0, 0, max_width - width3, cv2.BORDER_CONSTANT, value=[255, 255, 255])

        # Create a new image with the appropriate size
        combined_height = height3 + max_height12
        combined_width = max_width

        # Create a blank canvas for the new image
        new_image = np.zeros((combined_height, combined_width, 3), dtype=np.uint8)

        """   Phase 2   """
        # Place image3 (phase2green.bmp) at the top
        new_image[0:height3, 0:max_width] = padded_image3

        # Place the vertically flipped image3 directly above flipped_image1
        new_image[height3 - height3:height3, combined_width - width3:combined_width] = image3_flipped

        """   Corner   """
        # Place image1 (corner.bmp) in the bottom-left corner
        new_image[height3:height3 + height1, 0:width1] = padded_image1

        # Place flipped_image1 (corner.bmp flipped horizontally) in the bottom-right corner
        new_image[height3:height3 + height4, combined_width - width1:combined_width] = flipped_image1

        """   Phase 1   """
        # Place image2 (phase1green.bmp) to the right of image1
        new_image[height3:height3 + height1, width1:width1 + width2] = padded_image2
        # Save and show the new image
        cv2.imwrite(output_path, new_image)
