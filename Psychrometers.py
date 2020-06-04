# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Psychrometer's.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math
import numpy as np
from scipy.optimize import ridder
import pandas as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 628)
        MainWindow.setWindowIcon(QtGui.QIcon('icon_psy.png'))
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.darkBlue)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(300, 50, 331, 161))
        self.groupBox.setObjectName("groupBox")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(230, 120, 81, 22))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_3.setDecimals(1)
        self.doubleSpinBox_3.setProperty("value", 60.0)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(230, 80, 81, 22))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_2.setDecimals(0)
        self.doubleSpinBox_2.setMaximum(1000)
        self.doubleSpinBox_2.setProperty("value", 760)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 201, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 201, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(230, 40, 81, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setProperty("value", 35.0)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 201, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 20, 241, 221))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 270, 631, 321))
        self.groupBox_2.setObjectName("groupBox_2")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setPalette(palette)
        self.lineEdit_7.setGeometry(QtCore.QRect(470, 270, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(250, 20, 191, 71))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 241, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 220, 241, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setPalette(palette)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 170, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignHCenter)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setPalette(palette)
        self.lineEdit_6.setGeometry(QtCore.QRect(290, 220, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignHCenter)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setPalette(palette)
        self.lineEdit_5.setGeometry(QtCore.QRect(470, 220, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignHCenter) 
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 270, 241, 21))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setPalette(palette)
        self.lineEdit_8.setGeometry(QtCore.QRect(290, 270, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignHCenter)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setPalette(palette)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 120, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(430, 20, 191, 71))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 170, 241, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setFont(font)
        self.lineEdit.setPalette(palette)
        self.lineEdit.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignHCenter)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setPalette(palette)
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 170, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 230, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_clicked)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Психрометрический расчёт"))
        self.groupBox.setTitle(_translate("MainWindow", "Исходные данные"))
        self.label.setText(_translate("MainWindow", "Температура по сухому термометру, <span style=\" vertical-align:super;\">0</span>С"))
        self.label_3.setText(_translate("MainWindow", "Влажность, %"))
        self.label_2.setText(_translate("MainWindow", "Давление воздуха, мм.рт.ст."))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00007f;\">Расчёт </span></p><p align=\"center\"><span style=\" font-weight:600; color:#00007f;\">температуры по влажному термометру,</span></p><p align=\"center\"><span style=\" font-weight:600; color:#00007f;\">точки росы, энтальпии и плотности </span></p><p align=\"center\"><span style=\" font-weight:600; color:#00007f;\">влажного воздуха</span></p><p align=\"center\"><span style=\" color:#00007f;\">в зависимости от влажности, давления</span></p><p align=\"center\"><span style=\" color:#00007f;\">и температуры по сухому термометру</span></p><p align=\"center\"><span style=\" color:#00007f;\">по двум стандартам </span></p><p align=\"center\"><span style=\" color:#00007f;\">психрометрического расчёта.</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Результаты"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Расчёт по </p><p align=\"center\">2017 ASHRAE Handbook</p><p align=\"center\">Fundamentals</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Температура по влажному термометру,<span style=\" vertical-align:super;\">0</span>С</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Удельная энтальпия влажного воздуха, Дж/кг</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Плотность влажного воздуха, кг/м<sup>3</sup></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Расчёт по </p><p align=\"center\">ГОСТ Р 8.811-2012</p><p align=\"center\"> Таблицы психрометрические</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Точка росы, <span style=\" vertical-align:super;\">0</span>С</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "РАССЧИТАТЬ"))

    def on_clicked(self):
        t_d = self.doubleSpinBox.value()
        P = self.doubleSpinBox_2.value()
        phi = self.doubleSpinBox_3.value()
        data = (t_d,P,phi)
        tau = float(ridder(find,-50,100, args = data))
        dew = float(ridder(finddew,-50,tau, args = data))
        s = "%.4g"%tau
        self.lineEdit_2.setText(s)
        s = "%.4g"%dew
        self.lineEdit_3.setText(s)
        data = (phi/100,t_d,P*133.322)
        tau = float(ridder(wetbulb_temp,-50,100, args = data))
        s = "%.4g"%tau
        self.lineEdit.setText(s)
        (W,Pw,Pws) = pressure_w(tau,t_d,P*133.322)
        dew = 6.54+14.526*math.log(Pw,math.exp(1))+0.7389*math.log(Pw,math.exp(1))**2+0.09486*math.log(Pw,math.exp(1))**3+0.4569*Pw**0.1984
        s = "%.4g"%dew
        self.lineEdit_4.setText(s)
        h = 1.006*t_d+W*(2501+1.86*t_d)
        s = "%.5g"%h
        self.lineEdit_6.setText(s)
        g = P*0.133322/0.287042/(t_d+273.15)/(1+1.607858*W)*(1+W)
        s = "%.5g"%g
        self.lineEdit_8.setText(s)
        wdir='D:/Рабочие/Python'
        dataPD=pd.read_excel('TablePD_h.xls');
        T = dataPD['T'];
        #энтальпия
        d = list(dataPD['D'])[list(np.round(T,2)).index(round(t_d,2))];
        p = list(dataPD['P'])[list(np.round(T,2)).index(round(t_d,2))];
        x = phi/100*d*29.27*(t_d+273.15)/(13.5951*P-phi/100*p);
        enth = (0.24*t_d+x*(597.7+0.45*t_d))*4.1868;
        s = "%.5g"%enth
        self.lineEdit_5.setText(s)
        g = (13.5951*P-phi/100*p)/29.27/(t_d+273.15)+phi/100*d;
        s = "%.5g"%g
        self.lineEdit_7.setText(s)

def elasticity(t):
    E_w = 10**(10.79574*(1-273.16/(273.15+t))-5.028*math.log10((273.15+t)/273.16)+1.50475*10**(-4)*(1-10**(-8.2969*((273.15+t)/273.16-1)))+0.42873*10**(-3)*(10**(4.76955*(1-273.16/(273.15+t)))-1)+0.78614) 
    return E_w
    
def find(t,*data):
    tetta,p,f = data;
    e = f/100*elasticity(tetta);
    return elasticity(t)-0.0007947*p*1.33322*(tetta-t)*(1+0.00115*t)-e

def finddew(t,*data):
    tetta,p,f = data;
    e = f/100*elasticity(tetta);
    return elasticity(t)-e

def pressure_w(t, t_d, P):
    C8 = -5.8002206e3
    C9 = 1.3914993
    C10 = -4.8640239e-2
    C11 = 4.1764768e-5
    C12 = -1.4452093e-8
    C13 = 6.5459673
    T_w = t + 273.15
    T_d = t_d +273.15
    Pws = math.exp(C8/T_d+C9+C10*T_d+C11*T_d**2+C12*T_d**3+C13*math.log(T_d,math.exp(1)))
    Pws_w = math.exp(C8/T_w+C9+C10*T_w+C11*T_w**2+C12*T_w**3+C13*math.log(T_w,math.exp(1)))
    Ws_w = 0.621945*Pws_w/(P-Pws_w)
    W = ((2501-2.326*t)*Ws_w-1.006*(t_d-t))/(2501+1.86*t_d-4.186*t)
    Pw = P/1000*W/(0.621945+W)
    return (W,Pw,Pws)

def wetbulb_temp(t, *data):
    phi, t_d, P  = data
    (W,Pw,Pws) = pressure_w(t,t_d,P)
    return phi-Pw*1000/Pws

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

