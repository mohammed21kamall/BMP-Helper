from PyQt5.QtWidgets import QFileDialog

class BrowseMethod:
    def __init__(self, classUI):
        self.class_UI = classUI

    def browse_horizontal_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self.class_UI, "Select Horizontal Image", "",
                                                   "Image Files (*.bmp *.png *.jpg)")
        if file_name:
            self.class_UI.horizontal_image_input.setText(file_name)

    def browse_base_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self.class_UI, "Select Base Image", "",
                                                   "Images (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        if file_name:
            self.class_UI.base_image_input.setText(file_name)

    def browse_vertical_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self.class_UI, "Select Vertical Image", "", "Image Files (*.bmp *.png *.jpg)")
        if file_name:
            self.class_UI.vertical_image_input.setText(file_name)

    def browse_corner_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self.class_UI, "Select Corner Image", "", "Image Files (*.bmp *.png *.jpg)")
        if file_name:
            self.class_UI.corner_image_input.setText(file_name)

    def browse_output_path(self):
        folder = QFileDialog.getExistingDirectory(self.class_UI, "Select Output Folder")
        if folder:
            self.class_UI.output_path_input.setText(folder)

    def browse_make_horizontal_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self.class_UI, "Select Horizontal Image", "",
                                                   "Image Files (*.bmp *.png *.jpg)")
        if file_name:
            self.class_UI.make_horizontal_image_input.setText(file_name)

    def browse_make_vertical_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self.class_UI, "Select Vertical Image", "", "Image Files (*.bmp *.png *.jpg)")
        if file_name:
            self.class_UI.make_vertical_image_input.setText(file_name)

    def browse_make_corner_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self.class_UI, "Select Corner Image", "", "Image Files (*.bmp *.png *.jpg)")
        if file_name:
            self.class_UI.make_corner_image_input.setText(file_name)

    def browse_pattern_path(self):
        file_name, _ = QFileDialog.getOpenFileName(self.class_UI, "Select Pattern Image", "", "Image Files (*.bmp *.png *.jpg)")
        if file_name:
            self.class_UI.pattern_path_input.setText(file_name)

    def browse_make_output_path(self):
        folder = QFileDialog.getExistingDirectory(self.class_UI, "Select Output Folder")
        if folder:
            self.class_UI.make_output_path_input.setText(folder)
