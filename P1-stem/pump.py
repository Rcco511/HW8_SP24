# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pump.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2000, 2000)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.GB_Input = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GB_Input.sizePolicy().hasHeightForWidth())
        self.GB_Input.setSizePolicy(sizePolicy)
        self.GB_Input.setMaximumSize(QtCore.QSize(16777215, 13500))
        self.GB_Input.setObjectName("GB_Input")
        self.gridLayout = QtWidgets.QGridLayout(self.GB_Input)
        self.gridLayout.setObjectName("gridLayout")
        self.LBL_Filename = QtWidgets.QLabel(self.GB_Input)
        self.LBL_Filename.setObjectName("LBL_Filename")
        self.gridLayout.addWidget(self.LBL_Filename, 0, 0, 1, 1)
        self.TE_Filename = QtWidgets.QTextEdit(self.GB_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TE_Filename.sizePolicy().hasHeightForWidth())
        self.TE_Filename.setSizePolicy(sizePolicy)
        self.TE_Filename.setMinimumSize(QtCore.QSize(0, 20))
        self.TE_Filename.setBaseSize(QtCore.QSize(0, 50))
        self.TE_Filename.setObjectName("TE_Filename")
        self.gridLayout.addWidget(self.TE_Filename, 0, 1, 1, 1)
        self.CMD_Open = QtWidgets.QPushButton(self.GB_Input)
        self.CMD_Open.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CMD_Open.sizePolicy().hasHeightForWidth())
        self.CMD_Open.setSizePolicy(sizePolicy)
        self.CMD_Open.setObjectName("CMD_Open")
        self.gridLayout.addWidget(self.CMD_Open, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.GB_Input)
        self.GB_Output = QtWidgets.QGroupBox(Form)
        self.GB_Output.setObjectName("GB_Output")
        self.GL_Output = QtWidgets.QGridLayout(self.GB_Output)
        self.GL_Output.setObjectName("GL_Output")
        self.LE_EffCoefs = QtWidgets.QLineEdit(self.GB_Output)
        self.LE_EffCoefs.setObjectName("LE_EffCoefs")
        self.GL_Output.addWidget(self.LE_EffCoefs, 3, 1, 1, 3)
        self.LBL_HeadUnits = QtWidgets.QLabel(self.GB_Output)
        self.LBL_HeadUnits.setObjectName("LBL_HeadUnits")
        self.GL_Output.addWidget(self.LBL_HeadUnits, 1, 2, 1, 1)
        self.LBL_HeadCoefs = QtWidgets.QLabel(self.GB_Output)
        self.LBL_HeadCoefs.setObjectName("LBL_HeadCoefs")
        self.GL_Output.addWidget(self.LBL_HeadCoefs, 2, 0, 1, 1)
        self.LBL_EffCoefs = QtWidgets.QLabel(self.GB_Output)
        self.LBL_EffCoefs.setObjectName("LBL_EffCoefs")
        self.GL_Output.addWidget(self.LBL_EffCoefs, 3, 0, 1, 1)
        self.LE_HeadCoefs = QtWidgets.QLineEdit(self.GB_Output)
        self.LE_HeadCoefs.setObjectName("LE_HeadCoefs")
        self.GL_Output.addWidget(self.LE_HeadCoefs, 2, 1, 1, 3)
        self.LE_PumpName = QtWidgets.QLineEdit(self.GB_Output)
        self.LE_PumpName.setObjectName("LE_PumpName")
        self.GL_Output.addWidget(self.LE_PumpName, 0, 1, 1, 3)
        self.LE_FlowUnits = QtWidgets.QLineEdit(self.GB_Output)
        self.LE_FlowUnits.setObjectName("LE_FlowUnits")
        self.GL_Output.addWidget(self.LE_FlowUnits, 1, 1, 1, 1)
        self.LBL_PumpName = QtWidgets.QLabel(self.GB_Output)
        self.LBL_PumpName.setObjectName("LBL_PumpName")
        self.GL_Output.addWidget(self.LBL_PumpName, 0, 0, 1, 1)
        self.LBL_FlowUnits = QtWidgets.QLabel(self.GB_Output)
        self.LBL_FlowUnits.setObjectName("LBL_FlowUnits")
        self.GL_Output.addWidget(self.LBL_FlowUnits, 1, 0, 1, 1)
        self.LE_HeadUnits = QtWidgets.QLineEdit(self.GB_Output)
        self.LE_HeadUnits.setObjectName("LE_HeadUnits")
        self.GL_Output.addWidget(self.LE_HeadUnits, 1, 3, 1, 1)
        self.W_Plot = QtWidgets.QWidget(self.GB_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.W_Plot.sizePolicy().hasHeightForWidth())
        self.W_Plot.setSizePolicy(sizePolicy)
        self.W_Plot.setObjectName("W_Plot")
        self.GL_Output.addWidget(self.W_Plot, 5, 0, 1, 4)
        self.PB_Exit = QtWidgets.QPushButton(self.GB_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_Exit.sizePolicy().hasHeightForWidth())
        self.PB_Exit.setSizePolicy(sizePolicy)
        self.PB_Exit.setObjectName("PB_Exit")
        self.GL_Output.addWidget(self.PB_Exit, 6, 2, 1, 1)
        self.verticalLayout.addWidget(self.GB_Output)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.GB_Input.setTitle(_translate("Form", "Input"))
        self.LBL_Filename.setText(_translate("Form", "Filename"))
        self.CMD_Open.setText(_translate("Form", "Read File and Calculate"))
        self.GB_Output.setTitle(_translate("Form", "Output"))
        self.LBL_HeadUnits.setText(_translate("Form", "Head Units"))
        self.LBL_HeadCoefs.setText(_translate("Form", "Head Coefficients"))
        self.LBL_EffCoefs.setText(_translate("Form", "Efficiency Coefficients"))
        self.LBL_PumpName.setText(_translate("Form", "Pump Name"))
        self.LBL_FlowUnits.setText(_translate("Form", "Flow Units"))
        self.PB_Exit.setText(_translate("Form", "Exit"))

