import sys
import os
from PyQt5 import QtWidgets

# Press the green button in the gutter to run the script.
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QLabel, QSystemTrayIcon, QMenu

from MainWindow import MainWindow
from rena.interfaces import InferenceInterface

from PyQt5.QtCore import Qt, QFile, QTextStream

app = None

# Define function to import external files when using PyInstaller.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    # define icon

    # load the qt application
    app = QtWidgets.QApplication(sys.argv)
    tray_icon = QSystemTrayIcon(QIcon('icon.PNG'), parent=app)
    tray_icon.setToolTip('RNApp')
    tray_icon.show()

    # splash screen
    splash = QLabel()
    pixmap = QPixmap('../media/logo/RN.png')
    # pixmap = pixmap.scaled(640, 640)
    splash.setPixmap(pixmap)
    splash.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    splash.show()

    # main window init
    inference_interface = InferenceInterface.InferenceInterface()
    window = MainWindow(app=app, inference_interface=inference_interface)

    window.setWindowIcon(QIcon('../media/logo/RN.png'))
    # make tray menu
    menu = QMenu()
    exit_action = menu.addAction('Exit')
    exit_action.triggered.connect(window.close)

    # stylesheet init

    stylesheet = QFile('ui/stylesheet/dark.qss')
    stylesheet.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(stylesheet)
    app.setStyleSheet(stream.readAll())
    # splash screen destroy
    splash.destroy()

    window.show()
    app.exec_()
    print('Resuming Console Interaction.')
