from email.mime import application
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

application = QApplication([])

mainwindow = QMainWindow()
mainwindow.setGeometry(300,100,400,400)


button_print = QPushButton(mainwindow)
button_print.setGeometry(60,250,100,50)
button_print.setText("PRINT")

button_clear = QPushButton(mainwindow)
button_clear.setGeometry(235,250,100,50)
button_clear.setText("CLEAR")


line_box = QLineEdit(mainwindow)
line_box.setGeometry(145,150,100,25)

label_box=QLabel(mainwindow)
label_box.setGeometry(175,50,100,25)