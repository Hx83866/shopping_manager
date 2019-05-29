# Copyright (c) 2019 Xiang Hu
#
# -*- coding:utf-8 -*-
# @Script: edit_records.py
# @Author: Xiang Hu
# @Email: huxiangtony@gmail.com
# @Create At: 2019-05-24 10:32:58
# @Last Modified By: Xiang Hu
# @Last Modified At: 2019-05-28 15:11:09
# @Description: Create a toplevel class as a subwindow, with the help of which excel file can be found.

from tkinter import *
from tkinter import filedialog as fdl
from tkinter import messagebox, ttk

from xlrd import open_workbook
from xlutils import copy
from xlwt import Workbook
from edit_records_subwin import AppendRecords


class FileFindSubwin(Toplevel):
    """a Subwindow class for selecting file"""

    def __init__(self):
        """Initialize the attribute"""

        super().__init__()
        self.filepath = ""
        self.title("Edit Records")
        self.add_widgets()
        self.place_widgets()
        self.sub_resize_config()
    
    def add_widgets(self):
        """add Widgets into Subwindow"""

        #content
        self.content = ttk.Frame(self, padding=(2,2,3,3))

        #frame
        self.main_frame = ttk.Frame(self.content, borderwidth=2, width=400,\
            height=99)
            
        #label
        self.label = ttk.Label(self.content)
        self.label["text"] = "Please select your excel file."

        #filepath_Entry
        self.file_path_var = StringVar()
        self.entry_path = ttk.Entry(self.content, textvariable=\
            self.file_path_var)
        
        #Buttons
        #openfile_button
        self.openfile_button = ttk.Button(self.content, text="Input File",\
            command=self.get_path)
        #quit_button and next_button
        self.quit_button = ttk.Button(self.content, text="Quit", command=\
            self.destroy)
        #next_button
        self.next_button = ttk.Button(self.content, text="Next", command=\
            self.open_edit)
    
    def place_widgets(self):
        """Place the widgets in subwindow"""

        self.content.grid(column=0, row=0, sticky=(N,S,E,W))
        self.main_frame.grid(column=0, row=0, columnspan=4, rowspan=3,\
            sticky=(N,S,E,W))  #grid the subwindow into 4 cols and 3 rows
        
        self.label.grid(column=0, row=0, columnspan=2, rowspan=1,\
            sticky=(S,W))
        self.entry_path.grid(column=0, row=1, columnspan=3, rowspan=1,\
            sticky=(E,W))
        self.openfile_button.grid(column=3, row=1, columnspan=1,\
            rowspan=1, sticky=(E))
        self.next_button.grid(column=2, row=2, columnspan=1,\
            rowspan=1, sticky=(S,E))
        self.quit_button.grid(column=3, row=2, columnspan=1,\
            rowspan=1, sticky=(S,E))\
    
    def sub_resize_config(self):
        """Set resizing feature of the subwindow"""
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.content.columnconfigure(0, weight=0)
        self.content.columnconfigure(1, weight=2)
        self.content.columnconfigure(2, weight=0)
        self.content.columnconfigure(3, weight=0)
        self.content.rowconfigure(0, weight=0)  #label
        self.content.rowconfigure(1, weight=2)  #entry
        self.content.rowconfigure(2, weight=0)  #buttons
    
    def get_path(self):
        """
            Using Filedialog to get filepath,
            return complete filepath to StringVar
        """

        self.filepath = fdl.askopenfilename(parent=self.content)
        self.filepath = self.filepath.replace("/", "\\")
        print(self.filepath)
        print(type(self.filepath))

        self.file_path_var.set(self.filepath)
    
    def open_edit(self):
        """
            open selected excel file and
            the edit subwindow
        """
        
        edit_subwindow = AppendRecords(self.file_path_var.get())
