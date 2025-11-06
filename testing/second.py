from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QPushButton, QLabel, QVBoxLayout, 
    QMessageBox, QRadioButton, QHBoxLayout)

from random import randint

app = QApplication([])

main_window = QWidget()
main_window.setWindowTitle("Quiz App!")
main_window.resize(700, 200)

lbl_question = QLabel("Kapan Indonesia Merdeka?")

rbtn_answer1 = QRadioButton("1945")
rbtn_answer2 = QRadioButton("1949")
rbtn_answer3 = QRadioButton("1944")
rbtn_answer4 = QRadioButton("1947")

layout_row1 = QHBoxLayout()
layout_row1.addWidget(rbtn_answer1, alignment = Qt.AlignmentFlag.AlignCenter)
layout_row1.addWidget(rbtn_answer2, alignment = Qt.AlignmentFlag.AlignCenter)

layout_row2 = QHBoxLayout()
layout_row2.addWidget(rbtn_answer3, alignment = Qt.AlignmentFlag.AlignCenter)
layout_row2.addWidget(rbtn_answer4, alignment = Qt.AlignmentFlag.AlignCenter)

layout_main = QVBoxLayout()
layout_main.addWidget(lbl_question, alignment = Qt.AlignmentFlag.AlignCenter)
layout_main.addLayout(layout_row1)
layout_main.addLayout(layout_row2)

#Button Functionality
def answer_true():
    victory_win = QMessageBox()
    victory_win.setText("Jawaban Benarr!!!")
    victory_win.exec_()

def answer_false():
    lose_win = QMessageBox()
    lose_win.setText("Jawaban Salahhh!!!")
    lose_win.exec_()

rbtn_answer1.clicked.connect(answer_true)
rbtn_answer2.clicked.connect(answer_false)
rbtn_answer3.clicked.connect(answer_false)
rbtn_answer4.clicked.connect(answer_false)

main_window.setLayout(layout_main)
main_window.show()
app.exec_()