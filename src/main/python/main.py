from fbs_runtime.application_context.PySide6 import ApplicationContext
from fbs_runtime import PUBLIC_SETTINGS
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import sys

class _bodytypechart(QWidget):

    def __init__(self):

        super().__init__()

        self.setSizePolicy(
            QSizePolicy.MinimumExpanding,
            QSizePolicy.MinimumExpanding
        )

    def sizeHint(self):
        return QSize(40,120)

    def paintEvent(self, e):
        painter = QPainter(self)

        brush = QBrush()
        brush.setColor(QColor('black'))
        brush.setStyle(Qt.SolidPattern)
        rect = QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

class BodyTypeWidget(QWidget):

    def __init__(self):
        super().__init__()

        grid = QGridLayout()
        self._endo = QSlider(Qt.Horizontal)
        self._ecto = QSlider(Qt.Horizontal)
        self._meso = QSlider(Qt.Horizontal)

        self._endolabel = QSpinBox()
        self._endolabel.setMinimum(0)
        self._endolabel.setMaximum(100)
        self._endolabel.setValue(33.3)
        
        self._ectolabel = QSpinBox()
        self._ectolabel.setMinimum(0)
        self._ectolabel.setMaximum(100)
        self._ectolabel.setValue(33.3)
        
        self._mesolabel = QSpinBox()
        self._mesolabel.setMinimum(0)
        self._mesolabel.setMaximum(100)
        self._mesolabel.setValue(33.3)

        self._chart = _bodytypechart()

        grid.addWidget(self._chart,0,0)
        grid.addWidget(self._endo,1,0)
        grid.addWidget(self._endolabel,1,1)

        grid.addWidget(self._ecto,2,0)
        grid.addWidget(self._ectolabel,2,1)

        grid.addWidget(self._meso,3,0)
        grid.addWidget(self._mesolabel,3,1)
        
        self.setLayout(grid)

    
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        self.setWindowTitle("Creature Creator")
        bt = BodyTypeWidget()
        self.setCentralWidget(bt)


    def about_dialog(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("About")
    
        msg = "<center>"\
            "Creature Creator"\
            "&#8291;" \
            "<img src=icon.svg>" \
            "</center>" \
            f"<p>Version {PUBLIC_SETTINGS['version']}<br/>" \
            "Copyright &copy; Delta Studio</p>"\
            "<p>Program by <a href=\"https://twitter.com/nalisarc\"> Delta</a><br/>"\
            "Concept by <a href=\"https://twitter.com/Mecknavorz\">T&R</a></p>"
    
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
