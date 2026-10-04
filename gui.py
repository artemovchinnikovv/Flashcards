import sys
import time
from random_def_ans import random_def_ans
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QLineEdit, QVBoxLayout
from PySide6.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flashcards")
        self.resize(600, 400)
        # properties of a window

        self.wordnumbermax = 3
        self.definition, self.answer = random_def_ans(self.wordnumbermax)
        self.wordnumber = 0
        self.attempt = 0
        self.attemptmax = 3

        self.label = QLabel()
        self.label.setText(self.definition[self.wordnumber])
        # create a label where definition will be written self.label

        self.input = QLineEdit()
        self.input.setPlaceholderText("Press Enter")
        # create an input line where user answer will be written self.input

        self.layout = QVBoxLayout()
        self.layout.addStretch()
        self.layout.addWidget(self.label, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.input, alignment = Qt.AlignCenter)
        self.layout.addStretch()
        # create a spreedsheet for input and label to look correctly

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        # widget gets a layout and displayed

        self.input.returnPressed.connect(self.enter_pressed)
        # enter triggers check of a word (but firstly it will just start a program)

    def enter_pressed(self):
        if self.answer[self.wordnumber] == self.input.text():
            self.correct_answer()
        else:
            self.wrong_answer()

    def correct_answer(self):
        self.label.setText("You are right!")
        QTimer.singleShot(1000, self.to_next_word)

    def wrong_answer(self):
        self.label.setText("Wrong")
        QTimer.singleShot(1000, self.to_next_word)

    def to_next_word(self):
        self.wordnumber = self.wordnumber + 1
        if self.wordnumber >= self.wordnumbermax:
            app.quit()
            return
        self.label.setText(self.definition[self.wordnumber])

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())