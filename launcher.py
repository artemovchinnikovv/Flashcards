from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QHBoxLayout, QWidget, QLineEdit
from PySide6.QtCore import Qt, QTimer, QCoreApplication
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication
import sys
from gui import MainWindow

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
        self.button_rand.setFont(self.font)
        self.button_mist.setFont(self.font)
        self.button_rand.setFixedSize(140, 40)
        self.button_mist.setFixedSize(140, 40)
        self.button_rand.setCheckable(True)
        self.button_mist.setCheckable(True)

        self.layout_h = QHBoxLayout()
        self.layout_h.addStretch()
        self.layout_h.addWidget(self.button_rand)
        self.layout_h.addWidget(self.button_mist)
        self.layout_h.addStretch()

        self.input = QLineEdit()
        self.input.setFont(self.font)
        self.input.setPlaceholderText("Enter number of questions")

        self.button_start = QPushButton("Start")
        self.button_start.setFont(self.font)
        self.button_rand.setFixedSize(140, 40)

        self.layout_v = QVBoxLayout()
        self.layout_v.addStretch()
        self.layout_v.addLayout(self.layout_h)
        self.layout_v.addWidget(self.input, alignment = Qt.AlignCenter)
        self.layout_v.addWidget(self.button_start, alignment = Qt.AlignCenter)
        self.layout_v.addStretch()

        self.widget = QWidget()
        self.widget.setLayout(self.layout_v)
        self.setCentralWidget(self.widget)

        self.wordnumbermax = 0
        self.rand_or_mist = ""

        self.button_rand.clicked.connect(self.button_rand_click)
        self.button_mist.clicked.connect(self.button_mist_click)
        self.input.textChanged.connect(self.input_changed)
        self.button_start.clicked.connect(self.button_start_click)

    def input_changed(self):
        self.wordnumbermax = int (self.input.text())

    def button_start_click(self):
        self.close()
        print (self.wordnumbermax)
        window = MainWindow(self.wordnumbermax, self.rand_or_mist)
        window.show()
        sys.exit(app.exec())
        return

    def input_enter_pressed(self):
        self.wordnumbermax = int (self.input.text())

    def button_rand_click(self):
        self.rand_or_mist = "Random"

    def button_mist_click(self):
        self.rand_or_mist = "Mistakes"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Launcher()
    window.show()
    sys.exit(app.exec())