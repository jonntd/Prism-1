# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hou_SaveHDA.ui'
#
# Created: Tue Mar  7 11:17:52 2023
#      by: qtpy-uic 2.0.5
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_wg_SaveHDA(object):
    def setupUi(self, wg_SaveHDA):
        wg_SaveHDA.setObjectName("wg_SaveHDA")
        wg_SaveHDA.resize(340, 354)
        self.verticalLayout = QtWidgets.QVBoxLayout(wg_SaveHDA)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(wg_SaveHDA)
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
        self.groupBox_2 = QtWidgets.QGroupBox(wg_SaveHDA)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.f_taskName = QtWidgets.QWidget(self.groupBox_2)
        self.f_taskName.setObjectName("f_taskName")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.f_taskName)
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.l_tasklabel = QtWidgets.QLabel(self.f_taskName)
        self.l_tasklabel.setObjectName("l_tasklabel")
        self.horizontalLayout_11.addWidget(self.l_tasklabel)
        self.l_taskName = QtWidgets.QLabel(self.f_taskName)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_taskName.sizePolicy().hasHeightForWidth())
        self.l_taskName.setSizePolicy(sizePolicy)
        self.l_taskName.setText("")
        self.l_taskName.setAlignment(QtCore.Qt.AlignCenter)
        self.l_taskName.setObjectName("l_taskName")
        self.horizontalLayout_11.addWidget(self.l_taskName)
        self.b_changeTask = QtWidgets.QPushButton(self.f_taskName)
        self.b_changeTask.setEnabled(True)
        self.b_changeTask.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_changeTask.setObjectName("b_changeTask")
        self.horizontalLayout_11.addWidget(self.b_changeTask)
        self.verticalLayout_3.addWidget(self.f_taskName)
        self.w_outPath = QtWidgets.QWidget(self.groupBox_2)
        self.w_outPath.setObjectName("w_outPath")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.w_outPath)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.l_outPath = QtWidgets.QLabel(self.w_outPath)
        self.l_outPath.setObjectName("l_outPath")
        self.horizontalLayout_12.addWidget(self.l_outPath)
        spacerItem = QtWidgets.QSpacerItem(113, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.cb_outPath = QtWidgets.QComboBox(self.w_outPath)
        self.cb_outPath.setMinimumSize(QtCore.QSize(124, 0))
        self.cb_outPath.setObjectName("cb_outPath")
        self.horizontalLayout_12.addWidget(self.cb_outPath)
        self.verticalLayout_3.addWidget(self.w_outPath)
        self.w_projectHDA = QtWidgets.QWidget(self.groupBox_2)
        self.w_projectHDA.setObjectName("w_projectHDA")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.w_projectHDA)
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.l_projectHDA = QtWidgets.QLabel(self.w_projectHDA)
        self.l_projectHDA.setObjectName("l_projectHDA")
        self.horizontalLayout_19.addWidget(self.l_projectHDA)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem1)
        self.chb_projectHDA = QtWidgets.QCheckBox(self.w_projectHDA)
        self.chb_projectHDA.setText("")
        self.chb_projectHDA.setObjectName("chb_projectHDA")
        self.horizontalLayout_19.addWidget(self.chb_projectHDA)
        self.verticalLayout_3.addWidget(self.w_projectHDA)
        self.w_externalReferences = QtWidgets.QWidget(self.groupBox_2)
        self.w_externalReferences.setObjectName("w_externalReferences")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.w_externalReferences)
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.l_externalReferences = QtWidgets.QLabel(self.w_externalReferences)
        self.l_externalReferences.setObjectName("l_externalReferences")
        self.horizontalLayout_20.addWidget(self.l_externalReferences)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem2)
        self.chb_externalReferences = QtWidgets.QCheckBox(self.w_externalReferences)
        self.chb_externalReferences.setText("")
        self.chb_externalReferences.setObjectName("chb_externalReferences")
        self.horizontalLayout_20.addWidget(self.chb_externalReferences)
        self.verticalLayout_3.addWidget(self.w_externalReferences)
        self.w_blackboxHDA = QtWidgets.QWidget(self.groupBox_2)
        self.w_blackboxHDA.setObjectName("w_blackboxHDA")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.w_blackboxHDA)
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.l_blackboxHDA = QtWidgets.QLabel(self.w_blackboxHDA)
        self.l_blackboxHDA.setObjectName("l_blackboxHDA")
        self.horizontalLayout_18.addWidget(self.l_blackboxHDA)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem3)
        self.chb_blackboxHDA = QtWidgets.QCheckBox(self.w_blackboxHDA)
        self.chb_blackboxHDA.setText("")
        self.chb_blackboxHDA.setObjectName("chb_blackboxHDA")
        self.horizontalLayout_18.addWidget(self.chb_blackboxHDA)
        self.verticalLayout_3.addWidget(self.w_blackboxHDA)
        self.f_status = QtWidgets.QWidget(self.groupBox_2)
        self.f_status.setObjectName("f_status")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.f_status)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.f_status)
        self.label.setMinimumSize(QtCore.QSize(40, 0))
        self.label.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.l_status = QtWidgets.QLabel(self.f_status)
        self.l_status.setAlignment(QtCore.Qt.AlignCenter)
        self.l_status.setObjectName("l_status")
        self.horizontalLayout_4.addWidget(self.l_status)
        self.b_goTo = QtWidgets.QPushButton(self.f_status)
        self.b_goTo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_goTo.setObjectName("b_goTo")
        self.horizontalLayout_4.addWidget(self.b_goTo)
        self.verticalLayout_3.addWidget(self.f_status)
        self.f_connect = QtWidgets.QWidget(self.groupBox_2)
        self.f_connect.setObjectName("f_connect")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.f_connect)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b_connect = QtWidgets.QPushButton(self.f_connect)
        self.b_connect.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_connect.setObjectName("b_connect")
        self.horizontalLayout_3.addWidget(self.b_connect)
        self.verticalLayout_3.addWidget(self.f_connect)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(wg_SaveHDA)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(18, -1, 18, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 271, 69))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.l_pathLast = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.l_pathLast.setObjectName("l_pathLast")
        self.horizontalLayout_5.addWidget(self.l_pathLast)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.b_pathLast = QtWidgets.QToolButton(self.groupBox)
        self.b_pathLast.setEnabled(True)
        self.b_pathLast.setArrowType(QtCore.Qt.DownArrow)
        self.b_pathLast.setObjectName("b_pathLast")
        self.horizontalLayout.addWidget(self.b_pathLast)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(wg_SaveHDA)
        QtCore.QMetaObject.connectSlotsByName(wg_SaveHDA)
        wg_SaveHDA.setTabOrder(self.e_name, self.cb_outPath)
        wg_SaveHDA.setTabOrder(self.cb_outPath, self.chb_projectHDA)
        wg_SaveHDA.setTabOrder(self.chb_projectHDA, self.chb_externalReferences)
        wg_SaveHDA.setTabOrder(self.chb_externalReferences, self.chb_blackboxHDA)
        wg_SaveHDA.setTabOrder(self.chb_blackboxHDA, self.scrollArea)
        wg_SaveHDA.setTabOrder(self.scrollArea, self.b_pathLast)

    def retranslateUi(self, wg_SaveHDA):
        wg_SaveHDA.setWindowTitle(QtWidgets.QApplication.translate("", "Export", None, -1))
        self.l_name.setText(QtWidgets.QApplication.translate("", "Name:", None, -1))
        self.l_class.setText(QtWidgets.QApplication.translate("", "Save HDA", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("", "General", None, -1))
        self.l_tasklabel.setText(QtWidgets.QApplication.translate("", "Productname:", None, -1))
        self.b_changeTask.setText(QtWidgets.QApplication.translate("", "change", None, -1))
        self.l_outPath.setText(QtWidgets.QApplication.translate("", "Outputpath:", None, -1))
        self.l_projectHDA.setText(QtWidgets.QApplication.translate("", "Save as project HDA:", None, -1))
        self.l_externalReferences.setText(QtWidgets.QApplication.translate("", "Allow external references", None, -1))
        self.l_blackboxHDA.setText(QtWidgets.QApplication.translate("", "Create Blackbox:", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("", "Status:", None, -1))
        self.l_status.setText(QtWidgets.QApplication.translate("", "Not connected", None, -1))
        self.b_goTo.setText(QtWidgets.QApplication.translate("", "Go to Node", None, -1))
        self.b_connect.setText(QtWidgets.QApplication.translate("", "Connect with selected Node", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("", "Last export", None, -1))
        self.l_pathLast.setText(QtWidgets.QApplication.translate("", "None", None, -1))
        self.b_pathLast.setText(QtWidgets.QApplication.translate("", "...", None, -1))

