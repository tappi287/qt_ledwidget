# -*- coding: utf-8 -*-
"""
    Basic Qt Example application to demonstrate the usage of the LED widget
"""
# Form implementation generated from reading ui file 'gui_res/LED_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from qt_ledwidget import LedWidget
from PyQt5 import QtCore, QtWidgets


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

        """
            Add the LedWidget as self.led_ovr instance
            Provide a parent QWidget and a QLayout to add the widget to
            
            The widget contains 4 methods to animate the LED's
                led_on          [idx] Toggles the LED on with 100ms animation duration
                led_off         [idx] Toggles the LED off with 400ms animation duration
                led_blink       [idx, count, timer] Will blink n-times and toggle LED off
                led_blink_all   [forward] Will blink all LED with 100ms offset and toggle all off
                
                Parameter description:
                    idx     -   (int) Index of the LED to animate: 0 - Red, 1 - Yellow, 2 - Green
                    count   -   (int) Number of times the LED should blink(loop count)
                    timer   -   (int) Number of milliseconds after which the blink should start
                    forward -   (bool) Blink all LED from idx 0 to 2 or 2 to 0 with a 100ms offset
        """
        self.led_ovr = LedWidget(LedPanel, self.gridLayout)

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
