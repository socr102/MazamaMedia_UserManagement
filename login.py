from signup import *
from random import randint



class LoginForm(QtWidgets.QWidget):
	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.w = Window()
		self.s = Signup()
		self.setWindowTitle("Login")
		self.setFixedHeight(325)
		self.setFixedWidth(536)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("mazama.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(icon)

		self.signup = QtWidgets.QPushButton("Sign Up",self)
		self.signup.setGeometry(QtCore.QRect(220, 280, 81, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.signup.setFont(font)
		self.label = QtWidgets.QLabel("If you have\'t  an account,please sign up",self)
		self.label.setGeometry(QtCore.QRect(80, 260, 231, 16))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(10)
		self.label.setFont(font)
		self.label_2 = QtWidgets.QLabel("FacebookMessenger Management",self)
		self.label_2.setGeometry(QtCore.QRect(90, 20, 391, 61))
		font = QtGui.QFont()
		font.setFamily("Terminal")
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label_2.setFont(font)
		self.label_2.setTextFormat(QtCore.Qt.RichText)
		self.label_3 = QtWidgets.QLabel("UserName or email:",self)
		self.label_3.setGeometry(QtCore.QRect(80, 100, 131, 21))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_3.setFont(font)
		self.label_4 = QtWidgets.QLabel("Password:",self)
		self.label_4.setGeometry(QtCore.QRect(140, 140, 71, 21))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_4.setFont(font)
		self.username = QtWidgets.QLineEdit(self)
		self.username.setGeometry(QtCore.QRect(220, 100, 241, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(10)
		self.username.setFont(font)
		self.pwd = QtWidgets.QLineEdit(self)
		self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
		self.pwd.setGeometry(QtCore.QRect(220, 140, 241, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(10)
		self.pwd.setFont(font)
		self.label_5 = QtWidgets.QLabel("Security",self)
		self.label_5.setGeometry(QtCore.QRect(140, 180, 71, 21))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_5.setFont(font)
		self.security = QtWidgets.QLineEdit(self)
		self.security.setGeometry(QtCore.QRect(220, 180, 241, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(10)
		self.security.setFont(font)
		self.login = QtWidgets.QPushButton("Log In",self)
		self.login.setGeometry(QtCore.QRect(220, 220, 91, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.login.setFont(font)
		self.login.clicked.connect(self.LogIn)
		self.signup.clicked.connect(self.SignUp)
		self.generate_security()
	def LogIn(self):
			try:
				email = self.username.text()
				password = hashlib.md5(self.pwd.text().encode()).hexdigest()
				security = self.security.text()

				mydb = mc.connect(
					host="localhost",
					user="root",
					password="",
					database="mazama"
				)
	 
				mycursor = mydb.cursor()
				query = "SELECT email,username,pwd from manager where (email " \
						"like '"+email + "' or username " \
						"like '"+email + "') and pwd like '" \
						+ password + "'"

				mycursor.execute(query)
				result = mycursor.fetchone()
				if result == None:
					email = self.username.setText("")
					password = self.pwd.setText("")
					security = self.security.setText("")
					self.generate_security()
				else:
					if security!=str(self.security_number):
						email = self.username.setText("")
						password = self.pwd.setText("")
						security = self.security.setText("")
						self.generate_security()
					else:
						self.hide()
						self.w.show()

			except mc.Error as e:
				self.username.setText("")
				self.pwd.setText("")
				self.security.setText("")
	def SignUp(self):
		self.hide()
		self.s.show()

	def generate_security(self):
		value1 = randint(0, 10)
		value2 = randint(0, 10)
		self.security_number = value1+value2
		self.security.setText("{}+{}=?".format(value1,value2))

	
