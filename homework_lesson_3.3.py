import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout
from PyQt6.QtGui import QIcon

class MyButton(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyButton")
        self.setGeometry(100, 100, 300, 200)

        self.setWindowIcon(QIcon("panic-button.ico"))

        self.radio1 = QRadioButton("Red", self)
        self.radio2 = QRadioButton("Green", self)
        self.radio3 = QRadioButton("Blue", self)

        self.label = QLabel("", self)
        self.label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.radio1.toggled.connect(self.radio_changed)
        self.radio2.toggled.connect(self.radio_changed)
        self.radio3.toggled.connect(self.radio_changed)

    def radio_changed(self):
        if self.radio1.isChecked():
            self.label.setText("You chose Red!")
        elif self.radio2.isChecked():
            self.label.setText("You chose Green!")
        elif self.radio3.isChecked():
            self.label.setText("You chose Blue!")
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyButton()
    main.show()
    sys.exit(app.exec())
