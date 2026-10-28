from gui import MainWindow
from PySide6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = MainWindow(5, "Mistakes")
window.show()
sys.exit(app.exec())