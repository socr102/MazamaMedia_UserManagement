from login import *

app = QApplication(sys.argv)
login = LoginForm()
login.show()

app.setQuitOnLastWindowClosed(True)
icon = QtGui.QIcon("mazama.png")
          
tray = QtWidgets.QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)
menu = QtWidgets.QMenu()
log = QtWidgets.QAction("View Log")
log.triggered.connect(login.w.showlog)
menu.addAction(log)

    
quit = QtWidgets.QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

tray.setContextMenu(menu)
sys.exit(app.exec_())
