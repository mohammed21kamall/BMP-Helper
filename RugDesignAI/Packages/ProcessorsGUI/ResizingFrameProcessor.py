from Packages.InsertFrameToCreateTheRag.InsertTheFrameWithBaseFrame import RugDesign
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QLabel, QDialog
from Packages.DesignRugs.FrameProcessor import FrameProcessor
from Packages.Resize.TypesOfResize import ResizeTool
from Packages.GUI.GetOldHeight.getOldHeight import HeightInputDialog
from PyQt5.QtCore import Qt
from random import randint
import os

class ResizedProcessUI:
    organized_paths = {}

    def __init__(self, classUI):
        self.class_UI = classUI
        self.processed_first_frames = {}
        self.is_first_frame_processed = False

    def process_first_frame(self, width, height):
        try:
            Frame_Processor = FrameProcessor()

            horizontal_image_path = self.class_UI.horizontal_image_input.text()
            vertical_image_path = self.class_UI.vertical_image_input.text()
            corner_image_path = self.class_UI.corner_image_input.text()
            output_folder = self.class_UI.output_path_input.text()

            num = randint(0, 10000)

            output_horizontal = f"{output_folder}/Horizontal/horizontal{num}.bmp"
            output_vertical = f"{output_folder}/Vertical/vertical{num}.bmp"
            final_output = f"{output_folder}/U/U{num}.bmp"
            final_merged_output = f"{output_folder}/Design/Design{num}.bmp"

            Frame_Processor.MakeFirstFrame(horizontal_image_path, vertical_image_path,
                                           corner_image_path, width,
                                           height, output_horizontal,
                                           output_vertical, final_output,
                                           final_merged_output)

            return final_merged_output
        except Exception as e:
            QMessageBox.critical(self.class_UI, "Error", str(e))

    def process_make_frame(self, size_dict):
        try:
            Frame_Processor = FrameProcessor()

            base_image = size_dict["Base"] if size_dict["Base"] else None
            horizontal_image_path = os.path.join(size_dict["Path"], size_dict["Horizontal"])
            vertical_image_path = os.path.join(size_dict["Path"], size_dict["Vertical"])
            corner_image_path = os.path.join(size_dict["Path"], size_dict["Corner"])
            pattern_path = os.path.join(size_dict["Path"], size_dict["Pattern"]) if size_dict["Pattern"] else None

            output_folder = self.class_UI.make_output_path_input.text()
            horizontal_option = self.class_UI.horizontal_option_combo.currentText()
            vertical_option = self.class_UI.vertical_option_combo.currentText()
            merge_option = self.class_UI.merge_option_combo.currentText()

            num = randint(0, 10000)
            output_horizontal = f"{output_folder}/Horizontal/horizontal{num}.bmp"
            output_vertical = f"{output_folder}/Vertical/vertical{num}.bmp"
            final_output = f"{output_folder}/U/U{num}.bmp"
            final_merged_output = f"{output_folder}/Design/Design{num}.bmp"

            Frame_Processor.MakeFrames(base_image, horizontal_image_path,
                                       vertical_image_path, corner_image_path,
                                       output_horizontal, output_vertical,
                                       final_output, final_merged_output,
                                       pattern_path, horizontal_option,
                                       vertical_option, merge_option)

            return final_merged_output
        except Exception as e:
            print(f"Error in process_make_frame: {str(e)}")
            QMessageBox.critical(self.class_UI, "Error", str(e))

    def resize_selected(self):
        try:
            height_input_dialog = HeightInputDialog(self.class_UI)

            if height_input_dialog.exec_() == QDialog.Accepted:
                old_height = height_input_dialog.get_old_height()

                if not old_height.isdigit():
                    QMessageBox.warning(self.class_UI, "Warning", "Please enter a valid old height.")
                    return

                old_height = int(old_height)
                loading_dialog = self.show_loading_page()

                selected_rows = [
                    (int(self.class_UI.table.item(row, 0).text()), int(self.class_UI.table.item(row, 1).text()))
                    for row in range(self.class_UI.table.rowCount())
                    if self.class_UI.table.cellWidget(row, 2).isChecked()
                ]

                if not selected_rows:
                    QMessageBox.warning(self.class_UI, "Warning", "Please select at least one row.")
                    return

                image_paths = [
                    self.class_UI.make_horizontal_image_input.text(),
                    self.class_UI.make_vertical_image_input.text(),
                    self.class_UI.make_corner_image_input.text(),
                ]
                if self.class_UI.merge_option_combo.currentText() == 'Merge with Left and Right Patterns':
                    pattern_path = self.class_UI.pattern_path_input.text()
                    if pattern_path:
                        image_paths.append(pattern_path)

                image_paths = [path for path in image_paths if path]

                resize_tool = ResizeTool()
                output_folder = os.path.join(self.class_UI.make_output_path_input.text(), 'Patterns')
                for height, width in selected_rows:
                    print(f"Processing size: {width}x{height}")
                    directory_name = os.path.join(output_folder, f"{width}x{height}")
                    os.makedirs(directory_name, exist_ok=True)
                    scale = height / old_height

                    # استخدام طرق التحجيم الديناميكية والثابتة
                    new_paths = resize_tool.resizeImagesWithDynamicFactor(image_paths, directory_name, scale) \
                        if scale < 1.4 or scale > 1.5 \
                        else resize_tool.resizeImagesWithStaticFactor(image_paths, directory_name)

                    # تخزين معلومات التصميم في organized_paths
                    self.organized_paths[f"{width}x{height}"] = {
                        "Path": directory_name,
                        "Horizontal": os.path.basename(new_paths[0]) if len(new_paths) > 0 else "",
                        "Vertical": os.path.basename(new_paths[1]) if len(new_paths) > 1 else "",
                        "Corner": os.path.basename(new_paths[2]) if len(new_paths) > 2 else "",
                        "Pattern": os.path.basename(new_paths[3]) if len(new_paths) > 3 else "",
                        "Base": self.organized_paths.get(f"{width}x{height}", {}).get("Base", ""),
                    }

                loading_dialog.accept()
                QMessageBox.information(self.class_UI, "Success", "End Resizing Successfully")
            return self.organized_paths

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            QMessageBox.critical(self.class_UI, "Error", f"An error occurred while resizing images: {str(e)}")
            return None

    def process_both_frames_with_resize(self):
        try:
            Merged_Frames = RugDesign()
            resized_paths_dict = self.organized_paths
            print("Contents of organized_paths:")
            print(resized_paths_dict)

            if not resized_paths_dict:
                QMessageBox.warning(self.class_UI, "Warning", "No resized images found in the organized paths.")
                return

            for size_key, size_dict in resized_paths_dict.items():
                print(f"Processing for size: {size_key}")
                try:
                    width, height = map(int, size_key.split('x'))

                    # تحديث الـ Base هنا بعد التحقق من وجوده
                    if size_key not in self.processed_first_frames:
                        first_frame_output = self.process_first_frame(width, height)
                        if not os.path.exists(first_frame_output):
                            raise FileNotFoundError(f"First frame not found: {first_frame_output}")

                        # تحديث الـ Base
                        resized_paths_dict[size_key]["Base"] = first_frame_output
                        self.processed_first_frames[size_key] = first_frame_output
                        is_first_frame_processed = True
                    else:
                        first_frame_output = self.processed_first_frames[size_key]
                        is_first_frame_processed = False

                    base_image = resized_paths_dict[size_key]["Base"]
                    if not base_image or not os.path.exists(base_image):
                        raise FileNotFoundError(f"Base image not found: {base_image}")

                    # معالجة الإطار التالي
                    next_frame_output = self.process_make_frame(resized_paths_dict[size_key])
                    resized_paths_dict[size_key]["Base"] = next_frame_output  # تحديث الـ Base بعد المعالجة

                    # دمج الإطارات
                    if is_first_frame_processed:
                        Merged_Frames.MergedTheFrames(
                            first_frame_output,
                            next_frame_output,
                            f"{self.class_UI.output_path_input.text()}/Design/The Design_{size_key}.bmp"
                        )
                    else:
                        Merged_Frames.MergedTheFrames(
                            f"{self.class_UI.output_path_input.text()}/Design/The Design_{size_key}.bmp",
                            next_frame_output,
                            f"{self.class_UI.output_path_input.text()}/Design/The Design_{size_key}.bmp"
                        )

                except Exception as e:
                    print(f"Error in process_make_frame for {size_key}: {str(e)}")


            QMessageBox.information(self.class_UI, "Success", "Frames processed for all selected sizes!")

        except Exception as e:
            print(f"Error in process_both_frames_with_resize: {str(e)}")
            QMessageBox.critical(self.class_UI, "Error", f"An error occurred while processing frames: {str(e)}")


    def show_loading_page(self):
        loading_dialog = QDialog(self.class_UI)
        loading_dialog.setWindowTitle("Loading")
        loading_dialog.setModal(True)
        layout = QVBoxLayout()
        label = QLabel("Resizing images, please wait...")
        layout.addWidget(label)
        loading_dialog.setLayout(layout)
        loading_dialog.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        loading_dialog.show()
        return loading_dialog