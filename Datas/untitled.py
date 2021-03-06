# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import glob
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os, sys
import cv2 as cv
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator,img_to_array,array_to_img
from sklearn.model_selection import train_test_split
from tensorflow import keras
from PIL import Image
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report,confusion_matrix, auc, roc_curve
import matplotlib.pyplot as pyp
import seaborn as sns
from itertools import cycle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.teFolderName = QtWidgets.QTextEdit(self.tab)
        self.teFolderName.setGeometry(QtCore.QRect(0, 260, 341, 31))
        self.teFolderName.setObjectName("teFolderName")
        self.pbVeriOkuma = QtWidgets.QPushButton(self.tab)
        self.pbVeriOkuma.setGeometry(QtCore.QRect(340, 260, 201, 31))
        self.pbVeriOkuma.setObjectName("pbVeriOkuma")
        self.labelDataRead = QtWidgets.QLabel(self.tab)
        self.labelDataRead.setGeometry(QtCore.QRect(0, 20, 341, 231))
        self.labelDataRead.setScaledContents(True)
        self.labelDataRead.setObjectName("labelDataRead")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 261, 151))
        self.groupBox.setObjectName("groupBox")
        self.pbVeriOnisleme = QtWidgets.QPushButton(self.groupBox)
        self.pbVeriOnisleme.setGeometry(QtCore.QRect(10, 90, 141, 51))
        self.pbVeriOnisleme.setObjectName("pbVeriOnisleme")
        self.cbVeriArtirimi = QtWidgets.QCheckBox(self.groupBox)
        self.cbVeriArtirimi.setGeometry(QtCore.QRect(10, 40, 121, 41))
        self.cbVeriArtirimi.setObjectName("cbVeriArtirimi")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 41))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 561, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lblOrnekGorsel = QtWidgets.QLabel(self.groupBox_2)
        self.lblOrnekGorsel.setGeometry(QtCore.QRect(10, 20, 161, 131))
        self.lblOrnekGorsel.setScaledContents(True)
        self.lblOrnekGorsel.setObjectName("lblOrnekGorsel")
        self.lblOrnekGorsel2 = QtWidgets.QLabel(self.groupBox_2)
        self.lblOrnekGorsel2.setGeometry(QtCore.QRect(190, 20, 161, 131))
        self.lblOrnekGorsel2.setScaledContents(True)
        self.lblOrnekGorsel2.setObjectName("lblOrnekGorsel2")
        self.lblOrnekGorsel3 = QtWidgets.QLabel(self.groupBox_2)
        self.lblOrnekGorsel3.setGeometry(QtCore.QRect(390, 20, 161, 131))
        self.lblOrnekGorsel3.setScaledContents(True)
        self.lblOrnekGorsel3.setObjectName("lblOrnekGorsel3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(279, -1, 291, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pbTrainTransferLearning = QtWidgets.QPushButton(self.groupBox_3)
        self.pbTrainTransferLearning.setGeometry(QtCore.QRect(10, 30, 271, 51))
        self.pbTrainTransferLearning.setObjectName("pbTrainTransferLearning")
        self.pbCML = QtWidgets.QPushButton(self.groupBox_3)
        self.pbCML.setGeometry(QtCore.QRect(10, 90, 271, 51))
        self.pbCML.setObjectName("pbCML")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lblAccuracy = QtWidgets.QLabel(self.tab_4)
        self.lblAccuracy.setGeometry(QtCore.QRect(10, 10, 251, 131))
        self.lblAccuracy.setScaledContents(True)
        self.lblAccuracy.setObjectName("lblAccuracy")
        self.lblLoss = QtWidgets.QLabel(self.tab_4)
        self.lblLoss.setGeometry(QtCore.QRect(300, 10, 251, 131))
        self.lblLoss.setScaledContents(True)
        self.lblLoss.setObjectName("lblLoss")
        self.lblROC = QtWidgets.QLabel(self.tab_4)
        self.lblROC.setGeometry(QtCore.QRect(300, 170, 251, 131))
        self.lblROC.setScaledContents(True)
        self.lblROC.setObjectName("lblROC")
        self.lblKarmasiklikMatrisi = QtWidgets.QLabel(self.tab_4)
        self.lblKarmasiklikMatrisi.setGeometry(QtCore.QRect(10, 170, 251, 131))
        self.lblKarmasiklikMatrisi.setScaledContents(True)
        self.lblKarmasiklikMatrisi.setObjectName("lblKarmasiklikMatrisi")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.teTahminEt = QtWidgets.QTextEdit(self.tab_2)
        self.teTahminEt.setGeometry(QtCore.QRect(20, 280, 341, 31))
        self.teTahminEt.setObjectName("teTahminEt")
        self.pbTahminEtGorsel = QtWidgets.QPushButton(self.tab_2)
        self.pbTahminEtGorsel.setGeometry(QtCore.QRect(360, 280, 131, 31))
        self.pbTahminEtGorsel.setObjectName("pbTahminEtGorsel")
        self.lblDataReadTahmin = QtWidgets.QLabel(self.tab_2)
        self.lblDataReadTahmin.setGeometry(QtCore.QRect(20, 40, 381, 231))
        self.lblDataReadTahmin.setScaledContents(True)
        self.lblDataReadTahmin.setObjectName("lblDataReadTahmin")
        self.lblAcc = QtWidgets.QLabel(self.tab_2)
        self.lblAcc.setGeometry(QtCore.QRect(410, 140, 51, 21))
        self.lblAcc.setObjectName("lblAcc")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(410, 30, 151, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(410, 80, 71, 16))
        self.label_4.setObjectName("label_4")
        self.lblDorumu = QtWidgets.QLabel(self.tab_2)
        self.lblDorumu.setGeometry(QtCore.QRect(490, 140, 51, 21))
        self.lblDorumu.setText("")
        self.lblDorumu.setObjectName("lblDorumu")
        self.lblGercekEtiket = QtWidgets.QLabel(self.tab_2)
        self.lblGercekEtiket.setGeometry(QtCore.QRect(490, 30, 71, 16))
        self.lblGercekEtiket.setText("")
        self.lblGercekEtiket.setObjectName("lblGercekEtiket")
        self.lblTahminEtiket = QtWidgets.QLabel(self.tab_2)
        self.lblTahminEtiket.setGeometry(QtCore.QRect(490, 80, 71, 16))
        self.lblTahminEtiket.setText("")
        self.lblTahminEtiket.setObjectName("lblTahminEtiket")
        self.pbTahminEt = QtWidgets.QPushButton(self.tab_2)
        self.pbTahminEt.setGeometry(QtCore.QRect(490, 280, 75, 31))
        self.pbTahminEt.setObjectName("pbTahminEt")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbVeriOkuma.setText(_translate("MainWindow", "Klas??r Se??iniz"))
        self.labelDataRead.setText(_translate("MainWindow", "Okunacak Klas??r??n Etiket Say??lar??"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Veri Okuma"))
        self.groupBox.setTitle(_translate("MainWindow", "Veri ??ni??leme"))
        self.pbVeriOnisleme.setText(_translate("MainWindow", "Haz??rla"))
        self.cbVeriArtirimi.setText(_translate("MainWindow", "Veri Art??r??m?? Uygula"))
        self.label.setText(_translate("MainWindow", "Bu ad??mda HE ve CLAHE i??lemleri yap??lacakt??r"))
        self.groupBox_2.setTitle(_translate("MainWindow", "??rnek G??r??nt??ler"))
        self.lblOrnekGorsel.setText(_translate("MainWindow", "1.??rnek G??r??nt??"))
        self.lblOrnekGorsel2.setText(_translate("MainWindow", "2.??rnek G??r??nt??"))
        self.lblOrnekGorsel3.setText(_translate("MainWindow", "3.??rnek G??r??nt??"))
        self.groupBox_3.setTitle(_translate("MainWindow", "E??itme ????lemleri"))
        self.pbTrainTransferLearning.setText(_translate("MainWindow", "Transfer Learning ile E??it "))
        self.pbCML.setText(_translate("MainWindow", "Klasik Makine ????renimi ??le E??it"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Veri ??ni??leme ve HE | CLAHE"))
        self.lblAccuracy.setText(_translate("MainWindow", "Makinenizi ????rettikten sonra Accuracy Grafi??i\n"
"buraya gelecektir.\n"
"(Transfer Learning)"))
        self.lblLoss.setText(_translate("MainWindow", "Makinenizi ????rettikten sonra Loss Grafi??i\n"
"buraya gelecektir.\n"
"(Transfer Learning)"))
        self.lblROC.setText(_translate("MainWindow", "Makinenizi ????rettikten sonra  ROC E??risi Grafi??i\n"
"buraya gelecektir."))
        self.lblKarmasiklikMatrisi.setText(_translate("MainWindow", "Makinenizi ????rettikten sonra  Karma????kl??k Matrisi\n"
"(Confusion Matrix)buraya gelecektir."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Raporlama"))
        self.pbTahminEtGorsel.setText(_translate("MainWindow", "Resim Se??iniz..."))
        self.lblDataReadTahmin.setText(_translate("MainWindow", "Tahmin etmek istedi??iniz foto??raf?? \"Resim Se??iniz...\" buttonundan se??ip\n"
"\"Tahmin Et\" buttonuna t??klaman??z gerekmektedir."))
        self.lblAcc.setText(_translate("MainWindow", "Accuracy:"))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", "Tahmin Edilen:"))
        self.pbTahminEt.setText(_translate("MainWindow", "Tahmin Et"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tahmin Etme"))
        #Nesne Events
        self.pbVeriOkuma.clicked.connect(self.pbVeriOkumaClick)
        self.pbVeriOnisleme.clicked.connect(self.pbVeriOnislemeClick)
        self.pbTrainTransferLearning.clicked.connect(self.pbTrainTransferLearningClick)
        self.pbCML.clicked.connect(self.pbCMLClick)
        self.pbTahminEtGorsel.clicked.connect(self.pbTahminEtGorselClick)
        self.pbTahminEt.clicked.connect(self.pbTahminEtClick)
        #De??i??kenler
        self.labeled = []
        self.he = []
        self.CLAhe = []
        self.array = []
        self.veriler = []
        self.etiketler = []
        self.uzanti = []
        self.X_train = []
        self.X_test = []
        self.y_train = []
        self.y_test = []
        self.im_Size = (150,150)
        self.isClassic = False
        self.TahminEdilecekFotografinUzantisi = None

    #Buttonlar??n Clickleri
    def pbTahminEtClick(self):
        if self.isClassic:
            self.ClasicPrediction(self.TahminEdilecekFotografinUzantisi)
        else:
            self.prediction(self.TahminEdilecekFotografinUzantisi)

    def pbTahminEtGorselClick(self):
        fotograf = str(QtWidgets.QFileDialog.getOpenFileName(self, "Resiminizi se??in")[0])
        self.lblDataReadTahmin.setPixmap(QtGui.QPixmap(fotograf))
        self.TahminEdilecekFotografinUzantisi = fotograf
    def pbVeriOkumaClick(self):
        try:
            folder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Resim klas??r??n??z?? se??in"))
            folder = folder + "/"
            self.teFolderName.setPlainText(folder)
            self.dataRead(folder)
        except Exception as e:
            print(e)

    def pbVeriOnislemeClick(self):
        if self.cbVeriArtirimi.isChecked():
            self.veriArtirma()
        self.histogramE()
        self.CLAhistogramE()
        self.birlestirme()

    def pbTrainTransferLearningClick(self):
        print("Transfer Learning ????lemi Ba??lad??.")
        self.isClassic = False
        inputs = keras.Input(shape=(150, 150, 3))
        x = self.base_model(inputs, training=False)
        x = keras.layers.GlobalMaxPooling2D()(x)
        outputs = keras.layers.Dense(4, activation="softmax")(x)
        model = keras.Model(inputs, outputs)
        model.compile(optimizer="adam",  # hep Adam
                      loss="categorical_crossentropy",
                      metrics=["accuracy"])
        result = model.fit(self.X_train, self.y_train, batch_size=128, epochs=10, verbose=1,
                           validation_data=(self.X_test, self.y_test))
        self.GlobalModel = model

        # B
        y_pred = model.predict(self.X_test, batch_size=128)
        y_pred = np.argmax(y_pred, axis=1)
        y_test_encoded = np.argmax(self.y_test, axis=1)
        classificationResult = classification_report(y_test_encoded, y_pred,
                                                     target_names=["cloudy", "rain", "sunrise", "shine"])
        confusionMatrix = confusion_matrix(y_test_encoded, y_pred)
        pyp.figure(figsize=(5, 3))
        sns.set(font_scale=1)
        canvas = sns.heatmap(confusionMatrix, annot=True, xticklabels=["cloudy", "rain", "sunrise", "shine"],
                             yticklabels=["cloudy", "rain", "sunrise", "shine"],
                             cmap="RdGy", linewidths=1, linecolor="black", fmt=".0f")
        pyp.yticks(rotation=0)
        pyp.xlabel("Tahmin Sonu??lar??:")
        pyp.ylabel("Ger??ek Sonu??lar:")
        canvas.xaxis.set_ticks_position("top")
        pyp.title("Kar??????kl??k Matrisi")
        pyp.savefig("karmasiklikMatris.png")
        pyp.cla()
        pyp.clf()

        falsePositive = dict()
        truePositive = dict()
        aucRoc = dict()
        y_pred_oneHot = to_categorical(y_pred)
        for i in range(4):
            falsePositive[i], truePositive[i], c = roc_curve(self.y_test[:, i], y_pred_oneHot[:, i])
            aucRoc[i] = auc(falsePositive[i], truePositive[i])

        falsePositive["min"], truePositive["min"], c = roc_curve(self.y_test.ravel(), y_pred_oneHot.ravel())
        aucRoc["min"] = auc(falsePositive["min"], truePositive["min"])
        fp_all = np.unique(np.concatenate([falsePositive[i] for i in range(4)]))
        tp_ort = np.zeros_like(fp_all)
        for i in range(4):
            tp_ort += np.interp(fp_all, falsePositive[i], truePositive[i])
        tp_ort = tp_ort / 4
        falsePositive["max"] = fp_all
        truePositive["max"] = tp_ort
        aucRoc["max"] = auc(falsePositive["max"], truePositive["max"])
        pyp.plot(result.history["accuracy"])
        pyp.plot(result.history["val_accuracy"])
        pyp.ylabel("accuracy")
        pyp.xlabel("epoch")
        pyp.legend(["train", "test"], loc="upper left")
        pyp.savefig("Accuracy.png")
        pyp.cla()
        pyp.clf()

        pyp.plot(result.history["loss"])
        pyp.plot(result.history["val_loss"])
        pyp.ylabel("loss")
        pyp.xlabel("epoch")
        pyp.legend(["train", "test"], loc="upper left")
        pyp.savefig("Loss.png")
        pyp.cla()
        pyp.clf()

        pyp.figure()
        pyp.plot(falsePositive["min"], truePositive["min"],
                 label="Minimum Ortalama ROC E??risi (Alan={0:0.2f})".format(aucRoc["min"]), color="navy", linestyle=":",
                 linewidth=4)
        pyp.plot(falsePositive["max"], truePositive["max"],
                 label="Maksimum Ortalama ROC E??risi (Alan={0:0.2f})".format(aucRoc["max"]), color="deeppink",
                 linestyle=":", linewidth=4)
        colors = cycle(["cornflowerblue", "aqua", "darkorange"])

        for i, color in zip(range(4), colors):
            pyp.plot(falsePositive[i], truePositive[i], color=color, lw=2,
                     label='{0}. s??n??f??n ROC e??risi (Alan = {1:0.2f})'
                           ''.format(i, aucRoc[i]))

        pyp.plot([0, 1], [0, 1], 'k--', lw=2)
        pyp.xlim([0.0, 1.0])
        pyp.ylim([0.0, 1.05])
        pyp.xlabel('False Positive Rate')
        pyp.ylabel('True Positive Rate')
        pyp.title('Some extension of Receiver operating characteristic to multi-class')
        pyp.legend(loc="lower right")
        pyp.savefig("ROCegrisi.png")
        pyp.cla()
        pyp.clf()
        self.lblROC.setPixmap(QtGui.QPixmap("./ROCegrisi.png"))
        self.lblKarmasiklikMatrisi.setPixmap(QtGui.QPixmap("./karmasiklikMatris.png"))
        self.lblLoss.setPixmap(QtGui.QPixmap("./Loss.png"))
        self.lblAccuracy.setPixmap(QtGui.QPixmap("./Accuracy.png"))
        print("Transfer Learning ????lemi Bitti.")
    def pbCMLClick(self):
        print("Klasik Makine ????renmesi ????lemi Ba??lad??.")
        self.isClassic = True
        xfeatureExtractor = self.base_model.predict(self.X_train)  # FE
        X_train_features = xfeatureExtractor.reshape(xfeatureExtractor.shape[0], -1)
        xTefeatureExtractor = self.base_model.predict(self.X_test)  # FE
        X_test_features = xTefeatureExtractor.reshape(xTefeatureExtractor.shape[0], -1)
        rfModel = RandomForestClassifier(random_state=30, n_estimators=40)  # klasik makine ????renmesi algoritmas??
        self.mainExtractor = self.base_model
        rfModel.fit(X_train_features, self.y_train)
        self.GlobalModel = rfModel

        y_Tahmin = rfModel.predict(X_test_features)
        yTest = np.argmax(self.y_test, axis=1)
        yTahmin = np.argmax(y_Tahmin, axis=1)
        confusionMatrix = confusion_matrix(yTest, yTahmin)
        pyp.figure(figsize=(5, 3))
        sns.set(font_scale=1)
        canvas = sns.heatmap(confusionMatrix, annot=True, xticklabels=["cloudy", "rain", "sunrise", "shine"],
                             yticklabels=["cloudy", "rain", "sunrise", "shine"],
                             cmap="RdGy", linewidths=1, linecolor="black", fmt=".0f")
        pyp.yticks(rotation=0)
        pyp.xlabel("Tahmin Sonu??lar??:")
        pyp.ylabel("Ger??ek Sonu??lar:")
        canvas.xaxis.set_ticks_position("top")
        pyp.title("Kar??????kl??k Matrisi")
        pyp.savefig("karmasiklikMatrisCML.png")
        pyp.cla()
        pyp.clf()

        falsePositive = dict()
        truePositive = dict()
        aucRoc = dict()
        for i in range(4):
            falsePositive[i], truePositive[i], c = roc_curve(self.y_test[:, i], y_Tahmin[:, i])
            aucRoc[i] = auc(falsePositive[i], truePositive[i])

        falsePositive["min"], truePositive["min"], c = roc_curve(self.y_test.ravel(), y_Tahmin.ravel())
        aucRoc["min"] = auc(falsePositive["min"], truePositive["min"])
        fp_all = np.unique(np.concatenate([falsePositive[i] for i in range(4)]))
        tp_ort = np.zeros_like(fp_all)
        for i in range(4):
            tp_ort += np.interp(fp_all, falsePositive[i], truePositive[i])
        tp_ort = tp_ort / 4
        falsePositive["max"] = fp_all
        truePositive["max"] = tp_ort
        aucRoc["max"] = auc(falsePositive["max"], truePositive["max"])

        pyp.figure()
        pyp.plot(falsePositive["min"], truePositive["min"],
                 label="Minimum Ortalama ROC E??risi (Alan={0:0.2f})".format(aucRoc["min"]), color="navy",
                 linestyle=":", linewidth=4)
        pyp.plot(falsePositive["max"], truePositive["max"],
                 label="Maksimum Ortalama ROC E??risi (Alan={0:0.2f})".format(aucRoc["max"]), color="deeppink",
                 linestyle=":", linewidth=4)
        colors = cycle(["cornflowerblue", "aqua", "darkorange"])

        for i, color in zip(range(4), colors):
            pyp.plot(falsePositive[i], truePositive[i], color=color, lw=2,
                     label='{0}. s??n??f??n ROC e??risi (Alan = {1:0.2f})'
                           ''.format(i, aucRoc[i]))
        pyp.plot([0, 1], [0, 1], 'k--', lw=2)
        pyp.xlim([0.0, 1.0])
        pyp.ylim([0.0, 1.05])
        pyp.xlabel('False Positive Rate')
        pyp.ylabel('True Positive Rate')
        pyp.title('Some extension of Receiver operating characteristic to multi-class')
        pyp.legend(loc="lower right")
        pyp.savefig("ROCegrisiCML.png")
        pyp.cla()
        pyp.clf()
        self.lblROC.setPixmap(QtGui.QPixmap("./ROCegrisiCML.png"))
        self.lblKarmasiklikMatrisi.setPixmap(QtGui.QPixmap("./karmasiklikMatrisCML.png"))
        self.lblAccuracy.setPixmap(QtGui.QPixmap("./bos.png"))
        self.lblLoss.setPixmap(QtGui.QPixmap("./bos.png"))
        print("Klasik Makine ????renmesi ????lemi Bitti.")

    #Harici Fonksiyonlar??m??z

    def prediction(self,image):
        image = cv.imread(image)
        image = cv.cvtColor(image,cv.COLOR_BGR2RGB)
        image = Image.fromarray(image,"RGB")
        image = image.resize(self.im_Size)
        image = np.array(image)
        image = image / 255
        veri = []
        veri.append(image)
        veri = np.array(veri)
        point = self.GlobalModel.predict(veri,verbose=1)
        etiket = np.argmax(point)
        accuracy = np.max(point)
        self.lblAcc.setText("%"+str(accuracy*100))
        if etiket == 0:
            self.lblTahminEtiket.setText("Bulutlu")
        elif etiket == 1:
            self.lblTahminEtiket.setText("Ya??murlu")
        elif etiket == 2:
            self.lblTahminEtiket.setText("G??ndo??umu")
        else:
            self.lblTahminEtiket.setText("G??ne??li")
        self.lblGercekEtiket.setText("Transfer Learning")

    def ClasicPrediction(self,image):
        image = cv.imread(image)
        image = cv.cvtColor(image,cv.COLOR_BGR2RGB)
        image = Image.fromarray(image,"RGB")
        image = image.resize(self.im_Size)
        image = np.array(image)
        image = image / 255
        input = np.expand_dims(image,axis=0)
        features = self.mainExtractor.predict(input)
        features = features.reshape(features.shape[0],-1)
        tahmin = self.GlobalModel.predict(features)[0]
        etiket = np.argmax(tahmin)
        if etiket == 0:
            self.lblTahminEtiket.setText("Bulutlu")
        elif etiket == 1:
            self.lblTahminEtiket.setText("Ya??murlu")
        elif etiket == 2:
            self.lblTahminEtiket.setText("G??ndo??umu")
        else:
            self.lblTahminEtiket.setText("G??ne??li")
        self.lblAcc.setText("")
        self.lblGercekEtiket.setText("Klasik Makine ????renmesi")
    #Veri Okuma ????lemleri
    def birlestirme(self):
        self.labeled = np.array(self.labeled)
        self.he = np.array(self.he)
        self.CLAhe = np.array(self.CLAhe)
        self.array = np.array(np.concatenate((self.he, self.CLAhe)))
        birlestirilmis = np.concatenate((self.labeled, self.array))
        indisler = np.arange(len(birlestirilmis))
        np.random.shuffle(indisler)
        birlestirilmis = birlestirilmis[indisler]
        self.labeled = birlestirilmis
        for i, x in enumerate(self.labeled):
            self.veriler.append(np.array(self.labeled[i][0]))
            self.etiketler.append(self.labeled[i][1])
            self.uzanti.append(self.labeled[i][2])
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.veriler, self.etiketler, test_size=0.2)
        self.X_train = np.array(self.X_train)
        self.X_test = np.array(self.X_test)

        self.y_train = to_categorical(self.y_train)
        self.y_test = to_categorical(self.y_test)
        self.X_train = self.X_train.astype("float32") / 255
        self.X_test = self.X_test.astype("float32") / 255

        self.base_model = keras.applications.Xception(
            weights='imagenet',  # Load weights pre-trained on ImageNet.
            input_shape=(150, 150, 3),
            include_top=False)
        self.base_model.trainable = False


    def dataRead(self,folder):
        data = glob.glob(folder + "*")
        data = [x.replace('\\', '/') for x in data]
        folder = folder.replace("\\","/")
        print("Veri Okuma ????lemi Ba??lat??ld??.")
        print("Veri Say??s??:"+str(len(data)))
        for i, x in enumerate(data):
            try:
                image = cv.imread(x)
                imArray = Image.fromarray(image, "RGB")
                image =np.array(imArray.resize(self.im_Size))
                if data[i].startswith(folder + "cloudy"):
                    self.labeled.append([image, 0, os.path.basename(x)])
                elif data[i].startswith(folder + "rain"):
                    self.labeled.append([image, 1, os.path.basename(x)])
                elif data[i].startswith(folder + "sunrise"):
                    self.labeled.append([image, 2, os.path.basename(x)])
                elif data[i].startswith(folder + "shine"):
                    self.labeled.append([image, 3, os.path.basename(x)])
            except Exception as e:
                print("Bu veri okunam??yor!!")
        data_count = pd.DataFrame(self.labeled, columns=["image", "etiket", "filename"])
        pyp.figure(figsize=(20, 5))
        pyp.subplot(1, 1, 1)
        sns.countplot(data_count["etiket"])
        pyp.title('Veriler')
        pyp.savefig("./EtiketGrafigi/Etiketler.png")
        self.labelDataRead.setPixmap(QtGui.QPixmap("./EtiketGrafigi/Etiketler.png"))
        print("Veri Okuma ????lemi Bitti.")

    # Histogram E??itleme
    def histogramE(self):
        print("Histogram E??itleme i??lemi ba??lat??ld??-->")
        for im in self.labeled:
            try:
                image = im[0]
                img_yuv = cv.cvtColor(image, cv.COLOR_RGB2YUV)
                img_yuv[:, :, 0] = cv.equalizeHist(img_yuv[:, :, 0])
                he_img = cv.cvtColor(img_yuv, cv.COLOR_YUV2RGB)
                self.he.append([he_img, im[1], None])
            except Exception as e:
                print("Histogram E??itlemede bu veri okunam??yor!!")
        print("Histogram E??itleme i??lemi bitti<--")

    # CLAHistogram E??itleme
    def CLAhistogramE(self):
        print("Contrast Limited Adaptive Histogram E??itleme(CLAHE) i??lemi ba??lat??ld??-->")
        for im in self.labeled:
            try:
                image = im[0]
                img_yuv = cv.cvtColor(image, cv.COLOR_RGB2YUV)
                clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
                img_yuv[:, :, 0] = clahe.apply(img_yuv[:, :, 0])
                CLAhe_img = cv.cvtColor(img_yuv, cv.COLOR_YUV2RGB)
                self.CLAhe.append([CLAhe_img, im[1], None])
            except Exception as e:
                print("CLAHE'de bu veri okunam??yor!!")
        print("Contrast Limited Adaptive Histogram E??itleme(CLAHE) i??lemi bitti<--")

    #Veri Art??rma
    def veriArtirma(self):
        augmentated_path = "augDatas"
        if os.path.exists(augmentated_path):
            shutil.rmtree(augmentated_path)
        os.mkdir(augmentated_path)
        for img in self.labeled:
            try:
                image = img[0]
                datagen = ImageDataGenerator(
                    rotation_range= 60, width_shift_range= 0.2, height_shift_range= 0.2, shear_range=0.4, zoom_range=0.5,horizontal_flip = True,
                    vertical_flip=True,fill_mode= "nearest"
                )
                a = img_to_array(image)
                a = a.reshape((1,)+a.shape)
                i = 0
                img_format, img_name = img[2][::-1].split(".", 1)
                img_name = img_name[::-1]
                img_format = img_format[::-1]
                for batch in datagen.flow(a, batch_size=1, save_to_dir=(augmentated_path),
                                          save_prefix=img_name, save_format=img_format):
                    i += 1
                    if i > 1:
                        break
            except Exception as e:
                print(e)
        folder = os.path.join(os.path.dirname(os.path.abspath(__file__)),augmentated_path+"/")
        self.dataRead(folder)