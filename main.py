from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox

import MySQLdb
import sys

def get_user_list():
    db = MySQLdb.connect("localhost","root","","mazama" )
    cursor = db.cursor()
    sql = "SELECT First_name FROM  userlist "
    try:
        user_list_data = []
        cursor.execute(sql)
        users = cursor.fetchall()
        for user in users:
            user_list_data.append(user)
        return user_list_data    
    except:
        print ("Error: unable to fecth data")        

def get_user_info(first_name):
    db = MySQLdb.connect("localhost","root","","mazama" )
    cursor = db.cursor()
    sql = "SELECT * FROM  userlist WHERE First_name = '%s'" % (first_name)
    try:
        user_info_data = []
        cursor.execute(sql)
        users = cursor.fetchall()
        for user in users:
            user_info_data.append(user)
        return user_info_data    
    except:
        print ("Error: unable to fecth data")

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.listlabel = QtWidgets.QLabel("UserList")   
        self.listwidget = QtWidgets.QListWidget()
        users = get_user_list()
        index = 0
        for user in users:
            self.listwidget.insertItem(index, user[0])
            index+=1
        self.listwidget.clicked.connect(self.clicked)   
        self.layout.addWidget(self.listlabel,0,0) 
        self.layout.addWidget(self.listwidget,1,0)
        
        self.userlistlabel = QtWidgets.QLabel("UserInfo")   
        self.table_widget = QtWidgets.QTableWidget()
        self.layout.addWidget(self.userlistlabel,0,2)
        self.layout.addWidget(self.table_widget,1,2)

        self.editline = QtWidgets.QLineEdit()
        self.layout.addWidget(self.editline,2,0)


        self.submit = QtWidgets.QPushButton("Submit")
        self.submit.clicked.connect(self.transfer_message)
        self.refresh = QtWidgets.QPushButton("Refresh")

        self.layout.addWidget(self.submit,2,1)
        self.layout.addWidget(self.refresh,2,2)


    def clicked(self, qmodelindex):
        # self.userlistwidget.clear()
        self.table_widget.setShowGrid(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(1)
        self.table_widget.setRowCount(18)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(("Item", "Value"))

        item = self.listwidget.currentItem()
        user_info = get_user_info(item.text())
        length= len(user_info[0])
        items = ['ID','Email','FirstName','MiddleName','LastName','SecondName','Suffix','DateOfBirth','SocialSecurityNumber','ResidenceAddresss','Apartment','Permanent','Unit_address','Unit_Apartment','Unit_zipcode','ResidenceZipcode','ResidenceCity','ResidenceState']
        index = 0
        for i in range(length-1):
            self.table_widget.setItem(index,0, QtWidgets.QTableWidgetItem(items[i]))
            self.table_widget.setItem(index, 1, QtWidgets.QTableWidgetItem(str(user_info[0][i])))
            index+=1
    def transfer_message(self):
        text = self.editline.text()
        QMessageBox.about(self, "Success", text)
        self.editline.setText("")

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())