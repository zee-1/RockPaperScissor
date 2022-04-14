import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QStackedWidget

from playScreen import PlayScreen

class mainScreen(QDialog):
      def __init__(self):
            super(mainScreen, self).__init__()
            loadUi('Welcom.ui', self)
            self.setFixedHeight(670)
            self.setFixedWidth(530)
            self.setMaximumHeight(670)
            self.setMaximumWidth(530)
            self.setMinimumHeight(670)
            self.setMinimumWidth(530)
            self.Play.clicked.connect(self.gotoPlay)
            self.Quit.clicked.connect(lambda: self.close())
      def gotoPlay(self):
            play = PlayScreen(app)
            main.addWidget(play)
            main.setCurrentIndex(main.currentIndex()+1)

if __name__ == '__main__':
      app = QtWidgets.QApplication(sys.argv)
      MW = mainScreen()
      main = QStackedWidget()
      main.addWidget(MW)
      main.show()
      sys.exit(app.exec_())