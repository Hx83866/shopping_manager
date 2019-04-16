#!/usr/bin/env python
# coding=UTF-8
'''
@Descrption: It is a GUI for managment of data, which are generated during the purchasing oversea.
@Author: Xiang Hu
@LastEditors: Xiang Hu
@Date: 2019-04-10 22:32:43
@LastEditTime: 2019-04-16 13:46:38
'''

from application import Application
from tkinter import *

#generate a object
shopping_manager = Application()
shopping_manager.title("Shopping Manager")
shopping_manager.mainloop()