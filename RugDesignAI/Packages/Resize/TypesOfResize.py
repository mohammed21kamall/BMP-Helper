from Packages.Common.ResizeCode import upscale_image, extract_original_colors
from Packages.Common.CommonMethods import Method
from cv2 import dnn_superres
from math import ceil
import cv2
import os

class ResizeTool:
    @staticmethod
    def resizeImagesWithStaticFactor(image_paths, output_path, n_colors=50):
            method = Method()
            sr = dnn_superres.DnnSuperResImpl_create()
            sr.readModel("Packages/Model/EDSR_x3.pb")
            sr.setModel("edsr", 3)
            new_image_paths = []
            for image_path in image_paths:
                try:

                    image = cv2.imread(image_path)
                    if image is None:
                        print(f"Failed to read image: {image_path}")
                        continue

                    upscaled_image = upscale_image(sr, image)

                    new_width = ceil(upscaled_image.shape[1] * (1.5 / 3))
                    new_height = ceil(upscaled_image.shape[0] * (1.5 / 3))
                    resized_image = method.interpolation_image(upscaled_image, new_width, new_height)

                    original_colors = extract_original_colors(image, n_colors)

                    final_image = method.apply_kd_tree_to_image(resized_image, original_colors)

                    final_image = method.fix_uncolored_pixels(final_image, resized_image, original_colors)

                    output_file_path = os.path.join(output_path, os.path.basename(image_path))
                    cv2.imwrite(output_file_path, final_image)

                    new_image_paths.append(output_file_path)
                except Exception as e:
                    print(f"Error processing image {image_path}: {str(e)}")

            return new_image_paths

    @staticmethod
    def resizeImagesWithDynamicFactor(image_paths, output_path, scale_factor, n_colors=50):
        method = Method()

        sr = dnn_superres.DnnSuperResImpl_create()
        sr.readModel("Packages/Model/EDSR_x3.pb")
        sr.setModel("edsr", 3)
        new_image_paths = []


        scale_factor = round(scale_factor, 2)

        for image_path in image_paths:
            try:
                image = cv2.imread(image_path)
                if image is None:
                    print(f"Failed to read image: {image_path}")
                    continue

                upscaled_image = upscale_image(sr, image)

                new_width = ceil(upscaled_image.shape[1] * (scale_factor / 3))
                new_height_scaled = ceil(upscaled_image.shape[0] * (scale_factor / 3))

                resized_image = method.interpolation_image(upscaled_image, new_width, new_height_scaled)

                original_colors = extract_original_colors(image, n_colors)

                final_image = method.apply_kd_tree_to_image(resized_image, original_colors)

                final_image = method.fix_uncolored_pixels(final_image, resized_image, original_colors)

                output_file_name = f"resized_{os.path.basename(image_path)}"
                output_file_path = os.path.join(output_path, output_file_name)
                cv2.imwrite(output_file_path, final_image)

                new_image_paths.append(output_file_path)
            except Exception as e:
                print(f"Error processing image {image_path}: {str(e)}")

        return new_image_paths


