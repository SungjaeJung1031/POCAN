from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import * 

class Ui_LeftMenu(object):
    def __init__(self, bgApp, font):
        self.leftMenuBg = QFrame(bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(32, 0))
        self.leftMenuBg.setMaximumSize(QSize(32, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)

        self.v_layout_main_bg = QVBoxLayout(self.leftMenuBg)
        self.v_layout_main_bg.setSpacing(0)
        self.v_layout_main_bg.setObjectName(u"v_layout_left_menu_main_bg")
        self.v_layout_main_bg.setContentsMargins(0, 0, 0, 0)

        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 32))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 32))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)

        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(0, 0, 32, 32))
        self.topLogo.setMinimumSize(QSize(32, 32))
        self.topLogo.setMaximumSize(QSize(32, 32))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(40, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.v_layout_main_bg.addWidget(self.topLogoInfo)


        # left menu
        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)

        # most outside vertical box layout for left menu
        self.v_layout_main = QVBoxLayout(self.leftMenuFrame)
        self.v_layout_main.setSpacing(0)
        self.v_layout_main.setObjectName(u"vLayoutLeftmenuMain")
        self.v_layout_main.setContentsMargins(0, 0, 0, 0)

        ### >>> toggle
        # toggle frame 
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 32))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)

        # vertical layout (toggle)
        self.v_layout_toggle = QVBoxLayout(self.toggleBox)
        self.v_layout_toggle.setSpacing(0)
        self.v_layout_toggle.setObjectName(u"vLayoutLeftmenuToggle")
        self.v_layout_toggle.setContentsMargins(0, 0, 0, 0)

        # menu button (burger menu)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 32))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(resource/icons/menu-16.png);")

        self.v_layout_toggle.addWidget(self.toggleButton)
        ### <<< toggle

        self.v_layout_main.addWidget(self.toggleBox)

        ### >>> left menu (top)
        # left menu (top) frame
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)

        # vertical layout (left menu (top))
        self.v_layout_top = QVBoxLayout(self.topMenu)
        self.v_layout_top.setSpacing(0)
        self.v_layout_top.setObjectName(u"vLayoutLeftmenuTop")
        self.v_layout_top.setContentsMargins(0, 0, 0, 0)

        # button 1
        self.btn_simulation = QPushButton(self.topMenu)
        self.btn_simulation.setObjectName(u"btn_simulation")
        sizePolicy.setHeightForWidth(self.btn_simulation.sizePolicy().hasHeightForWidth())
        self.btn_simulation.setSizePolicy(sizePolicy)
        self.btn_simulation.setMinimumSize(QSize(0, 32))
        self.btn_simulation.setFont(font)
        self.btn_simulation.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_simulation.setLayoutDirection(Qt.LeftToRight)
        self.btn_simulation.setStyleSheet(u"background-image: url(resource/icons/vehicle-16.png);")

        self.v_layout_top.addWidget(self.btn_simulation)

        # button 2
        self.btn_label = QPushButton(self.topMenu)
        self.btn_label.setObjectName(u"btn_label")
        sizePolicy.setHeightForWidth(self.btn_label.sizePolicy().hasHeightForWidth())
        self.btn_label.setSizePolicy(sizePolicy)
        self.btn_label.setMinimumSize(QSize(0, 32))
        self.btn_label.setFont(font)
        self.btn_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_label.setLayoutDirection(Qt.LeftToRight)
        self.btn_label.setStyleSheet(u"background-image: url(resource/icons/tag-16.png);")

        self.v_layout_top.addWidget(self.btn_label)

        # button 2
        self.btn_labeled_data = QPushButton(self.topMenu)
        self.btn_labeled_data.setObjectName(u"btn_labeled_data")
        sizePolicy.setHeightForWidth(self.btn_labeled_data.sizePolicy().hasHeightForWidth())
        self.btn_labeled_data.setSizePolicy(sizePolicy)
        self.btn_labeled_data.setMinimumSize(QSize(0, 32))
        self.btn_labeled_data.setFont(font)
        self.btn_labeled_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_labeled_data.setLayoutDirection(Qt.LeftToRight)
        self.btn_labeled_data.setStyleSheet(u"background-image: url(resource/icons/edit-property-16.png);")

        self.v_layout_top.addWidget(self.btn_labeled_data)

        # button 3
        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 32))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(resource/icons/cil-file.png);")

        self.v_layout_top.addWidget(self.btn_new)

        # button 4
        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 32))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(resource/icons/cil-save.png)")

        self.v_layout_top.addWidget(self.btn_save)

        # button 5
        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 32))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(resource/icons/cil-x.png);")

        self.v_layout_top.addWidget(self.btn_exit)

        self.v_layout_main.addWidget(self.topMenu, 0, Qt.AlignTop)
        ### <<< left menu (top)

        ### >>> left menu (bottom)
        # left menu (bottom) frame
        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)

        # vertical layout (left menu (bottom))
        self.v_layout_bottom = QVBoxLayout(self.bottomMenu)
        self.v_layout_bottom.setSpacing(0)
        self.v_layout_bottom.setObjectName(u"vLayoutLeftmenuBottom")
        self.v_layout_bottom.setContentsMargins(0, 0, 0, 0)

        # button setting
        self.btn_setting = QPushButton(self.bottomMenu)
        self.btn_setting.setObjectName(u"btn_setting")
        sizePolicy.setHeightForWidth(self.btn_setting.sizePolicy().hasHeightForWidth())
        self.btn_setting.setSizePolicy(sizePolicy)
        self.btn_setting.setMinimumSize(QSize(0, 32))
        self.btn_setting.setFont(font)
        self.btn_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_setting.setLayoutDirection(Qt.LeftToRight)
        self.btn_setting.setStyleSheet(u"background-image: url(resource/icons/settings-16.png);")

        self.v_layout_bottom.addWidget(self.btn_setting)

        self.v_layout_main.addWidget(self.bottomMenu, 0, Qt.AlignBottom)
        ### <<< left menu (bottom)

        self.v_layout_main_bg.addWidget(self.leftMenuFrame)

    def retranslateUi(self):
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"POCAN", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_simulation.setText(QCoreApplication.translate("MainWindow", u"Simulation", None))
        self.btn_label.setText(QCoreApplication.translate("MainWindow", u"Data Labling", None))
        self.btn_labeled_data.setText(QCoreApplication.translate("MainWindow", u"Labled Data", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))