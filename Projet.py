# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Projet.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Pas_simple_objet import *
from Pas_accelere_objet import *
from Bissection import *
from NewtonRaphson import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 110, 161, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 221, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 151, 16))
        self.label_2.setObjectName("label_2")
        self.Function = QtWidgets.QLineEdit(self.centralwidget)
        self.Function.setGeometry(QtCore.QRect(30, 170, 161, 31))
        self.Function.setObjectName("Function")
        self.Pas = QtWidgets.QLineEdit(self.centralwidget)
        self.Pas.setGeometry(QtCore.QRect(130, 270, 71, 21))
        self.Pas.setObjectName("Pas")
        self.Valeur_depart = QtWidgets.QLineEdit(self.centralwidget)
        self.Valeur_depart.setGeometry(QtCore.QRect(130, 310, 71, 21))
        self.Valeur_depart.setObjectName("Valeur_depart")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 270, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 310, 91, 16))
        self.label_4.setObjectName("label_4")
        self.Solutions = QtWidgets.QTextEdit(self.centralwidget)
        self.Solutions.setGeometry(QtCore.QRect(360, 270, 256, 71))
        self.Solutions.setReadOnly(True)
        self.Solutions.setObjectName("Solutions")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(360, 250, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 0, 381, 61))
        self.label_7.setObjectName("label_7")
        self.Step = QtWidgets.QGraphicsView(self.centralwidget)
        self.Step.setGeometry(QtCore.QRect(360, 120, 256, 111))
        self.Step.setObjectName("Step")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 100, 47, 13))
        self.label_5.setObjectName("label_5")
        self.Epsilon = QtWidgets.QTextEdit(self.centralwidget)
        self.Epsilon.setGeometry(QtCore.QRect(130, 350, 71, 21))
        self.Epsilon.setObjectName("Epsilon")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 350, 91, 16))
        self.label_8.setObjectName("label_8")
        self.Intervalle = QtWidgets.QTextEdit(self.centralwidget)
        self.Intervalle.setGeometry(QtCore.QRect(130, 380, 71, 21))
        self.Intervalle.setObjectName("a")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 380, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 210, 161, 21))
        self.label_10.setObjectName("label_10")
        self.Optimize = QtWidgets.QPushButton(self.centralwidget)
        self.Optimize.setGeometry(QtCore.QRect(450, 360, 75, 23))
        self.Optimize.setObjectName("Optimize")
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(540, 360, 75, 23))
        self.Clear.setObjectName("Clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.Clear.clicked.connect(self.clear)
        self.Optimize.clicked.connect(self.optimi)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Pas fixe"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Pas fixe accéléré"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Méthode de la bissection"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Newton Raphson"))
        self.label.setText(_translate("MainWindow", "Choose your optimisation method :"))
        self.label_2.setText(_translate("MainWindow", "Enter your function"))
        self.label_3.setText(_translate("MainWindow", "Pas :"))
        self.label_4.setText(_translate("MainWindow", "Valeur de départ :"))
        self.label_6.setText(_translate("MainWindow", "Solutions"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; font-style:italic;\">Non Linear Optimization</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Step"))
        self.label_8.setText(_translate("MainWindow", "Epsilon :"))
        self.label_9.setText(_translate("MainWindow", "Intervalle [ ] :"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">(Exemple : a*x**2 + b* x * c)</span></p></body></html>"))
        self.Optimize.setText(_translate("MainWindow", "Optimize"))
        self.Clear.setText(_translate("MainWindow", "Clear"))
        
        
    def clear(self):
        self.Function.setText(None)
        self.Intervalle.setText(None)
        self.Epsilon.setText(None)
        self.Valeur_depart.setText(None)
        self.Pas.setText(None)
        
    # def gris(self):
        
    #     if self.comboBox.currentIndex() == 0 :
    #         self.Intervalle.setEnabled(False)
    #         self.Epsilon.setEnabled(False)
            
    #     elif self.comboBox.currentIndex() == 1 :
    #         self.Epsilon.setEnabled(True)

                    

        
        
        
    def optimi(self):
        
        function = self.Function.text()
        
        if self.comboBox.currentIndex() == 0 :
            
            #On récupère ici les variables de l'utilisateur pour faire le calcul du pas fixe
            pas = float(self.Pas.text())
            x1 = float(self.Valeur_depart.text())
            i = 1
            
            Test = Pas_fixe()
            res = Test.pas_fixe(i,pas,x1)
            r = Test.f(i,pas,x1)
            i=res[0]
            a=res[1]
            b=res[2]  
            self.Solutions.setText(f'x ∈ {a} et {b} \nf(x* = {r})')
                                         
        elif self.comboBox.currentIndex() == 1 :
            
            Test = Pas_fixe_acc()
            res= Test.pas_fixe_acc()
            n=res[0]
            a=res[1]
            b=res[2]   
            s=res[3]
            print(f"Le point de minimum x* se situe entre {a} et {b}")

            
            
        # elif self.comboBox.currentIndex() == 2 :
        #     
            
        #     bissection(function, a, b, N)
            
            
        # elif self.comboBox.currentIndex() == 3 :
            
        
        # fx = self.Function.text()
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

