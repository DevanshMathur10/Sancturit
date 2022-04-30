import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from maps import map

def locshow():
    map()
    app = QApplication(sys.argv)
    web = QWebEngineView()
    web.setWindowTitle("EMERGENCY LOCATIONS")
    web.load(QUrl("C:/Users/DELL/Documents/VS/HACKATHONS/SANCTURIT/map.html"))
    web.showMaximized()
    web.show()
    app.exec_()
#locshow()