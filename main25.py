from PIL import Image
from PIL.ImageFilter import SHARPEN
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow


class Widget(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.processor = ImageProcessor()
        self.ui.pushButton.clicked.connect(self.load_folder)
    def load_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Оберіть папку")
        if folder:
            self.processor.dir = folder
            images = [f for f in os.listdir(folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(images)
class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Оброблені зображення"
    def image_load(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()