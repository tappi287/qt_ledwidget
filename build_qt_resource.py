"""
    Creates python resource module for PyQt5 with pyrcc5
    Creates example_app.py to test the widget
"""

from shlex import split as shell_syntax
from subprocess import Popen
from sys import exit

args = "pyrcc5 -compress 9 -o qt_ledwidget/led_widget_res_rc.py gui_res/led_widget_res.qrc"
pyuic_args = "pyuic5 --from-imports -x -o qt_ledwidget/example_app.py gui_res/LED_widget.ui"

print('Creating resource file led_widget_res_rc.py')
print('Starting: ', str(args))
process = Popen(shell_syntax(args))
process.wait()

"""
print('Creating example qt-app example_app.py')
print('Starting: ', str(pyuic_args))
pyuic_process = Popen(shell_syntax(pyuic_args))
pyuic_process.wait()
"""

exit()

