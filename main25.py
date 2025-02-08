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
        self.ui.listWidget.itemClicked.connect(self.select_image)
        self.ui.pushButton_7.clicked.connect(self.apply_bw)
        
    def load_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Оберіть папку")
        if folder:
            self.processor.dir = folder
            images = [f for f in os.listdir(folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(images)
    def select_image(self, item):
        filename = item.text()
        self.processor.image_load(self.processor.dir, filename)
        self.display_image(os.path.join(self.processor.dir, filename))
    def display_image(self, path):
        pixmap = QPixmap(path)
        self.ui.label.setPixmap(pixmap.scaled(self.ui.label.width(), self.ui.label.height()))
    def apply_bw(self):
        self.display_image(self.processor.do_bw())
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
    def save_image(self):
        path = os.path.join(self.dir, self.save_dir)
        if not os.path.exists(path):
            os.mkdir(path)
            image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
        return image_path
    def do_bw(self):
        if self.image:
            self.image = self.image.convert('L')
            return self.save_image()
    def do_blure(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.BLUR)
            return self.save_image()
    
app = QApplication([])

ex = Widget()
ex.show()
app.exec_()