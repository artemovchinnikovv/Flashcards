from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QHBoxLayout, QWidget
from PySide6.QtCore import Qt, QTimer, QCoreApplication
from PySide6.QtGui import QFont

class Launcher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Launcher")
        self.resize(600, 400)
        # properties of a window

        self.font = QFont()
        self.font.setPointSize(20)

        self.button_rand = QPushButton("Random")
        self.button_mist = QPushButton("Mistakes")
        self.button_rand.setFixedSize(140, 40)
        self.button_mist.setFixedSize(140, 40)

        self.layout_h = QHBoxLayout()
        self.layout_h.addStretch()
        self.layout_h.addWidget(self.button_rand)
        self.layout_h.addWidget(self.button_mist)
        self.layout_h.addStretch()

        self.layout_v = QVBoxLayout()
        self.layout_v.addStretch()
        self.layout_v.addLayout(self.layout_h)
        self.layout_v.addStretch()

        self.widget = QWidget()
        self.widget.setLayout(self.layout_v)
        self.setCentralWidget(self.widget)

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    window = Launcher()
    window.show()
    sys.exit(app.exec())