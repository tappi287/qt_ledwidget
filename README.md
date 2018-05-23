# qt_ledwidget
**Python PyQt5 widget to display animated LEDs**

[![Latest PyPI version](https://img.shields.io/badge/pypi-v0.1-green.svg)](https://pypi.org/project/qt-ledwidget/)
[![License: MIT](https://img.shields.io/dub/l/vibe-d.svg)](https://opensource.org/licenses/MIT)

Widget that displays 3 LED's with animated on, off, blink and blink all methods.

![screenshot](/gui_res/screenshot.PNG?raw=true "Screenshot")

## Usage

Here is an usage example. For a complete example see ![/qt_ledwidget/example_app.py](https://github.com/tappi287/qt_ledwidget/blob/master/qt_ledwidget/example_app.py)

```Python
from qt_ledwidget import LedWidget

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

# inside your PyQt5 application
"""
    Add the LedWidget as led_widget instance
    Provide a parent QWidget and a QLayout to add the widget to
    OR provide no layout and add the widget instance to your layout yourself.

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
led_widget = LedWidget(YourParentWidget, YourLayout,
                       led_size=24,
                       show_red=False, show_yellow=True, show_green=True)


# Let em blink
led_widget.led_blink_all()
```

## Installation

### Python

From PyPI: Get the lastest stable version of ``qt-ledwidget`` package
using *pip* (preferable):

```bash
pip install qt-ledwidget
```

From code: Download/clone the project, go to ``qt_ledwidget`` folder that contains setup.py then:

- You can use the *setup* script and pip install.
    ```bash
    pip install .
    ```

- Or, you can use the *setup* script with Python:
    ```bash
    python setup.py install
    ```
