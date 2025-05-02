import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import QTimer

class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Работа с QLabel и QTimer")
        self.resize(300, 100)

        self.layout = QVBoxLayout()

        self.label = QLabel('Текст до таймера', self)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

        QTimer.singleShot(2000, self.change_text)

    def change_text(self):
        self.label.setText("Текст после таймера!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Timer()
    window.show()
    sys.exit(app.exec())
