"""
QLineEdit
"""

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Поле ввода")
#         self.setGeometry(100, 100, 300, 200)
#
#         self.input = QLineEdit(self)
#         self.input.move(50, 50)
#
#         self.label = QLabel("Введите что-нибудь", self)
#         self.label.move(50, 90)
#
#         self.input.textChanged.connect(self.text_changed)
#
#     def text_changed(self,text):
#         self.label.setText(f"Вы ввели: {text}")
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())


"""
Текстовая область
"""

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Текстовая область")
#         self.setGeometry(100, 100, 400, 300)
#
#         self.text_edit = QTextEdit(self)
#         self.text_edit.move(50, 50)
#         self.text_edit.resize(300, 200)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())


"""
QCheckBox
"""

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QCheckBox
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QCheckBox")
#         self.setGeometry(100, 100, 300, 200)
#
#         self.checkbox = QCheckBox("Я согласна", self)
#         self.checkbox.move(50, 50)
#
#         self.label = QLabel("",self)
#         self.label.move(50, 100)
#         self.label.setWordWrap(True)
#         self.label.resize(200,50)
#
#         self.checkbox.stateChanged.connect(self.checkbox_changed)
#
#     def checkbox_changed(self, state):
#         if state == 2:                  #0 = No, 2 = Yes in PyQt
#             self.label.setText("Вы согласились")
#         else:
#             self.label.setText("Вы не согласились")
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = MainWindow()
#     main.show()
#     sys.exit(app.exec())

"""
Радио кнопкa - QRadioButton
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QRadioButton
from PyQt6.QtGui import QIcon    #icon for widget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRadioButton")
        self.setGeometry(100, 100, 300, 200)

        self.setWindowIcon(QIcon("icon.ico"))    #name of the icon for widget
        self.radio1 = QRadioButton("Вариант 1", self)
        self.radio1.move(50,50)
        self.radio2 = QRadioButton("Вариант 2", self)
        self.radio2.move(50,80)

        self.label = QLabel("",self)
        self.label.move(50,120)
        self.label.setWordWrap(True)

        self.radio1.toggled.connect(self.radio_changed)
        self.radio2.toggled.connect(self.radio_changed)

    def radio_changed(self):
        if self.radio1.isChecked():
            self.label.setText("Выбран вариант 1")
        elif self.radio2.isChecked():
            self.label.setText("Выбран вариант 2")
        self.label.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec())
