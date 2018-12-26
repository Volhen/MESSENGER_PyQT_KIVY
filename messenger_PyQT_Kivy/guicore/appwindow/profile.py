import sys

import os

from PyQt5 import QtWidgets, QtGui

from PIL import Image, ImageDraw

from PIL.ImageQt import ImageQt

from guicore.appwindow.form.ava import Ui_MainWindow_profile


class AppProfile(QtWidgets.QMainWindow, Ui_MainWindow_profile):
    
    def __init__(self):

        dirname = os.path.dirname(os.path.abspath(__import__("__main__").__file__))

        self._path = os.path.join(dirname, 'src/avatar') 

        self.count_zoom = 0

        self._image = None

        super(AppProfile,self).__init__()

        self.setupUi_profile(self)

    
    def push_button(self):

        self.btn_rsc.clicked.connect(self.show_dialog)

        self.btn_zoom_in.clicked.connect(self.zoom_in)

        self.btn_zoom_out.clicked.connect(self.zoom_out)

        self.rbtn_gray.clicked.connect(self.gray_effects)

        self.rbtn_negative.clicked.connect(self.negative_effects)

        self.rbtn_sepia.clicked.connect(self.sepia_effects)

        self.rbtn_normal.clicked.connect(self.init_image)

        self.rbtn_black_white.clicked.connect(self.black_white_effects)

        self.btn_Ok.clicked.connect(self.push_button_ok)

        self.btn_Cancel.clicked.connect(self.push_button_ok)


    def show_dialog(self):

        self.fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', self._path)[0]
        
        self.init_image()

        # *****************************************

        self.rbtn_gray.setEnabled(True)

        self.rbtn_negative.setEnabled(True)

        self.rbtn_sepia.setEnabled(True)

        self.rbtn_black_white.setEnabled(True)

        self.rbtn_normal.setEnabled(True)

        self.label_effects.setEnabled(True)

        self.label_size_zoom.setEnabled(True)
        
        self.btn_zoom_in.setEnabled(True)

        self.btn_zoom_out.setEnabled(True)


    def render_image(self):

        img_tmp = ImageQt(self._image.convert('RGBA'))

        pixmap = QtGui.QPixmap.fromImage(img_tmp)

        self.display.setPixmap(pixmap)

    
    def init_image(self):

        self._image = Image.open(self.fname)

        self.width = self._image.size[0]

        self.height = self._image.size[1]

        self.label_size_zoom.setText('Size zoom')

        self.count_zoom = 0

        self.render_image()

    
    def init_draw_image(self):

        self.draw = ImageDraw.Draw(self._image)

        self.pix = self._image.load()

    
    def push_button_ok(self):

        self.close()

    
    def gray_effects(self):

        self.init_image()

        self.init_draw_image()


        for i in range(self.width):

            for j in range(self.height):

                a = self.pix[i, j][0]

                b = self.pix[i, j][1]

                c = self.pix[i, j][2]

                S = (a + b + c) // 2

                self.draw.point((i, j), (S, S, S))

        self.render_image()


    def negative_effects(self):

        self.init_image()

        self.init_draw_image()

        for i in range(self.width):

            for j in range(self.height):

                a = self.pix[i, j][0]

                b = self.pix[i, j][1]

                c = self.pix[i, j][2]

                self.draw.point((i, j), (255 - a, 255 - b, 255 - c))

        self.render_image()


    def sepia_effects(self):

        self.init_image()

        self.init_draw_image()

        depth = 30

        for i in range(self.width):

            for j in range(self.height):

                a = self.pix[i, j][0]

                b = self.pix[i, j][1]

                c = self.pix[i, j][2]

                S = (a + b + c)

                a = S + depth * 2

                b = S + depth

                c = S

                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255

                self.draw.point((i, j), (a, b, c))

        self.render_image()


    def black_white_effects(self):

        self.init_image()

        self.init_draw_image()

        factor = 50

        for i in range(self.width):

            for j in range(self.height):

                a = self.pix[i, j][0]

                b = self.pix[i, j][1]

                c = self.pix[i, j][2]

                S = a + b + c

                if (S > (((255 + factor) // 2) * 3)):

                    a, b, c = 255, 255, 255

                else:

                    a, b, c = 0, 0, 0

                self.draw.point((i, j), (a, b, c))

        self.render_image()


    def zoom_in(self):

        self.count_zoom = self.count_zoom + 10

        if self.count_zoom > -100 and self.count_zoom <= 100:

            itm = self.count_zoom

            width = self.width

            width = width + ((width * itm)//100)

            height = self.height

            height = height + ((height * itm)//100)

            # print('max: ', width, ' ', height)

            self._image = self._image.resize((width, height), Image.BICUBIC)

            self.draw = ImageDraw.Draw(self._image)

            self.render_image()

            # *********** zoom progress ***********

            text_zoom = 'Size zoom ' + str(self.count_zoom) + '%'

            self.label_size_zoom.setText(text_zoom)

    
    def zoom_out(self):

        self.count_zoom = self.count_zoom - 10

        if self.count_zoom > -100 and self.count_zoom <= 100:

            itm = self.count_zoom

            width = self.width

            width = width + ((width * itm)//100)

            height = self.height

            height = height + ((height * itm)//100)

            # print('min: ', width, ' ', height)

            self._image = self._image.resize((width, height), Image.BICUBIC)

            self.draw = ImageDraw.Draw(self._image)

            self.render_image()

           # *********** zoom progress ***********

            text_zoom = 'Size zoom ' + str(self.count_zoom) + '%'

            self.label_size_zoom.setText(text_zoom)