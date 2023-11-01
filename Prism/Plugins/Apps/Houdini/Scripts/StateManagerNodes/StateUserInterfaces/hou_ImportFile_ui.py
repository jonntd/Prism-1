# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hou_ImportFile.ui'
#
# Created: Tue Mar  7 11:17:44 2023
#      by: qtpy-uic 2.0.5
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_wg_ImportFile(object):
    def setupUi(self, wg_ImportFile):
        wg_ImportFile.setObjectName("wg_ImportFile")
        wg_ImportFile.resize(340, 372)
        self.verticalLayout = QtWidgets.QVBoxLayout(wg_ImportFile)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(wg_ImportFile)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 18, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l_name = QtWidgets.QLabel(self.widget_4)
        self.l_name.setObjectName("l_name")
        self.horizontalLayout_2.addWidget(self.l_name)
        self.e_name = QtWidgets.QLineEdit(self.widget_4)
        self.e_name.setMinimumSize(QtCore.QSize(0, 0))
        self.e_name.setMaximumSize(QtCore.QSize(9999, 16777215))
        self.e_name.setObjectName("e_name")
        self.horizontalLayout_2.addWidget(self.e_name)
        self.l_class = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.l_class.setFont(font)
        self.l_class.setObjectName("l_class")
        self.horizontalLayout_2.addWidget(self.l_class)
        self.verticalLayout.addWidget(self.widget_4)
        self.gb_import = QtWidgets.QGroupBox(wg_ImportFile)
        self.gb_import.setObjectName("gb_import")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gb_import)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.gb_import)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.w_currentVersion = QtWidgets.QWidget(self.groupBox)
        self.w_currentVersion.setObjectName("w_currentVersion")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.w_currentVersion)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.w_currentVersion)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.l_curVersion = QtWidgets.QLabel(self.w_currentVersion)
        self.l_curVersion.setObjectName("l_curVersion")
        self.horizontalLayout_5.addWidget(self.l_curVersion)
        self.verticalLayout_3.addWidget(self.w_currentVersion)
        self.w_latestVersion = QtWidgets.QWidget(self.groupBox)
        self.w_latestVersion.setObjectName("w_latestVersion")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.w_latestVersion)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.w_latestVersion)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.l_latestVersion = QtWidgets.QLabel(self.w_latestVersion)
        self.l_latestVersion.setObjectName("l_latestVersion")
        self.horizontalLayout_6.addWidget(self.l_latestVersion)
        self.verticalLayout_3.addWidget(self.w_latestVersion)
        self.w_autoUpdate = QtWidgets.QWidget(self.groupBox)
        self.w_autoUpdate.setObjectName("w_autoUpdate")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.w_autoUpdate)
        self.horizontalLayout_14.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.l_autoUpdate = QtWidgets.QLabel(self.w_autoUpdate)
        self.l_autoUpdate.setObjectName("l_autoUpdate")
        self.horizontalLayout_14.addWidget(self.l_autoUpdate)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem2)
        self.chb_autoUpdate = QtWidgets.QCheckBox(self.w_autoUpdate)
        self.chb_autoUpdate.setText("")
        self.chb_autoUpdate.setChecked(False)
        self.chb_autoUpdate.setObjectName("chb_autoUpdate")
        self.horizontalLayout_14.addWidget(self.chb_autoUpdate)
        self.verticalLayout_3.addWidget(self.w_autoUpdate)
        self.w_importLatest = QtWidgets.QWidget(self.groupBox)
        self.w_importLatest.setObjectName("w_importLatest")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.w_importLatest)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.b_browse = QtWidgets.QPushButton(self.w_importLatest)
        self.b_browse.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_browse.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_browse.setObjectName("b_browse")
        self.horizontalLayout_7.addWidget(self.b_browse)
        self.b_importLatest = QtWidgets.QPushButton(self.w_importLatest)
        self.b_importLatest.setMinimumSize(QtCore.QSize(0, 0))
        self.b_importLatest.setMaximumSize(QtCore.QSize(99999, 16777215))
        self.b_importLatest.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_importLatest.setObjectName("b_importLatest")
        self.horizontalLayout_7.addWidget(self.b_importLatest)
        self.verticalLayout_3.addWidget(self.w_importLatest)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gb_import)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setMinimumSize(QtCore.QSize(40, 0))
        self.label.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.l_status = QtWidgets.QLabel(self.widget_3)
        self.l_status.setAlignment(QtCore.Qt.AlignCenter)
        self.l_status.setObjectName("l_status")
        self.horizontalLayout_4.addWidget(self.l_status)
        self.b_goTo = QtWidgets.QPushButton(self.widget_3)
        self.b_goTo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_goTo.setObjectName("b_goTo")
        self.horizontalLayout_4.addWidget(self.b_goTo)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b_import = QtWidgets.QPushButton(self.widget_2)
        self.b_import.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_import.setObjectName("b_import")
        self.horizontalLayout_3.addWidget(self.b_import)
        self.b_objMerge = QtWidgets.QPushButton(self.widget_2)
        self.b_objMerge.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_objMerge.setObjectName("b_objMerge")
        self.horizontalLayout_3.addWidget(self.b_objMerge)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.gb_options = QtWidgets.QGroupBox(self.gb_import)
        self.gb_options.setObjectName("gb_options")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.gb_options)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.f_updateOnly = QtWidgets.QWidget(self.gb_options)
        self.f_updateOnly.setObjectName("f_updateOnly")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.f_updateOnly)
        self.horizontalLayout_16.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.l_updateOnly = QtWidgets.QLabel(self.f_updateOnly)
        self.l_updateOnly.setObjectName("l_updateOnly")
        self.horizontalLayout_16.addWidget(self.l_updateOnly)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem3)
        self.chb_updateOnly = QtWidgets.QCheckBox(self.f_updateOnly)
        self.chb_updateOnly.setText("")
        self.chb_updateOnly.setChecked(True)
        self.chb_updateOnly.setObjectName("chb_updateOnly")
        self.horizontalLayout_16.addWidget(self.chb_updateOnly)
        self.verticalLayout_6.addWidget(self.f_updateOnly)
        self.f_nameSpaces = QtWidgets.QWidget(self.gb_options)
        self.f_nameSpaces.setObjectName("f_nameSpaces")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.f_nameSpaces)
        self.horizontalLayout_12.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.l_keepRefEdits_2 = QtWidgets.QLabel(self.f_nameSpaces)
        self.l_keepRefEdits_2.setObjectName("l_keepRefEdits_2")
        self.horizontalLayout_12.addWidget(self.l_keepRefEdits_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.chb_autoNameSpaces = QtWidgets.QCheckBox(self.f_nameSpaces)
        self.chb_autoNameSpaces.setChecked(False)
        self.chb_autoNameSpaces.setObjectName("chb_autoNameSpaces")
        self.horizontalLayout_12.addWidget(self.chb_autoNameSpaces)
        spacerItem5 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem5)
        self.b_nameSpaces = QtWidgets.QPushButton(self.f_nameSpaces)
        self.b_nameSpaces.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_nameSpaces.setObjectName("b_nameSpaces")
        self.horizontalLayout_12.addWidget(self.b_nameSpaces)
        self.verticalLayout_6.addWidget(self.f_nameSpaces)
        self.verticalLayout_2.addWidget(self.gb_options)
        self.verticalLayout.addWidget(self.gb_import)

        self.retranslateUi(wg_ImportFile)
        QtCore.QMetaObject.connectSlotsByName(wg_ImportFile)

    def retranslateUi(self, wg_ImportFile):
        wg_ImportFile.setWindowTitle(QtWidgets.QApplication.translate("", "ImportFile", None, -1))
        self.l_name.setText(QtWidgets.QApplication.translate("", "Name:", None, -1))
        self.l_class.setText(QtWidgets.QApplication.translate("", "ImportFile", None, -1))
        self.gb_import.setTitle(QtWidgets.QApplication.translate("", "Import", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("", "Version", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("", "Current Version:", None, -1))
        self.l_curVersion.setText(QtWidgets.QApplication.translate("", "-", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("", "Latest Version:", None, -1))
        self.l_latestVersion.setText(QtWidgets.QApplication.translate("", "-", None, -1))
        self.l_autoUpdate.setText(QtWidgets.QApplication.translate("", "Auto load latest version:", None, -1))
        self.b_browse.setText(QtWidgets.QApplication.translate("", "Browse", None, -1))
        self.b_importLatest.setText(QtWidgets.QApplication.translate("", "Import latest Version", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("", "Scene", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("", "Status:", None, -1))
        self.l_status.setText(QtWidgets.QApplication.translate("", "Not found in scene", None, -1))
        self.b_goTo.setText(QtWidgets.QApplication.translate("", "Go to Node", None, -1))
        self.b_import.setText(QtWidgets.QApplication.translate("", "Re-Import", None, -1))
        self.b_objMerge.setText(QtWidgets.QApplication.translate("", "Create Obj Merge", None, -1))
        self.gb_options.setTitle(QtWidgets.QApplication.translate("", "Options", None, -1))
        self.l_updateOnly.setText(QtWidgets.QApplication.translate("", "Update path only:", None, -1))
        self.l_keepRefEdits_2.setText(QtWidgets.QApplication.translate("", "Maya Namespaces:", None, -1))
        self.chb_autoNameSpaces.setText(QtWidgets.QApplication.translate("", "Auto", None, -1))
        self.b_nameSpaces.setText(QtWidgets.QApplication.translate("", "Remove", None, -1))

