import sqlite3
from PyQt6 import QtCore, QtWidgets
import os
from add import Ui_Addwindow
import imaplib
import email
import quopri

class Ui_MainWindow(object):
    conn = sqlite3.connect('db/user_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT() FROM users;")
    all_results = cursor.fetchall()
    conn.commit()
    conn.close()

    def openwindowadd(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Addwindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(300, 400)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 49, 301, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.l1 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.l1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.l1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.l1.setObjectName("l1")
        self.verticalLayout.addWidget(self.l1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lchb1 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.lchb1.setObjectName("lchb1")
        self.horizontalLayout.addWidget(self.lchb1)
        self.chb1 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.chb1.setObjectName("chb1")
        self.horizontalLayout.addWidget(self.chb1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.le1 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.le1.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.le1.setText("")
        self.le1.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.le1.setObjectName("le1")
        self.horizontalLayout_4.addWidget(self.le1)
        self.lk1 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.lk1.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lk1.setAcceptDrops(False)
        self.lk1.setText("")
        self.lk1.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.lk1.setObjectName("lk1")
        self.horizontalLayout_4.addWidget(self.lk1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.l2 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.l2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.l2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.l2.setObjectName("l2")
        self.verticalLayout.addWidget(self.l2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lchb2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.lchb2.setObjectName("lchb2")
        self.horizontalLayout_2.addWidget(self.lchb2)
        self.chb2 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.chb2.setObjectName("chb2")
        self.horizontalLayout_2.addWidget(self.chb2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.le2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.le2.setText("")
        self.le2.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.le2.setObjectName("le2")
        self.horizontalLayout_5.addWidget(self.le2)
        self.lk2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.lk2.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lk2.setAcceptDrops(False)
        self.lk2.setText("")
        self.lk2.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.lk2.setObjectName("lk2")
        self.horizontalLayout_5.addWidget(self.lk2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.l3 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.l3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.l3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.l3.setObjectName("l3")
        self.verticalLayout.addWidget(self.l3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lchb3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.lchb3.setObjectName("lchb3")
        self.horizontalLayout_3.addWidget(self.lchb3)
        self.chb3 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.chb3.setObjectName("chb3")
        self.horizontalLayout_3.addWidget(self.chb3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.le3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.le3.setText("")
        self.le3.setObjectName("le3")
        self.horizontalLayout_7.addWidget(self.le3)
        self.lk3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.lk3.setText("")
        self.lk3.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.lk3.setObjectName("lk3")
        self.horizontalLayout_7.addWidget(self.lk3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 301, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.b_add = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2, clicked = lambda: self.openwindowadd())
        self.b_add.setObjectName("b_add")
        self.horizontalLayout_6.addWidget(self.b_add)
        self.b_dell = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2, clicked = lambda: self.delldb())
        self.b_dell.setObjectName("b_dell")
        self.horizontalLayout_6.addWidget(self.b_dell)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def delldb(self):
        if os.path.exists('db/user_database.db'):

            os.unlink('db/user_database.db')

    def cheaked1(self):
        bool1 = self.chb1.isChecked()
        return bool1

    def cheaked2(self):
        bool2 = self.chb2.isChecked()
        return bool2

    def cheaked3(self):
        bool3 = self.chb3.isChecked()
        return bool3

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SEDA"))
        self.lchb1.setText(_translate("MainWindow", "     Новое устройство:"))
        self.chb1.setText(_translate("MainWindow", "да/нет"))
        self.lchb2.setText(_translate("MainWindow", "     Новое устройство:"))
        self.chb2.setText(_translate("MainWindow", "да/нет"))
        self.lchb3.setText(_translate("MainWindow", "     Новое устройство:"))
        self.chb3.setText(_translate("MainWindow", "да/нет"))
        self.b_add.setText(_translate("MainWindow", "Добавить"))
        self.b_dell.setText(_translate("MainWindow", "Удалить все"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    def bdcalle(id):
        conn = sqlite3.connect('db/user_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT login FROM users WHERE id = ?", (id,))
        e = str(cursor.fetchall())
        re = e[3:len(e) - 4]
        conn.commit()
        conn.close()
        return re

    def bdcallimap(id):
        conn = sqlite3.connect('db/user_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM users WHERE id = ?", (id,))
        imap = str(cursor.fetchall())
        rimap = imap[3:len(imap) - 4]
        conn.commit()
        conn.close()
        return rimap
    def bdcallp(id):
        conn = sqlite3.connect('db/user_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE id = ?", (id,))
        p = str(cursor.fetchall())
        rp = p[3:len(p) - 4]
        conn.commit()
        conn.close()
        return rp

    def mail(id, pr):
        mail_pass = bdcallp(id)
        username = bdcalle(id)
        imap_server = bdcallimap(id)
        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(username, mail_pass)
        imap.select("INBOX")
        res, msg = imap.search(None, 'ALL')
        ids = msg[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]

        res, msg = imap.fetch(latest_email_id, '(RFC822)')
        msg = email.message_from_bytes(msg[0][1])

        mess_text_good = ''
        for part in msg.walk():
            if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
                mess_text = part.get_payload()

        for i in mess_text:
            if i != ',' and i != '.' and i != '!' and i != '?' and i != ':' and i != ';' and i != ' ':
                mess_text_good = mess_text_good + i

        output_decode = quopri.decodestring(mess_text_good)
        result = output_decode.decode('utf-8')

        if pr == 1:
            pos = result.find("Коддоступа")
            res1 = result[pos + 12:pos + 17]
            return res1
        elif pr == 0:
            pos = result.find("Выполучилиэтописьмо")
            res2 = result[pos - 9:pos - 4]
            return res2

        imap.close()
        imap.logout()

    def update_label():
        ui.le1.setText(bdcalle(1))
        if bdcalle(1) == "" or bdcallp(1) == "":
            return 0
        else:
            if ui.cheaked1()==True:
                ui.lk1.setText(mail(1, 1))
            elif ui.cheaked1()==False:
                ui.lk1.setText(mail(1, 0))

        ui.le2.setText(str(bdcalle(2)))
        if bdcalle(2) == "" or bdcallp(2) == "":
            return 0
        else:
            if ui.cheaked2()==True:
                ui.lk2.setText(mail(2, 1))
            elif ui.cheaked2()==False:
                ui.lk2.setText(mail(2, 0))
        ui.le3.setText(str(bdcalle(3)))
        if bdcalle(3) == "" or bdcallp(3) == "":
            return 0
        else:
            if ui.cheaked3()==True:
                ui.lk3.setText(mail(3, 1))
            elif ui.cheaked3()==False:
                ui.lk3.setText(mail(3, 0))

    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(1000)

    sys.exit(app.exec())
