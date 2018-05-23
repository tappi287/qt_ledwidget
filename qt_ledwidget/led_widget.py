import os
from tempfile import NamedTemporaryFile as Ntf
from . import led_widget_res_rc
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.uic import loadUi


def setup_resources():
    global UI_FILE_LED, RED_IMG, GREEN_IMG, YELLOW_IMG

    # Get UI file content from qt resource
    ui_rsc = QtCore.QFile(':/ui/LED_widget.ui')
    ui_rsc.open(QtCore.QFile.ReadOnly)
    UI_FILE_LED = ui_rsc.readAll()
    ui_rsc.close()
    del ui_rsc

    RED_IMG = ':/main/LED_Red_On.png'
    YELLOW_IMG = ':/main/LED_Yellow_On.png'
    GREEN_IMG = ':/main/LED_Green_On.png'


class LedWidget(QtWidgets.QWidget):

    # noinspection PyArgumentList
    def __init__(self, parent, layout=None, alignment=QtCore.Qt.AlignLeft,
                 led_size = 32,
                 show_red=True, show_yellow=True, show_green=True):
        """
        LED QWidget to show progress status to users similar to networking LED's on hardware devices.
            LED-Index: 0-RED, 1-YELLOW, 2-GREEN


        :param parent: The parent QWidget
        :param layout: Optional: the layout to add this widget to
        :param alignment: Optional: the alignment inside the provided layout. Default is left alignment.
        :param led_size: Optional: Pixel size as single integer for the LED graphics, maximum 32px
        :param show_red: Optional: show the red LED
        :param show_yellow: Optional: show the yellow LED
        :param show_green: Optional: show the green LED
        """
        super(LedWidget, self).__init__(parent=parent)
        setup_resources()

        self.parent = parent

        with Ntf(mode='wb', delete=False) as ui_temp_file:
            # Write ui file content to temporary file
            ui_temp_file.write(UI_FILE_LED)

        # loadUi only accepts a file path
        loadUi(ui_temp_file.name, self)

        try:
            os.remove(ui_temp_file.name)
        except OSError as e:
            print(e)

        # 0 - RED : 1 - YELLOW : 2 - GREEN
        self.led_default_labels = [self.ledRed, self.ledYellow, self.ledGreen]
        self.led_overlay_labels = list()

        # Load glowing overlay LED pixmaps
        for idx, img in enumerate([RED_IMG, YELLOW_IMG, GREEN_IMG]):
            default_pixmap = self.led_default_labels[idx].pixmap()
            on_pixmap = QtGui.QPixmap(img)

            # Resize pixmaps if size provided
            if led_size != 32:
                # Restrict to 32px
                led_size = min(led_size, 32)

                # Resize pixmaps
                on_pixmap = on_pixmap.scaled(
                    led_size, led_size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                default_pixmap = default_pixmap.scaled(
                    led_size, led_size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

                # Resize off labels
                self.led_default_labels[idx].setPixmap(default_pixmap)
                self.led_default_labels[idx].resize(led_size, led_size)

            led_on_label = _LedLabel(on_pixmap)
            self.led_overlay_labels.append(led_on_label)
            self.gridLayout.addWidget(led_on_label, 0, idx, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        if not show_red:
            self.led_default_labels[0].hide()
            self.led_overlay_labels[0].hide()
        if not show_yellow:
            self.led_default_labels[1].hide()
            self.led_overlay_labels[1].hide()
        if not show_green:
            self.led_default_labels[2].hide()
            self.led_overlay_labels[2].hide()

        if layout is not None:
            layout.addWidget(self, 0, alignment)

    def led_on(self, idx):
        """ Switch LED on by index 0 - RED : 1 - YELLOW : 2 - GREEN """
        if idx < len(self.led_overlay_labels):
            self.led_overlay_labels[idx].on()

    def led_off(self, idx):
        """ Switch LED off by index 0 - RED : 1 - YELLOW : 2 - GREEN """
        if idx < len(self.led_overlay_labels):
            self.led_overlay_labels[idx].off()

    def led_blink(self, idx, count=1, timer=0):
        """ Blink LED by index 0 - RED : 1 - YELLOW : 2 - GREEN """
        if idx < len(self.led_overlay_labels):
            self.led_overlay_labels[idx].blink(count, timer)

    def led_blink_all(self, forward=True):
        rng, start_time = range(2, -1, -1), 50
        if forward:
            rng = range(0, 3, 1)

        for idx in rng:
            start_time += 100
            self.led_overlay_labels[idx].blink(1, start_time)


class _LedLabel(QtWidgets.QLabel):
    def __init__(self, pixmap):
        super(_LedLabel, self).__init__()
        self.pixmap = pixmap
        self.setPixmap(self.pixmap)
        self.setGeometry(0, 0, self.pixmap.size().width(), self.pixmap.size().height())
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # Property value
        self._opacity = 0.0

        # Setup on animation
        self.on_anim = QtCore.QPropertyAnimation(self, b'opacity')
        self._setup_anim(self.on_anim, 0.0, 1.0, 100)

        # Setup off animation
        self.off_anim = QtCore.QPropertyAnimation(self, b'opacity')
        self._setup_anim(self.off_anim, 1.0, 0.0, 400)

        # Setup blink animation
        self.blink_anim = QtCore.QPropertyAnimation(self, b'opacity')
        self._setup_blink()

        # Setup blink timer
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self._blink_timer)

    def blink(self, count=1, time_later=0):
        if not time_later:
            if self.on_anim.state() == QtCore.QAbstractAnimation.Running:
                return
            if self.off_anim.state() == QtCore.QAbstractAnimation.Running:
                return

        self._setup_blink(count)

        if not time_later:
            # Blink immediately
            self.blink_anim.start()
        else:
            # Blink later
            self.timer.start(time_later)

    def on(self):
        self.on_anim.setLoopCount(1)
        self.on_anim.start()

    def off(self):
        self.off_anim.start()

    def _blink_timer(self):
        """ Timer target, blink animation already set-up """
        self.blink_anim.start()

    def _setup_blink(self, count=1):
        self.blink_anim.setEasingCurve(QtCore.QEasingCurve.OutInQuint)

        self.blink_anim.setStartValue(0.0)
        self.blink_anim.setKeyValueAt(0.5, 1.0)
        self.blink_anim.setEndValue(0.0)

        self.blink_anim.setDuration(200)
        self.blink_anim.setLoopCount(count)

    @staticmethod
    def _setup_anim(animation, start_value, end_value, duration):
        animation.setEasingCurve(QtCore.QEasingCurve.OutCubic)
        animation.setStartValue(start_value)
        animation.setEndValue(end_value)
        animation.setDuration(duration)

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setOpacity(self.opacity)
        painter.drawPixmap(0, 0, self.pixmap)
        painter.end()

    @QtCore.pyqtProperty(float)
    def opacity(self):
        return self._opacity

    @opacity.setter
    def opacity(self, value):
        self._opacity = value

        # Force re-paint on value change
        self.repaint()
