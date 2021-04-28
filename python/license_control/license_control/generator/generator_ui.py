# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kiven/code/my_utils/python/license_control/license_control/generator/generator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LicenseGeneratorDialog(object):
    def setupUi(self, LicenseGeneratorDialog):
        LicenseGeneratorDialog.setObjectName("LicenseGeneratorDialog")
        LicenseGeneratorDialog.resize(400, 475)
        self.gridLayout_2 = QtWidgets.QGridLayout(LicenseGeneratorDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.record_list_view = QtWidgets.QListView(LicenseGeneratorDialog)
        self.record_list_view.setObjectName("record_list_view")
        self.gridLayout_2.addWidget(self.record_list_view, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(LicenseGeneratorDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.saved_dir_line = QtWidgets.QLineEdit(LicenseGeneratorDialog)
        self.saved_dir_line.setObjectName("saved_dir_line")
        self.gridLayout.addWidget(self.saved_dir_line, 5, 1, 1, 1)
        self.saved_dir_button = QtWidgets.QPushButton(LicenseGeneratorDialog)
        self.saved_dir_button.setMinimumSize(QtCore.QSize(55, 0))
        self.saved_dir_button.setObjectName("saved_dir_button")
        self.gridLayout.addWidget(self.saved_dir_button, 5, 2, 1, 1)
        self.product_name_line = QtWidgets.QLineEdit(LicenseGeneratorDialog)
        self.product_name_line.setEnabled(True)
        self.product_name_line.setReadOnly(True)
        self.product_name_line.setObjectName("product_name_line")
        self.gridLayout.addWidget(self.product_name_line, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(LicenseGeneratorDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.mac_addr_text = QtWidgets.QTextEdit(LicenseGeneratorDialog)
        self.mac_addr_text.setObjectName("mac_addr_text")
        self.gridLayout.addWidget(self.mac_addr_text, 1, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(LicenseGeneratorDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.change_state_button = QtWidgets.QPushButton(LicenseGeneratorDialog)
        self.change_state_button.setMinimumSize(QtCore.QSize(55, 0))
        self.change_state_button.setObjectName("change_state_button")
        self.gridLayout.addWidget(self.change_state_button, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(LicenseGeneratorDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.datetime_edit = QtWidgets.QDateTimeEdit(LicenseGeneratorDialog)
        self.datetime_edit.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.datetime_edit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.datetime_edit.setProperty("showGroupSeparator", False)
        self.datetime_edit.setCalendarPopup(True)
        self.datetime_edit.setObjectName("datetime_edit")
        self.gridLayout.addWidget(self.datetime_edit, 4, 1, 1, 2)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 9)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(LicenseGeneratorDialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.create_button = QtWidgets.QPushButton(LicenseGeneratorDialog)
        self.create_button.setObjectName("create_button")
        self.horizontalLayout.addWidget(self.create_button)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(LicenseGeneratorDialog)
        QtCore.QMetaObject.connectSlotsByName(LicenseGeneratorDialog)

    def retranslateUi(self, LicenseGeneratorDialog):
        _translate = QtCore.QCoreApplication.translate
        LicenseGeneratorDialog.setWindowTitle(_translate("LicenseGeneratorDialog", "Licese Generator"))
        self.label.setText(_translate("LicenseGeneratorDialog", "Product Name"))
        self.saved_dir_button.setText(_translate("LicenseGeneratorDialog", "..."))
        self.product_name_line.setText(_translate("LicenseGeneratorDialog", "SCI"))
        self.label_3.setText(_translate("LicenseGeneratorDialog", "Saved Dir."))
        self.mac_addr_text.setToolTip(_translate("LicenseGeneratorDialog", "<html><head/><body><p>you can input multiple mac addresses, splited by LF.</p></body></html>"))
        self.label_2.setText(_translate("LicenseGeneratorDialog", "MAC addr."))
        self.change_state_button.setText(_translate("LicenseGeneratorDialog", "Enable"))
        self.label_4.setText(_translate("LicenseGeneratorDialog", "Expiration Date"))
        self.datetime_edit.setDisplayFormat(_translate("LicenseGeneratorDialog", "yyyy-MM-dd hh:mm:ss"))
        self.label_5.setText(_translate("LicenseGeneratorDialog", "Auth Records"))
        self.create_button.setText(_translate("LicenseGeneratorDialog", "Create License"))
