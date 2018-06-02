from ui.gui import *
from PyQt5 import QtWidgets, QtCore, QtGui


class ExternalUi(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.image_viewer = ImageViewer()

        # Connections
        self.ui.open_button.clicked.connect(self.open_file_in_viewer)

        # Following code is just to test if I can add new stuff on top of my existing gui.py file.
        self.ui.test_button = QtWidgets.QPushButton(self.ui.options_frame)
        self.ui.test_button.setObjectName("test_button")
        self.ui.gridLayout_3.addWidget(self.ui.test_button, 2, 0, 1, 1)

        # IMPORTANT: Let's add a grid layout to the left frame. (Where the image will be displayed)
        self.ui.grid_layout_viewer = QtWidgets.QGridLayout(self.ui.image_viewer_frame)
        # IMPORTANT: Let's add our custom image viewer widget in that new layout:
        self.ui.grid_layout_viewer.addWidget(self.image_viewer.image_label)

        # The following function must be called to display the name of the test_button.
        # See retranslate_ui() for names..
        self.retranslate_ui(self)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.ui.test_button.setText(_translate("MainWindow", "Test"))

    def open_file_in_viewer(self):
        # Careful, in PyQT5, getopenfilename returns a tuple! We must use the first element [0]
        self.fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')[0]
        print("File name is %s" % self.fname)
        self.image_viewer.open(self.fname)


class ImageViewer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.image_label = QtWidgets.QLabel()
        self.image_label.setBackgroundRole(QtGui.QPalette.Base)
        self.image_label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.image_label.setScaledContents(True)

    def open(self, filename):
        if filename:
            image = QtGui.QImage(filename)
            if image.isNull():
                QtWidgets.QMessageBox.information(self, "Image Viewer", "Cannot load %s" % filename)
                return
            self.image_label.setPixmap(QtGui.QPixmap(image))


