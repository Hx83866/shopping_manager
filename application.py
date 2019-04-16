#!/usr/bin/env python
# coding=UTF-8
'''
@Descrption: define a class for a GUI
@Author: Xiang Hu
@LastEditors: Xiang Hu
@Date: 2019-04-10 22:30:18
@LastEditTime: 2019-04-16 14:01:27
'''

import tkinter as tk
import tkinter.messagebox as msgb
from tkinter import ttk

class Application(tk.Tk):
    """继承tk中的Tk为父类"""
    
    def __init__(self):
        """初始化属性"""
        
        super().__init__()
        self.create_widgets()
        self.grid_widgets()
        
    def create_widgets(self):
        """创建框架和组件"""
        
        #主框架content
        self.mainframe = ttk.Frame(self, padding=(4,4,12,12))

        #添加组件
        self.frame = ttk.Frame(self.mainframe, borderwidth=5, relief="sunken",\
            width=400, height=300,)
        self.search_button = ttk.Button(self.mainframe)
        self.search_button["text"] = "Search"
        self.search_button["command"] = self.search
        #self.search_button.pack(side="left")
        
        self.edit_button = ttk.Button(self.mainframe)
        self.edit_button["text"] = 'Edit'
        self.edit_button["command"] = self.edit
        #self.edit_button.pack(side="right")

        self.create_button = ttk.Button(self.mainframe)
        self.create_button["text"] = "Create"
        self.create_button["command"] = self.create
        
        self.quit_button = ttk.Button(self.mainframe)
        self.quit_button["text"] = "Quit"
        self.quit_button["command"] = self.quit

        self.info_label = ttk.Label(self.mainframe)
        self.info_label["text"] = "Info_01...............................\n\
        Info_02............................................\n\
        Info_03............................................\n\
        Info_04............................................\n\
        Info_05............................................\n\
        Info_06............................................"
        
    def grid_widgets(self):
        """放置组件位置"""
        
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.frame.grid(column=0, row=0, columnspan=4, rowspan=6, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.create_button.grid(column=3, row=0, sticky=(tk.N, tk.E), padx=5)
        self.search_button.grid(column=3, row=1, sticky=(tk.N, tk.E), padx=5)
        self.edit_button.grid(column=3, row=2, sticky=(tk.N, tk.E), padx=5)
        self.quit_button.grid(column=3, row=5, sticky=(tk.S, tk.E), padx=5)
        self.info_label.grid(column=0, row=0, columnspan=3, rowspan=6, sticky=(tk.N, tk.S, tk.E, tk.W), padx=5, pady=5)

    def create(self):
        """新建数据库，用来保存新用户的数据"""

        msgb.showinfo(title='Create', message="Under Construction!\nPlease Wait!")

    def search(self):
        """提供搜索数据库的功能"""
        
        msgb.showinfo(title='Search', message="Under Construction!\nPlease Wait!")
        
    def edit(self):
        """提供修改数据库的功能"""
        
        msgb.showinfo(title='Edit', message="Under Construction!\nPlease Wait!")
    
    def quit(self):
        """退出GUI系统"""

        self.destroy()
