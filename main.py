from launcher import Launcher
from PySide6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = Launcher()
window.show()
sys.exit(app.exec())