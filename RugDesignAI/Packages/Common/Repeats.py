from math import ceil, floor

class Repeat:
    @staticmethod
    def calc_repeats_width(width, corner_width, image_width):
        num_repeats = (width - (corner_width * 2)) / image_width
        fractional_part = num_repeats - int(num_repeats)
        # Apply the conditional logic
        if fractional_part >= 0.5:
            num_repeats = ceil(num_repeats)
        else:
            num_repeats = floor(num_repeats)
        return num_repeats

    @staticmethod
    def calc_repeats_height(white_height, corner_height, pattern_height):
        num_repeats = (((white_height / 2) - (corner_height)) / pattern_height)

        # Extract the fractional part of the number
        fractional_part = num_repeats - int(num_repeats)

        # Apply the conditional logic
        if fractional_part >= 0.5:
            num_repeats = ceil(num_repeats)
        else:
            num_repeats = floor(num_repeats)
        return num_repeats
