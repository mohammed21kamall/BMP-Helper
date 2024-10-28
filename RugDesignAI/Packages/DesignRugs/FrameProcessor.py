from Packages.Phase1.horizontal_boundries import MergingPatternHorizontal
from Packages.Phase2.vertical_boundries import MergingPatternVertical
from Packages.Common.SizeWhiteSpace import SizeWhiteSpace
from Packages.Phase3.CombineClass import CombineClass
from Packages.Common.MargeFrame import MergeType
from Packages.Common.Repeats import Repeat
import cv2


class FrameProcessor:
    @staticmethod
    def MakeFirstFrame(horizontal_image_path, vertical_image_path, corner_image_path, width, height, output_horizontal,
                       output_vertical, final_output, final_merged_output):
        # Step 1: Create repeated horizontal image
        image_path_horizontal = cv2.imread(horizontal_image_path)
        corner_path_horizontal = cv2.imread(corner_image_path)
        image_width = image_path_horizontal.shape[1]
        corner_width = corner_path_horizontal.shape[1]
        num_repeats_horizontal = (width - (corner_width * 2)) // image_width

        MergingPattern_Horizontal = MergingPatternHorizontal()
        MergingPattern_Horizontal.create_repeated_image_with_horizontal(horizontal_image_path, output_horizontal, num_repeats_horizontal)

        # Step 2: Create repeated vertical image
        image_path_vertical = cv2.imread(vertical_image_path)
        corner_path_vertical = cv2.imread(corner_image_path)
        image_height = image_path_vertical.shape[0]
        corner_height = corner_path_vertical.shape[0]
        half_height = height // 2
        num_repeats_vertical = ((half_height - corner_height) // image_height)

        MergingPattern_Vertical = MergingPatternVertical()
        MergingPattern_Vertical.create_repeated_image_with_vertical(vertical_image_path, output_vertical, num_repeats_vertical)

        combine = CombineClass()
        combine.combine_images(corner_image_path, output_horizontal, output_vertical, final_output)

        MergeType.merge_with_matched_rows(final_output, final_merged_output)

    @staticmethod
    def MakeFrames(base_image_path, horizontal_image_path, vertical_image_path, corner_image_path,
                   output_horizontal, output_vertical, final_output, final_merged_output, pattern_path=None,
                   horizontal_option='Horizontal Normal', vertical_option='Vertical Normal', merge_option='Merge with Matched Rows'):

        # Get white space dimensions
        Size_White_Space = SizeWhiteSpace()
        white_height, white_width = Size_White_Space.getHeightAndWidthWhiteArea(base_image_path)

        # Process horizontal image
        Repeat_Pattern = Repeat()
        horizontal_image = cv2.imread(horizontal_image_path)
        corner_image = cv2.imread(corner_image_path)
        image_width = horizontal_image.shape[1]
        corner_width = corner_image.shape[1]
        num_repeats_horizontal = Repeat_Pattern.calc_repeats_width(white_width, corner_width, image_width)

        MergingPattern_Horizontal = MergingPatternHorizontal()
        if horizontal_option == 'Horizontal with Flip':
            MergingPattern_Horizontal.create_repeated_image_with_horizontal_flip(horizontal_image_path, output_horizontal, num_repeats_horizontal)
        else:
            MergingPattern_Horizontal.create_repeated_image_with_horizontal(horizontal_image_path, output_horizontal, num_repeats_horizontal)

        # Process vertical image
        vertical_image = cv2.imread(vertical_image_path)
        image_height = vertical_image.shape[0]
        corner_height = corner_image.shape[0]
        num_repeats_vertical = Repeat_Pattern.calc_repeats_height(white_height, corner_height, image_height)

        MergingPattern_Vertical = MergingPatternVertical()
        if vertical_option == 'Vertical with Flip':
            MergingPattern_Vertical.create_repeated_image_with_vertical_flip(vertical_image_path, output_vertical, num_repeats_vertical)
        else:
            MergingPattern_Vertical.create_repeated_image_with_vertical(vertical_image_path, output_vertical, num_repeats_vertical)

        # Combine images
        Combine_Class = CombineClass()

        Combine_Class.combine_images(corner_image_path, output_horizontal, output_vertical, final_output)

        Merge_Type = MergeType()
        # Merge final image
        if merge_option == 'Merge with Matched Rows':
            Merge_Type.merge_with_matched_rows(final_output, final_merged_output)
        elif merge_option == 'Merge with Left and Right Patterns':
            if pattern_path is None:
                raise ValueError("Pattern path is required for left_right_patterns merge option")
            Merge_Type.merge_with_left_right_patterns(final_output, pattern_path, final_merged_output)
        else:
            raise ValueError("Invalid merge option")

