from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QPushButton, QLabel, QVBoxLayout)

from random import randint

app = QApplication([])

main_window = QWidget()
main_window.setWindowTitle("Generator Number!")
main_window.resize(700,500)

lbl_title = QLabel("Dont Press the button PLIS!!")
lbl_result = QLabel("???")
btn_generate = QPushButton("Button")
#tata letak
layout_main = QVBoxLayout()
layout_main.addWidget(lbl_title, alignment=Qt.AlignmentFlag.AlignCenter)
layout_main.addWidget(lbl_result, alignment=Qt.AlignmentFlag.AlignCenter)
layout_main.addWidget(btn_generate, alignment=Qt.AlignmentFlag.AlignCenter)

def random_number():
    number = randint(1,9)
    lbl_result.setText(str(number))

btn_generate.clicked.connect(random_number)


main_window.setLayout(layout_main)
main_window.show()
app.exec_()