# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_res/LED_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import qt_ledwidget.led_widget
from PyQt5 import QtCore, QtGui, QtWidgets


class Timer(QtCore.QObject):
    timer_one = QtCore.QTimer()
    timer_one.setInterval(800)

    timer_two = QtCore.QTimer()
    timer_two.setInterval(1600)


class Ui_LedPanel(object):
    def setupUi(self, LedPanel):
        LedPanel.setObjectName("LedPanel")
        LedPanel.resize(380, 109)
        self.gridLayout = QtWidgets.QGridLayout(LedPanel)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.led_ovr = qt_ledwidget.led_widget.LedWidget(LedPanel, self.gridLayout)

        # Let em blink
        self.timer = Timer().timer_one
        self.timer.timeout.connect(self.led_ovr.led_blink_all)
        self.timer.start()

        self.fancy_timer = Timer().timer_two
        self.fancy_timer.timeout.connect(self.fancy_blink)
        self.fancy_timer.start()

        self.retranslateUi(LedPanel)
        QtCore.QMetaObject.connectSlotsByName(LedPanel)

    def fancy_blink(self):
        self.led_ovr.led_blink(0, 3, 10)
        self.led_ovr.led_blink(1, 3, 60)
        self.led_ovr.led_blink(2, 3, 110)

    def retranslateUi(self, LedPanel):
        _translate = QtCore.QCoreApplication.translate
        LedPanel.setWindowTitle(_translate("LedPanel", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LedPanel = QtWidgets.QWidget()
    ui = Ui_LedPanel()
    ui.setupUi(LedPanel)
    LedPanel.show()
    sys.exit(app.exec_())
