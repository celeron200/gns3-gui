# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/noplay/code/gns3/gns3-gui/gns3/ui/server_preferences_page.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServerPreferencesPageWidget(object):
    def setupUi(self, ServerPreferencesPageWidget):
        ServerPreferencesPageWidget.setObjectName("ServerPreferencesPageWidget")
        ServerPreferencesPageWidget.resize(529, 645)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ServerPreferencesPageWidget.sizePolicy().hasHeightForWidth())
        ServerPreferencesPageWidget.setSizePolicy(sizePolicy)
        ServerPreferencesPageWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ServerPreferencesPageWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiServerPreferenceTabWidget = QtWidgets.QTabWidget(ServerPreferencesPageWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiServerPreferenceTabWidget.sizePolicy().hasHeightForWidth())
        self.uiServerPreferenceTabWidget.setSizePolicy(sizePolicy)
        self.uiServerPreferenceTabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.uiServerPreferenceTabWidget.setObjectName("uiServerPreferenceTabWidget")
        self.uiLocalTabWidget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalTabWidget.sizePolicy().hasHeightForWidth())
        self.uiLocalTabWidget.setSizePolicy(sizePolicy)
        self.uiLocalTabWidget.setObjectName("uiLocalTabWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiLocalTabWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiLocalServerAutoStartCheckBox = QtWidgets.QCheckBox(self.uiLocalTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalServerAutoStartCheckBox.sizePolicy().hasHeightForWidth())
        self.uiLocalServerAutoStartCheckBox.setSizePolicy(sizePolicy)
        self.uiLocalServerAutoStartCheckBox.setMinimumSize(QtCore.QSize(0, 0))
        self.uiLocalServerAutoStartCheckBox.setChecked(False)
        self.uiLocalServerAutoStartCheckBox.setObjectName("uiLocalServerAutoStartCheckBox")
        self.verticalLayout.addWidget(self.uiLocalServerAutoStartCheckBox)
        self.uiGeneralSettingsGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiGeneralSettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.uiGeneralSettingsGroupBox.setSizePolicy(sizePolicy)
        self.uiGeneralSettingsGroupBox.setObjectName("uiGeneralSettingsGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiGeneralSettingsGroupBox)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.uiLocalServerPathLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPathLabel.setObjectName("uiLocalServerPathLabel")
        self.gridLayout.addWidget(self.uiLocalServerPathLabel, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiLocalServerPathLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPathLineEdit.setObjectName("uiLocalServerPathLineEdit")
        self.horizontalLayout.addWidget(self.uiLocalServerPathLineEdit)
        self.uiLocalServerToolButton = QtWidgets.QToolButton(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiLocalServerToolButton.setObjectName("uiLocalServerToolButton")
        self.horizontalLayout.addWidget(self.uiLocalServerToolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.uiUbridgePathLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiUbridgePathLabel.setObjectName("uiUbridgePathLabel")
        self.gridLayout.addWidget(self.uiUbridgePathLabel, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uiUbridgePathLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsGroupBox)
        self.uiUbridgePathLineEdit.setObjectName("uiUbridgePathLineEdit")
        self.horizontalLayout_5.addWidget(self.uiUbridgePathLineEdit)
        self.uiUbridgeToolButton = QtWidgets.QToolButton(self.uiGeneralSettingsGroupBox)
        self.uiUbridgeToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiUbridgeToolButton.setObjectName("uiUbridgeToolButton")
        self.horizontalLayout_5.addWidget(self.uiUbridgeToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.uiLocalServerHostLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerHostLabel.setObjectName("uiLocalServerHostLabel")
        self.gridLayout.addWidget(self.uiLocalServerHostLabel, 5, 0, 1, 1)
        self.uiLocalServerHostComboBox = QtWidgets.QComboBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerHostComboBox.setObjectName("uiLocalServerHostComboBox")
        self.gridLayout.addWidget(self.uiLocalServerHostComboBox, 6, 0, 1, 1)
        self.uiLocalServerPortLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPortLabel.setObjectName("uiLocalServerPortLabel")
        self.gridLayout.addWidget(self.uiLocalServerPortLabel, 7, 0, 1, 1)
        self.uiLocalServerPortSpinBox = QtWidgets.QSpinBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPortSpinBox.setSuffix(" TCP")
        self.uiLocalServerPortSpinBox.setMaximum(65535)
        self.uiLocalServerPortSpinBox.setProperty("value", 3080)
        self.uiLocalServerPortSpinBox.setObjectName("uiLocalServerPortSpinBox")
        self.gridLayout.addWidget(self.uiLocalServerPortSpinBox, 8, 0, 1, 1)
        self.uiConsoleConnectionsToAnyIPCheckBox = QtWidgets.QCheckBox(self.uiGeneralSettingsGroupBox)
        self.uiConsoleConnectionsToAnyIPCheckBox.setObjectName("uiConsoleConnectionsToAnyIPCheckBox")
        self.gridLayout.addWidget(self.uiConsoleConnectionsToAnyIPCheckBox, 10, 0, 1, 1)
        self.uiLocalServerAuthCheckBox = QtWidgets.QCheckBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerAuthCheckBox.setObjectName("uiLocalServerAuthCheckBox")
        self.gridLayout.addWidget(self.uiLocalServerAuthCheckBox, 9, 0, 1, 1)
        self.verticalLayout.addWidget(self.uiGeneralSettingsGroupBox)
        self.uiConsolePortRangeGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiConsolePortRangeGroupBox.setObjectName("uiConsolePortRangeGroupBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.uiConsolePortRangeGroupBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiConsoleStartPortSpinBox = QtWidgets.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleStartPortSpinBox.setSuffix(" TCP")
        self.uiConsoleStartPortSpinBox.setMaximum(65535)
        self.uiConsoleStartPortSpinBox.setProperty("value", 2000)
        self.uiConsoleStartPortSpinBox.setObjectName("uiConsoleStartPortSpinBox")
        self.horizontalLayout_7.addWidget(self.uiConsoleStartPortSpinBox)
        self.uiConsolePortRangeLabel = QtWidgets.QLabel(self.uiConsolePortRangeGroupBox)
        self.uiConsolePortRangeLabel.setObjectName("uiConsolePortRangeLabel")
        self.horizontalLayout_7.addWidget(self.uiConsolePortRangeLabel)
        self.uiConsoleEndPortSpinBox = QtWidgets.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleEndPortSpinBox.setSuffix(" TCP")
        self.uiConsoleEndPortSpinBox.setMaximum(65535)
        self.uiConsoleEndPortSpinBox.setProperty("value", 5000)
        self.uiConsoleEndPortSpinBox.setObjectName("uiConsoleEndPortSpinBox")
        self.horizontalLayout_7.addWidget(self.uiConsoleEndPortSpinBox)
        self.verticalLayout.addWidget(self.uiConsolePortRangeGroupBox)
        self.uiUDPPortRangeGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiUDPPortRangeGroupBox.setObjectName("uiUDPPortRangeGroupBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.uiUDPPortRangeGroupBox)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.uiUDPStartPortSpinBox = QtWidgets.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPStartPortSpinBox.setSuffix(" UDP")
        self.uiUDPStartPortSpinBox.setMaximum(65535)
        self.uiUDPStartPortSpinBox.setProperty("value", 10000)
        self.uiUDPStartPortSpinBox.setObjectName("uiUDPStartPortSpinBox")
        self.horizontalLayout_8.addWidget(self.uiUDPStartPortSpinBox)
        self.uiUDPPortRangeLabel = QtWidgets.QLabel(self.uiUDPPortRangeGroupBox)
        self.uiUDPPortRangeLabel.setObjectName("uiUDPPortRangeLabel")
        self.horizontalLayout_8.addWidget(self.uiUDPPortRangeLabel)
        self.uiUDPEndPortSpinBox = QtWidgets.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPEndPortSpinBox.setSuffix(" UDP")
        self.uiUDPEndPortSpinBox.setMaximum(65535)
        self.uiUDPEndPortSpinBox.setProperty("value", 20000)
        self.uiUDPEndPortSpinBox.setObjectName("uiUDPEndPortSpinBox")
        self.horizontalLayout_8.addWidget(self.uiUDPEndPortSpinBox)
        self.verticalLayout.addWidget(self.uiUDPPortRangeGroupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.uiGeneralSettingsGroupBox.raise_()
        self.uiConsolePortRangeGroupBox.raise_()
        self.uiUDPPortRangeGroupBox.raise_()
        self.uiLocalServerAutoStartCheckBox.raise_()
        self.uiServerPreferenceTabWidget.addTab(self.uiLocalTabWidget, "")
        self.uiGNS3VMTabWidget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiGNS3VMTabWidget.sizePolicy().hasHeightForWidth())
        self.uiGNS3VMTabWidget.setSizePolicy(sizePolicy)
        self.uiGNS3VMTabWidget.setObjectName("uiGNS3VMTabWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uiGNS3VMTabWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiEnableVMCheckBox = QtWidgets.QCheckBox(self.uiGNS3VMTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiEnableVMCheckBox.sizePolicy().hasHeightForWidth())
        self.uiEnableVMCheckBox.setSizePolicy(sizePolicy)
        self.uiEnableVMCheckBox.setMinimumSize(QtCore.QSize(0, 0))
        self.uiEnableVMCheckBox.setChecked(False)
        self.uiEnableVMCheckBox.setObjectName("uiEnableVMCheckBox")
        self.verticalLayout_3.addWidget(self.uiEnableVMCheckBox)
        self.uiGNS3VMSettingsGroupBox = QtWidgets.QGroupBox(self.uiGNS3VMTabWidget)
        self.uiGNS3VMSettingsGroupBox.setObjectName("uiGNS3VMSettingsGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiGNS3VMSettingsGroupBox)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiAdjustLocalServerIPCheckBox = QtWidgets.QCheckBox(self.uiGNS3VMSettingsGroupBox)
        self.uiAdjustLocalServerIPCheckBox.setObjectName("uiAdjustLocalServerIPCheckBox")
        self.gridLayout_2.addWidget(self.uiAdjustLocalServerIPCheckBox, 8, 0, 1, 2)
        self.uiHeadlessCheckBox = QtWidgets.QCheckBox(self.uiGNS3VMSettingsGroupBox)
        self.uiHeadlessCheckBox.setObjectName("uiHeadlessCheckBox")
        self.gridLayout_2.addWidget(self.uiHeadlessCheckBox, 6, 0, 1, 1)
        self.uiShutdownCheckBox = QtWidgets.QCheckBox(self.uiGNS3VMSettingsGroupBox)
        self.uiShutdownCheckBox.setObjectName("uiShutdownCheckBox")
        self.gridLayout_2.addWidget(self.uiShutdownCheckBox, 7, 0, 1, 1)
        self.uiVMNameLabel = QtWidgets.QLabel(self.uiGNS3VMSettingsGroupBox)
        self.uiVMNameLabel.setObjectName("uiVMNameLabel")
        self.gridLayout_2.addWidget(self.uiVMNameLabel, 4, 0, 1, 1)
        self.uiRefreshPushButton = QtWidgets.QPushButton(self.uiGNS3VMSettingsGroupBox)
        self.uiRefreshPushButton.setObjectName("uiRefreshPushButton")
        self.gridLayout_2.addWidget(self.uiRefreshPushButton, 5, 1, 1, 1)
        self.uiVMListComboBox = QtWidgets.QComboBox(self.uiGNS3VMSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVMListComboBox.sizePolicy().hasHeightForWidth())
        self.uiVMListComboBox.setSizePolicy(sizePolicy)
        self.uiVMListComboBox.setObjectName("uiVMListComboBox")
        self.gridLayout_2.addWidget(self.uiVMListComboBox, 5, 0, 1, 1)
        self.uiVirtualizationSoftwarLabel = QtWidgets.QLabel(self.uiGNS3VMSettingsGroupBox)
        self.uiVirtualizationSoftwarLabel.setObjectName("uiVirtualizationSoftwarLabel")
        self.gridLayout_2.addWidget(self.uiVirtualizationSoftwarLabel, 0, 0, 1, 1)
        self.uiVirtualBoxRadioButton = QtWidgets.QRadioButton(self.uiGNS3VMSettingsGroupBox)
        self.uiVirtualBoxRadioButton.setObjectName("uiVirtualBoxRadioButton")
        self.gridLayout_2.addWidget(self.uiVirtualBoxRadioButton, 2, 0, 1, 1)
        self.uiVmwareRadioButton = QtWidgets.QRadioButton(self.uiGNS3VMSettingsGroupBox)
        self.uiVmwareRadioButton.setChecked(True)
        self.uiVmwareRadioButton.setObjectName("uiVmwareRadioButton")
        self.gridLayout_2.addWidget(self.uiVmwareRadioButton, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.uiGNS3VMSettingsGroupBox)
        self.groupBox = QtWidgets.QGroupBox(self.uiGNS3VMTabWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uiVMUserLabel = QtWidgets.QLabel(self.groupBox)
        self.uiVMUserLabel.setObjectName("uiVMUserLabel")
        self.gridLayout_3.addWidget(self.uiVMUserLabel, 0, 0, 1, 1)
        self.uiVMUserLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.uiVMUserLineEdit.setObjectName("uiVMUserLineEdit")
        self.gridLayout_3.addWidget(self.uiVMUserLineEdit, 0, 1, 1, 1)
        self.uiVMPasswordLabel = QtWidgets.QLabel(self.groupBox)
        self.uiVMPasswordLabel.setObjectName("uiVMPasswordLabel")
        self.gridLayout_3.addWidget(self.uiVMPasswordLabel, 1, 0, 1, 1)
        self.uiVMPasswordLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.uiVMPasswordLineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.uiVMPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uiVMPasswordLineEdit.setObjectName("uiVMPasswordLineEdit")
        self.gridLayout_3.addWidget(self.uiVMPasswordLineEdit, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.uiServerPreferenceTabWidget.addTab(self.uiGNS3VMTabWidget, "")
        self.uiRemoteTabWidget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteTabWidget.sizePolicy().hasHeightForWidth())
        self.uiRemoteTabWidget.setSizePolicy(sizePolicy)
        self.uiRemoteTabWidget.setObjectName("uiRemoteTabWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.uiRemoteTabWidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.uiRemoteServerHostLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerHostLabel.setObjectName("uiRemoteServerHostLabel")
        self.gridLayout_5.addWidget(self.uiRemoteServerHostLabel, 2, 0, 1, 1)
        self.uiRemoteServersTreeWidget = QtWidgets.QTreeWidget(self.uiRemoteTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersTreeWidget.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersTreeWidget.setSizePolicy(sizePolicy)
        self.uiRemoteServersTreeWidget.setColumnCount(4)
        self.uiRemoteServersTreeWidget.setObjectName("uiRemoteServersTreeWidget")
        self.uiRemoteServersTreeWidget.headerItem().setText(0, "Protocol")
        self.uiRemoteServersTreeWidget.headerItem().setText(1, "Host")
        self.uiRemoteServersTreeWidget.headerItem().setText(2, "Port")
        self.gridLayout_5.addWidget(self.uiRemoteServersTreeWidget, 0, 0, 1, 2)
        self.uiRemoteServerProtocolLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerProtocolLabel.setObjectName("uiRemoteServerProtocolLabel")
        self.gridLayout_5.addWidget(self.uiRemoteServerProtocolLabel, 1, 0, 1, 1)
        self.uiRemoteServerProtocolComboBox = QtWidgets.QComboBox(self.uiRemoteTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServerProtocolComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServerProtocolComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServerProtocolComboBox.setObjectName("uiRemoteServerProtocolComboBox")
        self.uiRemoteServerProtocolComboBox.addItem("")
        self.uiRemoteServerProtocolComboBox.addItem("")
        self.gridLayout_5.addWidget(self.uiRemoteServerProtocolComboBox, 1, 1, 1, 1)
        self.uiRemoteServerPortLineEdit = QtWidgets.QLineEdit(self.uiRemoteTabWidget)
        self.uiRemoteServerPortLineEdit.setObjectName("uiRemoteServerPortLineEdit")
        self.gridLayout_5.addWidget(self.uiRemoteServerPortLineEdit, 2, 1, 1, 1)
        self.uiRemoteServerUserLineEdit = QtWidgets.QLineEdit(self.uiRemoteTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServerUserLineEdit.sizePolicy().hasHeightForWidth())
        self.uiRemoteServerUserLineEdit.setSizePolicy(sizePolicy)
        self.uiRemoteServerUserLineEdit.setObjectName("uiRemoteServerUserLineEdit")
        self.gridLayout_5.addWidget(self.uiRemoteServerUserLineEdit, 5, 1, 1, 1)
        self.uiRemoteServerPortLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerPortLabel.setObjectName("uiRemoteServerPortLabel")
        self.gridLayout_5.addWidget(self.uiRemoteServerPortLabel, 3, 0, 1, 1)
        self.uiRemoteServerUserLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerUserLabel.setObjectName("uiRemoteServerUserLabel")
        self.gridLayout_5.addWidget(self.uiRemoteServerUserLabel, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiAddRemoteServerPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiAddRemoteServerPushButton.setObjectName("uiAddRemoteServerPushButton")
        self.horizontalLayout_3.addWidget(self.uiAddRemoteServerPushButton)
        self.uiDeleteRemoteServerPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiDeleteRemoteServerPushButton.setEnabled(False)
        self.uiDeleteRemoteServerPushButton.setObjectName("uiDeleteRemoteServerPushButton")
        self.horizontalLayout_3.addWidget(self.uiDeleteRemoteServerPushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 7, 0, 1, 2)
        self.uiRemoteServerPortSpinBox = QtWidgets.QSpinBox(self.uiRemoteTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServerPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServerPortSpinBox.setSizePolicy(sizePolicy)
        self.uiRemoteServerPortSpinBox.setSuffix(" TCP")
        self.uiRemoteServerPortSpinBox.setMaximum(65535)
        self.uiRemoteServerPortSpinBox.setProperty("value", 3080)
        self.uiRemoteServerPortSpinBox.setObjectName("uiRemoteServerPortSpinBox")
        self.gridLayout_5.addWidget(self.uiRemoteServerPortSpinBox, 3, 1, 1, 1)
        self.uiRAMLimitLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRAMLimitLabel.setObjectName("uiRAMLimitLabel")
        self.gridLayout_5.addWidget(self.uiRAMLimitLabel, 4, 0, 1, 1)
        self.uiRAMLimitSpinBox = QtWidgets.QSpinBox(self.uiRemoteTabWidget)
        self.uiRAMLimitSpinBox.setMaximum(10000000)
        self.uiRAMLimitSpinBox.setSingleStep(512)
        self.uiRAMLimitSpinBox.setObjectName("uiRAMLimitSpinBox")
        self.gridLayout_5.addWidget(self.uiRAMLimitSpinBox, 4, 1, 1, 1)
        self.uiRemoteServerPasswordLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerPasswordLabel.setObjectName("uiRemoteServerPasswordLabel")
        self.gridLayout_5.addWidget(self.uiRemoteServerPasswordLabel, 6, 0, 1, 1)
        self.uiRemoteServerPasswordLineEdit = QtWidgets.QLineEdit(self.uiRemoteTabWidget)
        self.uiRemoteServerPasswordLineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.uiRemoteServerPasswordLineEdit.setText("")
        self.uiRemoteServerPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uiRemoteServerPasswordLineEdit.setObjectName("uiRemoteServerPasswordLineEdit")
        self.gridLayout_5.addWidget(self.uiRemoteServerPasswordLineEdit, 6, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem3, 8, 0, 1, 1)
        self.uiRemoteServerProtocolComboBox.raise_()
        self.uiRemoteServerHostLabel.raise_()
        self.uiRemoteServerPortLineEdit.raise_()
        self.uiRemoteServerPortLabel.raise_()
        self.uiRemoteServerPortSpinBox.raise_()
        self.uiRAMLimitLabel.raise_()
        self.uiRAMLimitSpinBox.raise_()
        self.uiRemoteServerUserLabel.raise_()
        self.uiRemoteServerUserLineEdit.raise_()
        self.uiRemoteServersTreeWidget.raise_()
        self.uiRemoteServerProtocolLabel.raise_()
        self.uiRemoteServerPasswordLineEdit.raise_()
        self.uiRemoteServerPasswordLabel.raise_()
        self.uiServerPreferenceTabWidget.addTab(self.uiRemoteTabWidget, "")
        self.uiLoadBalancingTabWidget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLoadBalancingTabWidget.sizePolicy().hasHeightForWidth())
        self.uiLoadBalancingTabWidget.setSizePolicy(sizePolicy)
        self.uiLoadBalancingTabWidget.setObjectName("uiLoadBalancingTabWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.uiLoadBalancingTabWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.uiMethodGroupBox = QtWidgets.QGroupBox(self.uiLoadBalancingTabWidget)
        self.uiMethodGroupBox.setObjectName("uiMethodGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.uiMethodGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.uiRAMUsageRadioButton = QtWidgets.QRadioButton(self.uiMethodGroupBox)
        self.uiRAMUsageRadioButton.setChecked(True)
        self.uiRAMUsageRadioButton.setObjectName("uiRAMUsageRadioButton")
        self.gridLayout_4.addWidget(self.uiRAMUsageRadioButton, 0, 0, 1, 1)
        self.uiRoundRobinRadioButton = QtWidgets.QRadioButton(self.uiMethodGroupBox)
        self.uiRoundRobinRadioButton.setObjectName("uiRoundRobinRadioButton")
        self.gridLayout_4.addWidget(self.uiRoundRobinRadioButton, 1, 0, 1, 1)
        self.uiRendezVousHashingRadioButton = QtWidgets.QRadioButton(self.uiMethodGroupBox)
        self.uiRendezVousHashingRadioButton.setEnabled(False)
        self.uiRendezVousHashingRadioButton.setObjectName("uiRendezVousHashingRadioButton")
        self.gridLayout_4.addWidget(self.uiRendezVousHashingRadioButton, 2, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.uiMethodGroupBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.uiServerPreferenceTabWidget.addTab(self.uiLoadBalancingTabWidget, "")
        self.verticalLayout_2.addWidget(self.uiServerPreferenceTabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.uiRestoreDefaultsPushButton = QtWidgets.QPushButton(ServerPreferencesPageWidget)
        self.uiRestoreDefaultsPushButton.setObjectName("uiRestoreDefaultsPushButton")
        self.horizontalLayout_2.addWidget(self.uiRestoreDefaultsPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ServerPreferencesPageWidget)
        self.uiServerPreferenceTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ServerPreferencesPageWidget)
        ServerPreferencesPageWidget.setTabOrder(self.uiServerPreferenceTabWidget, self.uiLocalServerAutoStartCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerAutoStartCheckBox, self.uiLocalServerPathLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerPathLineEdit, self.uiLocalServerToolButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerToolButton, self.uiUbridgePathLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiUbridgePathLineEdit, self.uiUbridgeToolButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiUbridgeToolButton, self.uiLocalServerHostComboBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerHostComboBox, self.uiLocalServerPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerPortSpinBox, self.uiLocalServerAuthCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerAuthCheckBox, self.uiConsoleConnectionsToAnyIPCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleConnectionsToAnyIPCheckBox, self.uiConsoleStartPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleStartPortSpinBox, self.uiConsoleEndPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleEndPortSpinBox, self.uiUDPStartPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiUDPStartPortSpinBox, self.uiUDPEndPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiUDPEndPortSpinBox, self.uiRestoreDefaultsPushButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiRestoreDefaultsPushButton, self.uiEnableVMCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiEnableVMCheckBox, self.uiVMListComboBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiVMListComboBox, self.uiRefreshPushButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiRefreshPushButton, self.uiHeadlessCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiHeadlessCheckBox, self.uiShutdownCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiShutdownCheckBox, self.uiVMUserLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiVMUserLineEdit, self.uiVMPasswordLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiVMPasswordLineEdit, self.uiRemoteServersTreeWidget)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServersTreeWidget, self.uiRemoteServerProtocolComboBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerProtocolComboBox, self.uiRemoteServerPortLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerPortLineEdit, self.uiRemoteServerPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerPortSpinBox, self.uiRemoteServerUserLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerUserLineEdit, self.uiRemoteServerPasswordLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerPasswordLineEdit, self.uiAddRemoteServerPushButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiAddRemoteServerPushButton, self.uiDeleteRemoteServerPushButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiDeleteRemoteServerPushButton, self.uiRAMLimitSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiRAMLimitSpinBox, self.uiRAMUsageRadioButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiRAMUsageRadioButton, self.uiRoundRobinRadioButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiRoundRobinRadioButton, self.uiRendezVousHashingRadioButton)

    def retranslateUi(self, ServerPreferencesPageWidget):
        _translate = QtCore.QCoreApplication.translate
        ServerPreferencesPageWidget.setWindowTitle(_translate("ServerPreferencesPageWidget", "Server"))
        self.uiLocalServerAutoStartCheckBox.setText(_translate("ServerPreferencesPageWidget", "Enable local server"))
        self.uiGeneralSettingsGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "General settings"))
        self.uiLocalServerPathLabel.setText(_translate("ServerPreferencesPageWidget", "Server path:"))
        self.uiLocalServerToolButton.setText(_translate("ServerPreferencesPageWidget", "&Browse..."))
        self.uiUbridgePathLabel.setText(_translate("ServerPreferencesPageWidget", "Ubridge path:"))
        self.uiUbridgeToolButton.setText(_translate("ServerPreferencesPageWidget", "&Browse..."))
        self.uiLocalServerHostLabel.setText(_translate("ServerPreferencesPageWidget", "Host binding:"))
        self.uiLocalServerPortLabel.setText(_translate("ServerPreferencesPageWidget", "Port:"))
        self.uiConsoleConnectionsToAnyIPCheckBox.setText(_translate("ServerPreferencesPageWidget", "Allow console connections to any local IP address"))
        self.uiLocalServerAuthCheckBox.setText(_translate("ServerPreferencesPageWidget", "Protect server with password (recommended)"))
        self.uiConsolePortRangeGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "Console port range (5900 => 6000 is shared with VNC)"))
        self.uiConsolePortRangeLabel.setText(_translate("ServerPreferencesPageWidget", "to"))
        self.uiUDPPortRangeGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "UDP tunneling port range"))
        self.uiUDPPortRangeLabel.setText(_translate("ServerPreferencesPageWidget", "to"))
        self.uiServerPreferenceTabWidget.setTabText(self.uiServerPreferenceTabWidget.indexOf(self.uiLocalTabWidget), _translate("ServerPreferencesPageWidget", "Local server"))
        self.uiEnableVMCheckBox.setText(_translate("ServerPreferencesPageWidget", "Enable the local GNS3 VM"))
        self.uiGNS3VMSettingsGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "Settings"))
        self.uiAdjustLocalServerIPCheckBox.setText(_translate("ServerPreferencesPageWidget", "Adjust the local server IP to be in the same subnet"))
        self.uiHeadlessCheckBox.setText(_translate("ServerPreferencesPageWidget", "Start VM in headless mode"))
        self.uiShutdownCheckBox.setText(_translate("ServerPreferencesPageWidget", "ACPI shutdown VM when closing GNS3"))
        self.uiVMNameLabel.setText(_translate("ServerPreferencesPageWidget", "VM name:"))
        self.uiRefreshPushButton.setText(_translate("ServerPreferencesPageWidget", "&Refresh"))
        self.uiVirtualizationSoftwarLabel.setText(_translate("ServerPreferencesPageWidget", "Virtualization software:"))
        self.uiVirtualBoxRadioButton.setText(_translate("ServerPreferencesPageWidget", "VirtualBox"))
        self.uiVmwareRadioButton.setText(_translate("ServerPreferencesPageWidget", "VMware (recommended)"))
        self.groupBox.setTitle(_translate("ServerPreferencesPageWidget", "Authentication (optional)"))
        self.uiVMUserLabel.setText(_translate("ServerPreferencesPageWidget", "User:"))
        self.uiVMPasswordLabel.setText(_translate("ServerPreferencesPageWidget", "Password:"))
        self.uiServerPreferenceTabWidget.setTabText(self.uiServerPreferenceTabWidget.indexOf(self.uiGNS3VMTabWidget), _translate("ServerPreferencesPageWidget", "Local GNS3 VM"))
        self.uiRemoteServerHostLabel.setText(_translate("ServerPreferencesPageWidget", "Host:"))
        self.uiRemoteServersTreeWidget.headerItem().setText(3, _translate("ServerPreferencesPageWidget", "User"))
        self.uiRemoteServerProtocolLabel.setText(_translate("ServerPreferencesPageWidget", "Protocol:"))
        self.uiRemoteServerProtocolComboBox.setCurrentText(_translate("ServerPreferencesPageWidget", "HTTP"))
        self.uiRemoteServerProtocolComboBox.setItemText(0, _translate("ServerPreferencesPageWidget", "HTTP"))
        self.uiRemoteServerProtocolComboBox.setItemText(1, _translate("ServerPreferencesPageWidget", "HTTPS"))
        self.uiRemoteServerPortLineEdit.setText(_translate("ServerPreferencesPageWidget", "192.168.56.101"))
        self.uiRemoteServerPortLabel.setText(_translate("ServerPreferencesPageWidget", "Port:"))
        self.uiRemoteServerUserLabel.setText(_translate("ServerPreferencesPageWidget", "User:"))
        self.uiAddRemoteServerPushButton.setText(_translate("ServerPreferencesPageWidget", "&Add"))
        self.uiDeleteRemoteServerPushButton.setText(_translate("ServerPreferencesPageWidget", "&Delete"))
        self.uiRAMLimitLabel.setText(_translate("ServerPreferencesPageWidget", "RAM limit:"))
        self.uiRAMLimitSpinBox.setSuffix(_translate("ServerPreferencesPageWidget", " MB"))
        self.uiRemoteServerPasswordLabel.setText(_translate("ServerPreferencesPageWidget", "Password:"))
        self.uiServerPreferenceTabWidget.setTabText(self.uiServerPreferenceTabWidget.indexOf(self.uiRemoteTabWidget), _translate("ServerPreferencesPageWidget", "Remote servers"))
        self.uiMethodGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "Method"))
        self.uiRAMUsageRadioButton.setText(_translate("ServerPreferencesPageWidget", "RAM usage"))
        self.uiRoundRobinRadioButton.setText(_translate("ServerPreferencesPageWidget", "Round-Robin"))
        self.uiRendezVousHashingRadioButton.setText(_translate("ServerPreferencesPageWidget", "Rendezvous hashing"))
        self.uiServerPreferenceTabWidget.setTabText(self.uiServerPreferenceTabWidget.indexOf(self.uiLoadBalancingTabWidget), _translate("ServerPreferencesPageWidget", "Load Balancing"))
        self.uiRestoreDefaultsPushButton.setText(_translate("ServerPreferencesPageWidget", "Restore defaults"))

