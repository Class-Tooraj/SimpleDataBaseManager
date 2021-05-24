__author__ = "Tooraj_Jahangiri"
__email__ = "toorajjahangiri@gmail.com"


# IMPORT
import sys

# IMPORT MAIN WINDOW
from gui.mainwindow_wi import MainWindow

# IMPORT GUI CORE
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    try:
        APP = QApplication(sys.argv)
        WIN = MainWindow()
        WIN.show()
        sys.exit(APP.exec_())
    except Exception as e:
        print(f"ERR >> /{e}/\n{type(e).__name__}")