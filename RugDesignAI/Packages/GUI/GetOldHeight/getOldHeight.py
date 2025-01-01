from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class HeightInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enter Old Height")

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Please enter the old height:")
        self.layout.addWidget(self.label)

        self.old_height_input = QLineEdit(self)
        self.layout.addWidget(self.old_height_input)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)  # Close the dialog when clicked
        self.layout.addWidget(self.ok_button)

        self.setLayout(self.layout)

    def get_old_height(self):
        return self.old_height_input.text()  # Return the input height
