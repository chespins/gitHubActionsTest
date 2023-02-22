# -*- coding: utf-8 -*-
import os
from util import util

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
os.environ['KIVY_NO_CONSOLELOG'] = '1'

from kivy.config import Config
Config.set("kivy","log_dir",util.findDataFile("/log"))
Config.set("kivy","log_level","info")
Config.set("kivy","log_name","./pielog.txt")
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')
Config.set('graphics', 'multisamples', '0')


from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.text import DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.uix.screenmanager import ScreenManager
from kivy.logger import logging

from view import menu as mu
from constant.systemconstant import FONT_DIR
from constant.systemconstant import FONT_FILE_NAME


resource_add_path(util.findDataFile(FONT_DIR))
LabelBase.register(DEFAULT_FONT, FONT_FILE_NAME)

class TetoconeScoreApp(App):
    def build(self):
        logging.debug("App起動")
        self.sm = ScreenManager()
        self.sm.add_widget(
                mu.MenuScreen(
                        name='menu'
                    )
            )
        return self.sm


if __name__ == '__main__':
    TetoconeScoreApp().run()
