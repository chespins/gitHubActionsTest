# -*- coding: utf-8 -*-
import os

from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.text import DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config

from view import menu as mu
from util import util
from constant.systemconstant import FONT_DIR
from constant.systemconstant import FONT_FILE_NAME

os.environ['KIVY_GL_BACKEND'] = 'sdl2'
os.environ['KIVY_NO_CONSOLELOG'] = '1'

Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

resource_add_path(util.findDataFile(FONT_DIR))
LabelBase.register(DEFAULT_FONT, FONT_FILE_NAME)

class TetoconeScoreApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(
                mu.MenuScreen(
                        name='menu'
                    )
            )
        return self.sm


if __name__ == '__main__':
    TetoconeScoreApp().run()
