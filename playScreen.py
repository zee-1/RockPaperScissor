import sys
from time import sleep
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QStackedWidget

import RPS

class PlayScreen(QDialog):
      choice = "noChoice"
      A = "noChoice"
      Ready = False
      Score =int(0);
      def __init__(self,app):
            super(PlayScreen, self).__init__()
            loadUi('playscreen.ui', self)
            self.setFixedHeight(670)
            self.setFixedWidth(530)
            self.setMaximumHeight(670)
            self.setMaximumWidth(530)
            self.setMinimumHeight(670)
            self.setMinimumWidth(530)
            self.Rock.clicked.connect(self.giveRock)
            self.Paper.clicked.connect(self.givePaper)
            self.Scissors.clicked.connect(self.giveScissors)
            self.ready.clicked.connect(self.ReadyNotReady)
            self.quit.clicked.connect(self.Quit)
      def Quit(self):
            self.close()

      def updateBotLable(self):
            self.A = RPS.bot_choice()
            # pixmap = QPixmap('/home/zee/Documents/RockPaperScissors/img/loading.png')
            # pixmap = pixmap.scaled(80,80)
            # self.Bot.setPixmap(pixmap)
            # sleep(0.05)
            if (self.A == "Rock"):
                  pixmap = QPixmap('/home/zee/Documents/RockPaperScissors/img/raised-fist-emoji-by-google.png')   #change this path to your path /your-path/img/raised-fist-emoji-by-google.png
                  pixmap = pixmap.scaled(80,80)
                  self.Bot.setPixmap(pixmap)
            elif (self.A == "Paper"):
                  pixmap = QPixmap('/home/zee/Documents/RockPaperScissors/img/hand-emoji-by-google.png')          #change this path to your path /your-path/img/hand-emoji-by-google.png
                  pixmap = pixmap.scaled(80,80)
                  self.Bot.setPixmap(pixmap)
            elif (self.A == "Scissors"):
                  pixmap = QPixmap('/home/zee/Documents/RockPaperScissors/img/peace-sign-emoji-by-google.png')    #change this path to/your-path/img/peace-sign-emoji-by-google.png'
                  pixmap = pixmap.scaled(80,80)
                  self.Bot.setPixmap(pixmap)
      
      def incScore(self):
            self.Score+=1

      def ReadyNotReady(self):
            if(not self.Ready):
                  self.Ready = True
                  count = 3;
                  while count>=0:
                        self.counter.setText("Start")
                        sleep(0.3)
                        count -=1
                  self.ready_l.setStyleSheet("background-color: #00ff11; border-radius: 8px")
            else:
                  self.Ready = False
                  self.ready_l.setStyleSheet("background-color: rgb(255,0,0); border-radius: 8px")
                  

      def giveRock(self):
            if(not self.Ready):
                  self.counter.setText("You're not ready yet")
                  sleep(2)
                  self.counter.setText("Waiting")
                  return
            self.choice = "Rock"
            self.updateBotLable()
            self.counter.setText(RPS.RPS_win_loss(self.choice,self.A,self.incScore))
            self.scoreCard.setText(str(self.Score))
            self.choice = "noChoice"
            self.A = "noChoice"


      def givePaper(self):
            self.choice = "Paper"
            if(not self.Ready):
                  self.counter.setText("You're not ready yet")
                  sleep(2)
                  self.counter.setText("Waiting")
                  return
            self.updateBotLable()
            self.counter.setText(RPS.RPS_win_loss(self.choice,self.A,self.incScore))
            self.scoreCard.setText(str(self.Score))
            self.choice = "noChoice"
            self.A = "noChoice"


      def giveScissors(self):
            self.choice = "Scissors"
            if(not self.Ready):
                  self.counter.setText("You're not ready yet")
                  sleep(2)
                  self.counter.setText("Waiting")
                  return
            self.updateBotLable()
            self.counter.setText(RPS.RPS_win_loss(self.choice,self.A,self.incScore))
            self.scoreCard.setText(str(self.Score))
            self.choice = "noChoice"
            self.A = "noChoice"
