from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys
import pymysql
import bcrypt

def connect_to_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="inventory_app",
        cursorclass=pymysql.cursors.DictCursor
    )

class LoginApp:
    def __init__(self):
        loader = QUiLoader()
        file = QFile("ui/login.ui")
        file.open(QFile.ReadOnly)
        self.window = loader.load(file)
        file.close()
        self.window.loginButton.clicked.connect(self.handle_login)

    def handle_login(self):
        role = self.window.roleComboBox.currentText()
        username = self.window.usernameLineEdit.text()
        password = self.window.passwordLineEdit.text()

        try:
            db = connect_to_db()
            with db.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE username=%s AND role=%s", (username, role))
                user = cursor.fetchone()
                if user and bcrypt.checkpw(password.encode(), user["password_hash"].encode()):
                    QMessageBox.information(self.window, "Success", f"Logged in as {role}")
                else:
                    QMessageBox.warning(self.window, "Error", "Invalid credentials")
        except Exception as e:
            QMessageBox.critical(self.window, "Database Error", str(e))

    def run(self):
        self.window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginApp()
    login.run()
    sys.exit(app.exec())
