from Packages.InsertFrameToCreateTheRag.InsertTheFrameWithBaseFrame import RugDesign
from Packages.DesignRugs.FrameProcessor import FrameProcessor
from PyQt5.QtWidgets import QMessageBox
from random import randint

class ProcessUI:
    def __init__(self, classUI):
        self.class_UI = classUI
    def process_first_frame(self):
        try:
            Frame_Processor = FrameProcessor()
            horizontal_image_path = self.class_UI.horizontal_image_input.text()
            vertical_image_path = self.class_UI.vertical_image_input.text()
            corner_image_path = self.class_UI.corner_image_input.text()
            width = self.class_UI.width_input.value()
            height = self.class_UI.height_input.value()
            output_folder = self.class_UI.output_path_input.text()
            num = randint(0, 10000)
            output_horizontal = f"{output_folder}/Horizontal/horizontal{num}.bmp"
            output_vertical = f"{output_folder}/Vertical/vertical{num}.bmp"
            final_output = f"{output_folder}/U/U{num}.bmp"
            final_merged_output = f"{output_folder}/Design/Design{num}.bmp"
            Frame_Processor.MakeFirstFrame(horizontal_image_path, vertical_image_path, corner_image_path, width, height,
                                           output_horizontal, output_vertical, final_output, final_merged_output)


            self.class_UI.base_image_input.setText(final_merged_output)
            QMessageBox.information(self.class_UI, "Success", "Frame processed successfully!")
            return final_merged_output
        except Exception as e:
            QMessageBox.critical(self.class_UI, "Error", str(e))
    def process_make_frame(self):
        try:

            base_image_path = self.class_UI.base_image_input.text()
            horizontal_image_path = self.class_UI.make_horizontal_image_input.text()
            vertical_image_path = self.class_UI.make_vertical_image_input.text()
            corner_image_path = self.class_UI.make_corner_image_input.text()
            output_folder = self.class_UI.make_output_path_input.text()
            pattern_path = self.class_UI.pattern_path_input.text()

            horizontal_option = self.class_UI.horizontal_option_combo.currentText()
            vertical_option = self.class_UI.vertical_option_combo.currentText()
            merge_option = self.class_UI.merge_option_combo.currentText()

            num = randint(0, 10000)
            output_horizontal = f"{output_folder}/Horizontal/horizontal{num}.bmp"
            output_vertical = f"{output_folder}/Vertical/vertical{num}.bmp"
            final_output = f"{output_folder}/U/U{num}.bmp"
            final_merged_output = f"{output_folder}/Design/Design{num}.bmp"

            Frame_Processor = FrameProcessor()
            Frame_Processor.MakeFrames(base_image_path, horizontal_image_path, vertical_image_path, corner_image_path,
                                       output_horizontal, output_vertical, final_output, final_merged_output, pattern_path
                                       , horizontal_option, vertical_option, merge_option)
            self.class_UI.base_image_input.setText(final_merged_output)
            QMessageBox.information(self.class_UI, "Success", "Frame processed successfully!")
            return final_merged_output

        except Exception as e:
            QMessageBox.critical(self.class_UI, "Error", str(e))

    def process_both_frames(self):
        try:
            Merged_Frames = RugDesign()
            if not hasattr(self, 'is_first_frame_processed'):
                self.is_first_frame_processed = False
            if not hasattr(self, 'is_second_frame_processed'):
                self.is_second_frame_processed = False

            if not self.is_first_frame_processed:
                first_frame_output = self.process_first_frame()
                self.is_first_frame_processed = True


                Merged_Frames.MergedTheFrames(
                    first_frame_output,
                    self.process_make_frame(),
                    f"{self.class_UI.output_path_input.text()}/Design/The Design.bmp"
                )
            else:
                next_frame_output = self.process_make_frame()
                self.is_second_frame_processed = True

                Merged_Frames.MergedTheFrames(
                    f"{self.class_UI.output_path_input.text()}/Design/The Design.bmp",
                    next_frame_output,
                    f"{self.class_UI.output_path_input.text()}/Design/The Design.bmp"
                )

            QMessageBox.information(self.class_UI, "Success", "Frames processed successfully!")

        except Exception as e:
            QMessageBox.critical(self.class_UI, "Error", str(e))

