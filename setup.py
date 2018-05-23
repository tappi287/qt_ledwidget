from setuptools import setup

setup(name='qt-ledwidget',
      version='0.1',
      packages=['qt_ledwidget'],
      install_requires=[
          'PyQt5',
      ],
      include_package_data=True,
      url='https://github.com/tappi287/qt_ledwidget', license='MIT',
      author='Stefan Tapper',
      author_email='tapper.stefan@gmail.com',
      description='PyQt5 widget with animated LEDs')
