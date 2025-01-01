import sys
from PyQt5.QtWidgets import QApplication
from Packages.DesignGUI import CombinedFrameCreator

def main():
    app = QApplication(sys.argv)
    ex = CombinedFrameCreator()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


