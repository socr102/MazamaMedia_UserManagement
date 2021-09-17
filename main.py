from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox

import datetime
import MySQLdb
import sys,os

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

        #set the username
        self.username = ""
        self.manager = ""
        #set the icon
        self.setWindowIcon(QtGui.QIcon('mazama.png'))
        # set the title
        self.setWindowTitle("MazamaMedia")
        #set the size of the window
        # setting the minimum size
        width = 1000
        height = 700
        self.setMinimumSize(width, height)
        #set the widget
        self.layout = QtWidgets.QGridLayout()
        

        self.setLayout(self.layout)
        self.listlabel = QtWidgets.QLabel("UserList") 
        self.listlabel.setFont(QtGui.QFont('Arial', 20))  
        self.listwidget = QtWidgets.QListWidget()
        self.userlistlabel = QtWidgets.QLabel("UserInfo")
        self.userlistlabel.setFont(QtGui.QFont('Arial', 20))   
        self.table_widget = QtWidgets.QTableWidget()
        self.editline = QtWidgets.QLineEdit()
        self.editline.setFixedHeight(30)
        self.submit = QtWidgets.QPushButton("Submit")
        self.submit.setFont(QtGui.QFont('Times', 15))
        self.refresh = QtWidgets.QPushButton(" Load Database ")
        self.refresh.setFont(QtGui.QFont('Times', 15))

        self.refresh.clicked.connect(self.load_database)
        self.submit.clicked.connect(self.transfer_message)
        #gridlayout
        self.layout.addWidget(self.listlabel,0,0,1,1) 
        self.layout.addWidget(self.listwidget,1,0,4,1)    
        self.layout.addWidget(self.userlistlabel,0,2,1,1)
        self.layout.addWidget(self.table_widget,1,2,4,4)
        self.layout.addWidget(self.editline,5,0,1,1)
        self.layout.addWidget(self.submit,5,1,1,1)
        self.layout.addWidget(self.refresh,0,5,1,1)
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 0)
        self.layout.setColumnStretch(2, 3)
        self.layout.setRowStretch(0, 0)
        self.layout.setRowStretch(1, 4)
        self.layout.setRowStretch(2, 0)
        self.layout.setRowStretch(3, 1)

    def load_database(self):
        self.pbar = QtWidgets.QProgressBar(self)
        self.layout.addWidget(self.pbar,5,2,2,1)

        self.refresh.setText("Refresh Database")
        self.listwidget.clear()
        #get the user list from the database
        users = get_user_list()
        # add the list in the list widget using the data from the database
        index = 0
        total = len(users)
        for user in users:
            self.listwidget.insertItem(index, user[0])
            index+=1
            self.pbar.setValue(float(index*100/total))
        self.listwidget.clicked.connect(self.clicked)

    def clicked(self, qmodelindex):
        # self.userlistwidget.clear()
        self.pbar.hide()
        self.table_widget.setShowGrid(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(1)
        self.table_widget.setRowCount(18)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(("Item", "Value"))

        item = self.listwidget.currentItem()
        user_info = get_user_info(item.text())
        self.username = item.text()
        length= len(user_info[0])
        items = ['ID','Email','FirstName','MiddleName','LastName','SecondName','Suffix','DateOfBirth','SocialSecurityNumber','ResidenceAddresss','Apartment','Permanent','Unit_address','Unit_Apartment','Unit_zipcode','ResidenceZipcode','ResidenceCity','ResidenceState']
        index = 0
        for i in range(length-1):
            self.table_widget.setItem(index,0, QtWidgets.QTableWidgetItem(items[i]))
            self.table_widget.setItem(index, 1, QtWidgets.QTableWidgetItem(str(user_info[0][i])))
            index+=1

        # self.table_widget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            
    def transfer_message(self):
        text = self.editline.text()
        if self.username=="":
            QMessageBox.critical(self, "Warning!!!",'Select the correct username!')
        elif text=="":
            QMessageBox.critical(self, "Warning!!!",'Please fill the submit text!')   
        else:     
            buttonReply  = QMessageBox.question(self, 'To {}'.format(self.username), "Do you really submit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                QMessageBox.about(self,"Success!!","It submits successful")
                now = datetime.datetime.now()
                current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                try:
                    with open("log.txt","a") as f:
                        f.write("You submit `{}` to `{}` at {} ".format(text,self.username,current_time))
                        f.write("\n")
                        f.close()
                except IOError:
                    with open("log.txt","w") as f:
                        f.write("You submit `{}` to '{}' at {} ".format(text,self.username,current_time))
                        f.write("\n")
                        f.close()           
            else:
                print('No clicked.')
        self.editline.setText("")
        self.username==""

    def showlog(self):
        osCommandString = "notepad.exe log.txt"
        os.system(osCommandString)   

