from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from main import *

import hashlib
import requests,re
import mysql.connector as mc
import sys,os
import MySQLdb
import datetime
import warnings


class Signup(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.w = Window()

        self.setWindowTitle("Signup")
        self.setFixedHeight(325)
        self.setFixedWidth(536)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("mazama.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.label_4 = QtWidgets.QLabel("Password:",self)
        self.label_4.setGeometry(QtCore.QRect(140, 160, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_5 = QtWidgets.QLabel("Rewrite Password:",self)
        self.label_5.setGeometry(QtCore.QRect(90, 200, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_3 = QtWidgets.QLabel("UserName or email:",self)
        self.label_3.setGeometry(QtCore.QRect(80, 120, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        
        
        self.username = QtWidgets.QLineEdit(self)
        self.username.setGeometry(QtCore.QRect(220, 120, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.username.setFont(font)

        self.pwd = QtWidgets.QLineEdit(self)
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd.setGeometry(QtCore.QRect(220, 160, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pwd.setFont(font)

        self.pwd_again = QtWidgets.QLineEdit(self)
        self.pwd_again.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd_again.setGeometry(QtCore.QRect(220, 200, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pwd_again.setFont(font)

        self.signin = QtWidgets.QPushButton("Sign Up ",self)
        self.signin.setGeometry(QtCore.QRect(220, 240, 91, 31))
        self.signin.clicked.connect(self.SignIn)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signin.setFont(font)

        self.label_2 = QtWidgets.QLabel("FacebookMessenger Management",self)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        
    def SignIn(self):
        try:
            email_or_username = self.username.text()
            username=""
            pwd = self.pwd.text()
            pwd_again = self.pwd_again.text()
            now = datetime.datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", email_or_username)

            if len(email)>0 :
                email = email[0]
                # response = requests.get("https://isitarealemail.com/api/email/validate",params = {'email': email})
                # status = response.json()['status']
                status = 'valid'
                if status=='valid':
                    if pwd== pwd_again:
                        mydb = mc.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="mazama"
                        )
                        mycursor = mydb.cursor()
                        query = "INSERT INTO manager(username,email,pwd,created_date) VALUES (%s, %s,%s,%s)"
                        val = (username,email,hashlib.md5(pwd.encode()).hexdigest(),current_time)
                        mycursor.execute(query,val)
                        mydb.commit()
                        self.hide()
                        self.w.show()
                    else:
                        QMessageBox.critical(self, "Warning!!!",'Passowrd Not Matching!!!') 
                        self.pwd.setText("")
                        self.pwd_again.setText("")  
                            
                else:
                    QMessageBox.critical(self, "Warning!!!",'Invalid email!')   
                    self.username.setText("")
                    self.pwd.setText("")
                    self.pwd_again.setText("")  
            else:
                username = email_or_username
                email=""
                if pwd == pwd_again:
                    mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="mazama"
                    )
                    mycursor = mydb.cursor()
                    query = "INSERT INTO manager (username,email,pwd,created_date) VALUES (%s, %s,%s,%s)"
                    val = (username,email,hashlib.md5(pwd.encode()).hexdigest(),current_time)
                    mycursor.execute(query,val)
                    mydb.commit()
                    self.hide()
                    self.w.show()
                else:
                    QMessageBox.critical(self, "Warning!!!",'Passowrd Not Matching!!!') 
                    self.pwd.setText("")
                    self.pwd_again.setText("")  
        except mc.Error as e:
            self.username.setText("")
            self.pwd.setText("")
            self.pwd_again.setText("")                     