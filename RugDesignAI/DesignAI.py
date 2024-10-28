from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QGroupBox, QFormLayout, QLineEdit, \
    QPushButton, QLabel, QSpinBox, QComboBox, QHBoxLayout, QApplication, QTableWidget, \
    QTableWidgetItem, QCheckBox
from Packages.BrowseMethod.BrowseMethod import BrowseMethod
from Packages.ProcessorsGUI.ResizingFrameProcessor import ResizedProcessUI
from Packages.CreateFolders.CreateFolders import CreateFolder
from Packages.ProcessorsGUI.ProcessUI import ProcessUI
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys


class CombinedFrameCreator(QWidget):
    def __init__(self):
        super().__init__()
        self.Create_Folder = CreateFolder()
        self.main_folder_path = self.create_folders()
        self.Resized_Process = ResizedProcessUI(self)
        self.Browse = BrowseMethod(self)
        self.process = ProcessUI(self)
        self.initUI()


    def initUI(self):
        main_layout = QVBoxLayout()

        tabs = QTabWidget()
        first_frame_tab = QWidget()
        make_frame_tab = QWidget()

        tabs.addTab(make_frame_tab, "Create Frames")
        tabs.addTab(first_frame_tab, "Create Black Frame")

        self.setup_first_frame_tab(first_frame_tab)
        self.setup_make_frame_tab(make_frame_tab)

        main_layout.addWidget(tabs)

        # Add the Make Frames button
        self.reset_button = QPushButton('Process Both Frames')
        self.reset_button.clicked.connect(self.process_make_frame_button_FN)
        main_layout.addWidget(self.reset_button)

        # Add the reset button
        self.reset_button = QPushButton('Reset')
        self.reset_button.clicked.connect(self.reset)
        main_layout.addWidget(self.reset_button)

        self.setLayout(main_layout)
        self.setWindowTitle('Design AI Tool')
        self.setWindowIcon(QIcon('Packages/Icons/Web_Design-1024.webp'))
        self.setGeometry(300, 100, 700, 500)

    def setup_first_frame_tab(self, tab):
        layout = QVBoxLayout()

        image_group = QGroupBox("Image Paths")
        size_group = QGroupBox("Frame Size")
        output_group = QGroupBox("Output")

        image_layout = QFormLayout()
        self.horizontal_image_input = QLineEdit()
        self.vertical_image_input = QLineEdit()
        self.corner_image_input = QLineEdit()

        image_layout.addRow(QLabel("Horizontal Image:"), self.create_browse_row(self.horizontal_image_input,
                                                                                self.Browse.browse_horizontal_image))
        image_layout.addRow(QLabel("Vertical Image:"), self.create_browse_row(self.vertical_image_input,
                                                                              self.Browse.browse_vertical_image))
        image_layout.addRow(QLabel("Corner Image:"), self.create_browse_row(self.corner_image_input,
                                                                            self.Browse.browse_corner_image))

        image_group.setLayout(image_layout)

        size_layout = QFormLayout()
        self.width_input = QSpinBox()
        self.height_input = QSpinBox()

        # Disable manual input
        self.width_input.setReadOnly(True)
        self.height_input.setReadOnly(True)

        self.width_input.setRange(1, 10000)
        self.height_input.setRange(1, 10000)
        size_group.setLayout(size_layout)

        output_layout = QFormLayout()
        self.output_path_input = QLineEdit()
        output_layout.addRow(QLabel("Output Path:"), self.create_browse_row(self.output_path_input,
                                                                            self.Browse.browse_output_path))
        output_group.setLayout(output_layout)
        process_first_frame = QPushButton('Process First Frame')
        process_first_frame.clicked.connect(self.process.process_first_frame)

        layout.addWidget(image_group)
        layout.addWidget(output_group)
        layout.addWidget(process_first_frame)
        layout.addStretch()

        tab.setLayout(layout)

        self.output_path_input.setText(self.main_folder_path)

    def setup_make_frame_tab(self, tab):
        layout = QVBoxLayout()

        image_group = QGroupBox("Image Paths")
        options_group = QGroupBox("Options")
        output_group = QGroupBox("Output")

        image_layout = QFormLayout()

        self.base_image_input = QLineEdit()
        self.make_horizontal_image_input = QLineEdit()
        self.make_vertical_image_input = QLineEdit()
        self.make_corner_image_input = QLineEdit()
        self.pattern_path_input = QLineEdit()

        image_layout.addRow(QLabel("Base Image:"), self.create_browse_row(self.base_image_input,
                                                                          self.Browse.browse_base_image))
        image_layout.addRow(QLabel("Horizontal Image:"), self.create_browse_row(self.make_horizontal_image_input,
                                                                                self.Browse.browse_make_horizontal_image))
        image_layout.addRow(QLabel("Vertical Image:"), self.create_browse_row(self.make_vertical_image_input,
                                                                              self.Browse.browse_make_vertical_image))
        image_layout.addRow(QLabel("Corner Image:"), self.create_browse_row(self.make_corner_image_input,
                                                                            self.Browse.browse_make_corner_image))
        self.pattern_label = QLabel("Pattern Image:")
        self.pattern_browse_row = self.create_browse_row(self.pattern_path_input, self.Browse.browse_pattern_path)
        image_layout.addRow(self.pattern_label, self.pattern_browse_row)

        image_group.setLayout(image_layout)

        options_layout = QFormLayout()
        self.horizontal_option_combo = QComboBox()
        self.horizontal_option_combo.addItems(['Horizontal Normal', 'Horizontal with Flip'])
        self.vertical_option_combo = QComboBox()
        self.vertical_option_combo.addItems(['Vertical Normal', 'Vertical with Flip'])
        self.merge_option_combo = QComboBox()
        self.merge_option_combo.addItems(['Merge with Matched Rows', 'Merge with Left and Right Patterns'])

        options_layout.addRow("Horizontal Option:", self.horizontal_option_combo)
        options_layout.addRow("Vertical Option:", self.vertical_option_combo)
        options_layout.addRow("Merge Option:", self.merge_option_combo)
        options_group.setLayout(options_layout)

        self.merge_option_combo.currentIndexChanged.connect(self.toggle_pattern_path_visibility)

        output_layout = QFormLayout()
        self.make_output_path_input = QLineEdit()
        output_layout.addRow(QLabel("Output Path:"), self.create_browse_row(self.make_output_path_input,
                                                                            self.Browse.browse_make_output_path))
        output_group.setLayout(output_layout)

        process_make_frame_button = QPushButton('Process Make Frames')
        process_make_frame_button.clicked.connect(self.process.process_make_frame)

        layout.addWidget(image_group)
        layout.addWidget(options_group)
        layout.addWidget(output_group)
        layout.addStretch()
        layout.addWidget(process_make_frame_button)
        layout.addWidget(self.setup_table())


        tab.setLayout(layout)

        self.make_output_path_input.setText(self.main_folder_path)

        self.pattern_label.hide()
        self.pattern_browse_row.itemAt(0).widget().hide()
        self.pattern_browse_row.itemAt(1).widget().hide()

    def create_folders(self):
        main_folder_path = self.Create_Folder.CreateFolders()
        if main_folder_path:
            print(f"Folders created successfully. Main folder path: {main_folder_path}")
        else:
            print("Failed to create folders.")
        return main_folder_path

    def toggle_pattern_path_visibility(self):
        if self.merge_option_combo.currentText() == 'Merge with Left and Right Patterns':
            self.pattern_label.show()
            self.pattern_browse_row.itemAt(0).widget().show()
            self.pattern_browse_row.itemAt(1).widget().show()
        else:
            self.pattern_label.hide()
            self.pattern_browse_row.itemAt(0).widget().hide()
            self.pattern_browse_row.itemAt(1).widget().hide()

    def setup_table(self):
        table_widget = QWidget()
        table_layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setRowCount(3)

        self.table.setHorizontalHeaderLabels(['Height', 'Width', 'Check'])

        items = [
            ('1320', '639'),
            ('1680', '799'),
            ('1950', '959')
        ]

        for row, (width, height) in enumerate(items):
            item_width = QTableWidgetItem(width)
            item_width.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.table.setItem(row, 0, item_width)

            item_height = QTableWidgetItem(height)
            item_height.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.table.setItem(row, 1, item_height)

            checkbox = QCheckBox()
            checkbox.stateChanged.connect(self.update_width_height_from_table)
            self.table.setCellWidget(row, 2, checkbox)

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        table_width = self.table.horizontalHeader().length() + 20
        table_height = self.table.verticalHeader().length() + self.table.horizontalHeader().height() + 20

        self.table.setFixedSize(table_width, table_height)

        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        button_container = QWidget()
        button_layout = QVBoxLayout(button_container)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(0)

        self.print_button = QPushButton('Resize Selected')
        self.print_button.clicked.connect(self.Resized_Process.resize_selected)
        self.print_button.setFixedSize(table_width, 30)

        self.print_button2 = QPushButton('Process Makes')
        self.print_button2.clicked.connect(self.Resized_Process.process_both_frames_with_resize)
        self.print_button2.setFixedSize(table_width, 30)

        button_layout.addWidget(self.print_button)
        button_layout.addWidget(self.print_button2)

        table_layout.addWidget(self.table)
        table_layout.addWidget(button_container)

        table_layout.setSpacing(0)
        table_layout.setContentsMargins(0, 0, 0, 0)

        total_height = table_height + self.print_button.height() + self.print_button2.height()
        table_widget.setFixedSize(table_width, total_height)

        table_widget.setLayout(table_layout)

        return table_widget

    def update_width_height_from_table(self):
        for row in range(self.table.rowCount()):
            checkbox = self.table.cellWidget(row, 2)
            if checkbox and checkbox.isChecked():
                width_item = self.table.item(row, 1)
                height_item = self.table.item(row, 0)
                if width_item and height_item:
                    self.width_input.setValue(int(width_item.text()))
                    self.height_input.setValue(int(height_item.text()))
                    break

    def create_browse_row(self, input_widget, browse_function):
        browse_button = QPushButton('Browse')
        browse_button.clicked.connect(browse_function)

        browse_row = QHBoxLayout()
        browse_row.addWidget(input_widget)
        browse_row.addWidget(browse_button)

        return browse_row


    def process_make_frame_button_FN(self):
        self.process.process_both_frames()

    def reset(self):
        """Reset the GUI to its initial state"""
        # Clear all QLineEdit fields
        for widget in [self.horizontal_image_input, self.vertical_image_input, self.corner_image_input,
                       self.output_path_input, self.base_image_input, self.make_horizontal_image_input,
                       self.make_vertical_image_input, self.make_corner_image_input, self.pattern_path_input,
                       self.make_output_path_input]:
            widget.clear()

        # Reset spin boxes to default values
        self.width_input.setValue(1)
        self.height_input.setValue(1)

        # Reset combo boxes to the first item
        self.horizontal_option_combo.setCurrentIndex(0)
        self.vertical_option_combo.setCurrentIndex(0)
        self.merge_option_combo.setCurrentIndex(0)

        # Hide pattern path components initially
        self.pattern_label.hide()
        self.pattern_browse_row.itemAt(0).widget().hide()
        self.pattern_browse_row.itemAt(1).widget().hide()

        # Clear all checkboxes in the table
        for row in range(self.table.rowCount()):
            checkbox = self.table.cellWidget(row, 2)
            if checkbox:
                checkbox.setChecked(False)

        # Reset the main folder path
        self.main_folder_path = self.create_folders()

        # Set default output paths
        self.output_path_input.setText(self.main_folder_path)
        self.make_output_path_input.setText(self.main_folder_path)
        self.process.is_first_frame_processed = False
        self.process.is_second_frame_processed = False


def main():
    app = QApplication(sys.argv)
    ex = CombinedFrameCreator()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
