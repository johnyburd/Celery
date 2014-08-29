from CeleryUI01 import *

class UI_Celery(object):
    #:def __init__(self, parent=None, name=None, fl=0):
       # object.__init__(self,parent,name,fl)
    QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sendText)

#def sendText(self):
 #   self.label.setText(self.lineEdit.text())
  #  ircSend(self.lineEdit.text())


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Celery = QtGui.QMainWindow()
    ui = Ui_Celery()
    ui.setupUi(Celery)
    Celery.show()
    sys.exit(app.exec_())
