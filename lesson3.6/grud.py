import sys
from PyQt6.QtWidgets import(
    QApplication, QWidget, QPushButton, QVBoxLayout,
QHBoxLayout,QLineEdit, QLabel, QMessageBox, QTextEdit, QInputDialog
)
import crud_alt

class UserApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('User CRUD PyQt6')
        self.setGeometry(100, 100, 600,450)

        crud_alt.create_table()

        self.layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.email_input = QLineEdit()
        self.phone_input = QLineEdit()

        self.layout.addWidget(QLabel('Name:'))
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(QLabel('Age:'))
        self.layout.addWidget(self.age_input)
        self.layout.addWidget(QLabel('Email:'))
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(QLabel('Phone:'))
        self.layout.addWidget(self.phone_input)

        btn_layout = QHBoxLayout()

        self.add_btn = QPushButton('Add')
        self.update_btn = QPushButton('Update by ID')
        self.list_btn = QPushButton('Show list')
        self.find_btn = QPushButton('Find')
        self.delete_btn = QPushButton('Delete by ID')

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.update_btn)
        btn_layout.addWidget(self.list_btn)
        btn_layout.addWidget(self.find_btn)
        btn_layout.addWidget(self.delete_btn)

        self.setLayout(self.layout)

        self.add_btn.clicked.connect(self.add_user)
        self.update_btn.clicked.connect(self.update_user)
        self.list_btn.clicked.connect(self.show_users)
        self.find_btn.clicked.connect(self.find_user)
        self.delete_btn.clicked.connect(self.delete_user)

    def add_user(self):
        name = self.name_input.text()
        age = self.age_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()

        if not name or not age:
            QMessageBox.warning(self, 'Error', 'Name and Age are required')
            return
        try:
            conn = crud_alt.connect_db()
            conn.execute("INSERT INTO users (name, age, email, phone) VALUES (?, ?, ?, ?)",
                         (name, age, email, phone))
            conn.commit()
            conn.close()
            self.output.append(f"[+] Added: {name}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def update_user(self):
        user_id, ok = QInputDialog.getInt(self, "Update", "Enter User ID")
        if ok:
            name = self.name_input.text()
            age = self.age_input.text()
            email = self.email_input.text()
            phone = self.phone_input.text()

            if not name or not age:
                QMessageBox.warning(self, 'Error', 'Name and Age are required')
                return

            count = crud_alt.update_user(user_id, name, age, email, phone)
            if count:
                self.output.append(f'[Update] User ID = {user_id} is updated successfully')

            else:
                self.output.append("[!] User is not found")

    def show_users(self):
        conn = crud_alt.connect_db()
        users = conn.execute("SELECT * FROM users").fetchall()
        self.output.clear()
        for u in users:
            self.output.append(f"{u[0]} | {u[1]} | {u[2]} | {u[3]} | {u[4]}")
        conn.close()

    # def find_user(self):