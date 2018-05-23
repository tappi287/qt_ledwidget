# qt_ledwidget
**Python PyQt5 widget to display animated LEDs**

[![Latest PyPI version](https://img.shields.io/badge/pypi-v0.2-green.svg)](https://pypi.org/project/qt-ledwidget/)
[![License: MIT](https://img.shields.io/dub/l/vibe-d.svg)](https://opensource.org/licenses/MIT)

Widget that displays 3 LED's with animated on, off, blink and blink all methods.

![screenshot](/gui_res/screenshot.PNG?raw=true "Screenshot")

## Usage

Here is an usage example. For a complete example see ![/qt_ledwidget/example_app.py](https://github.com/tappi287/qt_ledwidget/blob/master/qt_ledwidget/example_app.py)

```Python
from qt_ledwidget import LedWidget

"""
LED QWidget to show progress status to users similar to networking LED's on hardware devices.
"""

# inside your PyQt5 application
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
