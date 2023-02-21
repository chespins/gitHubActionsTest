# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from util import util

Builder.load_file(util.findDataFile('./kvfile/menu.kv'))


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

    def on_pre_enter(self, **kwargs):
        pass


if __name__ == '__main__':
    pass
