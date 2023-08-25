from PyQt6 import QtCore, QtWidgets
import sqlite3

conn = sqlite3.connect('db/user_database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                login TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL)''')
conn.commit()
conn.close()
class Ui_Addwindow(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 180)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 49, 22))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 180, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 80, 180, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(115, 130, 70, 24))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 49, 22))
        self.label_2.setObjectName("label_2")

        self.pushButton.clicked.connect(lambda: self.emailsearch())
        self.pushButton.clicked.connect(lambda: self.show_line())
        self.pushButton.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def emailsearch(self):
        email = self.lineEdit.text()
        posdog = email.find("@")
        email = email[posdog+1:]
        posdot = email.find(".")
        if email[:posdot] == "mail" or "gmail" or "yahoo" or "outlook" or "hotmail":
            lett = "imap." + email
            return lett
    def show_line(self):
        login = self.lineEdit.text()
        email = self.emailsearch()
        password = self.lineEdit_2.text()

        try:
            conn = sqlite3.connect('db/user_database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (login, email, password) VALUES (?, ?, ?)",
                           (login, email, password))
            conn.commit()
            conn.close()
        except sqlite3.Error as error:
            return error

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавьте аккаунт"))
        self.label.setText(_translate("Form", "Логин:"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.label_2.setText(_translate("Form", "Пароль:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Addwindow = QtWidgets.QWidget()
    ui = Ui_Addwindow()
    ui.setupUi(Addwindow)
    Addwindow.show()
    sys.exit(app.exec())
