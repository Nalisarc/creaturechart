from fbs_runtime.application_context.PySide6 import ApplicationContext
from PySide6.QtWidgets import *

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.about_dialog)
        self.setCentralWidget(button)

    def about_dialog(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("About")
    
        msg = "<center>"\
            "Creature Creator"\
            "&#8291;" \
            "<img src=icon.svg>" \
            "</center>" \
            "<p>Version 31.4.159.265358<br/>" \
            "Copyright &copy; Company Inc.</p>"
    
        dlg.setText(msg)
        button = dlg.exec_()
    
        if button == QMessageBox.Ok:
            print("OK!")


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.resize(250, 150)
    window.show()
    exit_code = appctxt.app.exec()      # 2. Invoke appctxt.app.exec()
    sys.exit(exit_code)
