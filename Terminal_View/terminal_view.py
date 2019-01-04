# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'terminal_view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Terminal(object):
    def setupUi(self, Terminal):
        Terminal.setObjectName("Terminal")
        Terminal.resize(816, 283)
        Terminal.setMinimumSize(QtCore.QSize(0, 283))
        self.horizontalLayoutWidget = QtWidgets.QWidget(Terminal)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 811, 281))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.serialPortComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.serialPortComboBox.setObjectName("serialPortComboBox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.serialPortComboBox)
        self.scanSerialPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.scanSerialPushButton.setObjectName("scanSerialPushButton")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.scanSerialPushButton)
        self.baudComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.baudComboBox.setObjectName("baudComboBox")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.baudComboBox)
        self.serialConnectPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.serialConnectPushButton.setObjectName("serialConnectPushButton")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.serialConnectPushButton)
        self.serialDisconnectPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.serialDisconnectPushButton.setObjectName("serialDisconnectPushButton")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.serialDisconnectPushButton)
        self.horizontalLayout.addLayout(self.formLayout_3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.serialTextBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.serialTextBrowser.setMinimumSize(QtCore.QSize(400, 0))
        self.serialTextBrowser.setObjectName("serialTextBrowser")
        self.verticalLayout_8.addWidget(self.serialTextBrowser)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cmdLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.cmdLineEdit.setObjectName("cmdLineEdit")
        self.horizontalLayout_4.addWidget(self.cmdLineEdit)
        self.sendCmdPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sendCmdPushButton.setObjectName("sendCmdPushButton")
        self.horizontalLayout_4.addWidget(self.sendCmdPushButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.startPingPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.startPingPushButton.setObjectName("startPingPushButton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.startPingPushButton)
        self.stopPingPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stopPingPushButton.setObjectName("stopPingPushButton")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.stopPingPushButton)
        self.breakPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.breakPushButton.setObjectName("breakPushButton")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.breakPushButton)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.recordPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.recordPushButton.setCheckable(True)
        self.recordPushButton.setObjectName("recordPushButton")
        self.gridLayout.addWidget(self.recordPushButton, 0, 0, 1, 1)
        self.bytesWrittenLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.bytesWrittenLabel.setText("")
        self.bytesWrittenLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bytesWrittenLabel.setObjectName("bytesWrittenLabel")
        self.gridLayout.addWidget(self.bytesWrittenLabel, 1, 0, 1, 1)
        self.clearConsolePushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.clearConsolePushButton.setObjectName("clearConsolePushButton")
        self.gridLayout.addWidget(self.clearConsolePushButton, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.clearBulkCmdPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.clearBulkCmdPushButton.setObjectName("clearBulkCmdPushButton")
        self.gridLayout_2.addWidget(self.clearBulkCmdPushButton, 1, 1, 1, 1)
        self.sendBulkCmdPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sendBulkCmdPushButton.setObjectName("sendBulkCmdPushButton")
        self.gridLayout_2.addWidget(self.sendBulkCmdPushButton, 1, 0, 1, 1)
        self.bulkCmdMlainTextEdit = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.bulkCmdMlainTextEdit.setObjectName("bulkCmdMlainTextEdit")
        self.gridLayout_2.addWidget(self.bulkCmdMlainTextEdit, 0, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(Terminal)
        QtCore.QMetaObject.connectSlotsByName(Terminal)

    def retranslateUi(self, Terminal):
        _translate = QtCore.QCoreApplication.translate
        Terminal.setWindowTitle(_translate("Terminal", "Form"))
        self.scanSerialPushButton.setText(_translate("Terminal", "SCAN"))
        self.serialConnectPushButton.setText(_translate("Terminal", "CONNECT"))
        self.serialDisconnectPushButton.setText(_translate("Terminal", "DISCONNECT"))
        self.sendCmdPushButton.setText(_translate("Terminal", "SEND"))
        self.startPingPushButton.setText(_translate("Terminal", "START PING"))
        self.stopPingPushButton.setText(_translate("Terminal", "STOP PING"))
        self.breakPushButton.setText(_translate("Terminal", "BREAK"))
        self.recordPushButton.setText(_translate("Terminal", "RECORD"))
        self.clearConsolePushButton.setText(_translate("Terminal", "CLEAR"))
        self.clearBulkCmdPushButton.setText(_translate("Terminal", "CLEAR"))
        self.sendBulkCmdPushButton.setText(_translate("Terminal", "SEND"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Terminal = QtWidgets.QWidget()
    ui = Ui_Terminal()
    ui.setupUi(Terminal)
    Terminal.show()
    sys.exit(app.exec_())
