# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Fri Aug 29 17:41:05 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def ircSend(textToSend):
    print(textToSend) 

class Ui_Celery(object):

    def setupUi(self, Celery):
        Celery.setObjectName(_fromUtf8("Celery"))
        Celery.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Celery)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Celery.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Celery)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Celery.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Celery)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Celery.setStatusBar(self.statusbar)

        self.retranslateUi(Celery)

        #######
        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sendText)
        QtCore.QMetaObject.connectSlotsByName(Celery)

#    def sendText(self):
#        self.label.setText(self.lineEdit.text())
#        ircSend(self.lineEdit.text())

    def retranslateUi(self, Celery):
        Celery.setWindowTitle(_translate("Celery", "Celery", None))
        self.label.setText(_translate("Celery", "TextLabel", None))
        self.pushButton.setText(_translate("Celery", "PushButton", None))

"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Celery = QtGui.QMainWindow()
    ui = Ui_Celery()
    ui.setupUi(Celery)
    Celery.show()
    sys.exit(app.exec_())
"""
