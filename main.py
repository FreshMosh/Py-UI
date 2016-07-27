#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Kivy Understanding

This file exists only to serve me as a test object for learning and understanding kivy"""

import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()