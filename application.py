# Copyright (c) 2019 Xiang Hu
#
# -*- coding:utf-8 -*-
# @Script: application.py
# @Author: Xiang Hu
# @Email: huxiangtony@gmail.com
# @Create At: 2019-04-24 20:02:22
# @Last Modified By: Xiang Hu
# @Last Modified At: 2019-05-07 15:59:22
# @Description: a class for an GUI application.

import tkinter as tk
from tkinter import ttk
from create_records import CreateRecords


class Application(tk.Tk):
    """继承tk中的Tk为父类"""
    
    def __init__(self):
        """初始化属性"""
        
        super().__init__()
        self.create_widgets()
        self.grid_widgets()
        self.resize_config()
        
    def create_widgets(self):
        """创建框架和组件"""
        
        #主框架content
        self.mainframe = ttk.Frame(self, padding=(2,2,3,3))

        #添加组件
        self.frame = ttk.Frame(self.mainframe, borderwidth=2,\
            width=400, height=300,)
        self.search_button = ttk.Button(self.mainframe)
        self.search_button["text"] = "Search"
        self.search_button["command"] = self.search
        
        self.edit_button = ttk.Button(self.mainframe)
        self.edit_button["text"] = 'Edit'
        self.edit_button["command"] = self.edit

        self.create_button = ttk.Button(self.mainframe)
        self.create_button["text"] = "Create"
        self.create_button["command"] = self.create
        
        self.quit_button = ttk.Button(self.mainframe)
        self.quit_button["text"] = "Quit"
        self.quit_button["command"] = self.quit

        self.info_label = tk.Listbox(self.mainframe)
        self.info_label["relief"] = "sunken"  #下沉
        #self.info_label["anchor"] = "nw"   #文字靠左上角
        self.scrollbar = ttk.Scrollbar(self.mainframe, \
            orient=tk.VERTICAL, command=self.info_label.yview)
        self.info_label['yscrollcommand'] = self.scrollbar.set

        for i in range(1, 101):
            self.info_label.insert('end', "Line %d of 100." % i)
        
    def grid_widgets(self):
        """放置组件位置"""
        
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.frame.grid(column=0, row=0, columnspan=4, rowspan=6, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.create_button.grid(column=4, row=0, sticky=(tk.N))
        self.search_button.grid(column=4, row=1, sticky=(tk.N))
        self.edit_button.grid(column=4, row=2, sticky=(tk.N))
        self.quit_button.grid(column=4, row=5, sticky=(tk.S))
        self.info_label.grid(column=1, row=0, columnspan=3, rowspan=6, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.scrollbar.grid(column=0, row=0, columnspan=1, rowspan=6, sticky=(tk.N, tk.S, tk.W))

    def resize_config(self):
        """设置resize的属性，即跟随窗口扩大的系数"""
        
        #root
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        #mainframe(content)
        self.mainframe.columnconfigure(0, weight=0)
        self.mainframe.columnconfigure(1, weight=3)
        self.mainframe.columnconfigure(2, weight=3)
        self.mainframe.columnconfigure(3, weight=3)
        self.mainframe.columnconfigure(4, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=1)
        self.mainframe.rowconfigure(3, weight=3)  #“Quit”按钮上面的空间
        self.mainframe.rowconfigure(4, weight=3)  #“Quit”按钮上面的空间
        self.mainframe.rowconfigure(5, weight=1)
    
    def create(self):
        """新建文档或数据库，用来保存新用户的数据"""

        #create window for create new records
        create_win = CreateRecords()
        create_win.mainloop()

    def search(self):
        """提供搜索数据库的功能"""
        
        #msgb.showinfo(title='Search', message="Under Construction!\nPlease Wait!")
        search_win = tk.Toplevel()
        search_win.title("Search Historical Records")
        search_win.geometry('600x300+400+400')
        
    def edit(self):
        """提供修改数据库的功能"""
        
        #msgb.showinfo(title='Edit', message="Under Construction!\nPlease Wait!")
        edit_win = tk.Toplevel()
        edit_win.title("Edit Your Records")
        edit_win.geometry('600x300+500+500')
    
    def quit(self):
        """退出GUI系统"""

        self.destroy()
