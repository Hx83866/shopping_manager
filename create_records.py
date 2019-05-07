# Copyright (c) 2019 Xiang Hu
#
# -*- coding:utf-8 -*-
# @Script: create_records.py
# @Author: Xiang Hu
# @Email: huxiangtony@gmail.com
# @Create At: 2019-04-30 13:40:42
# @Last Modified By: Xiang Hu
# @Last Modified At: 2019-05-07 16:54:27
# @Description: a Subwindow for create and edit the new records.

from tkinter import *
from tkinter import filedialog as fdl
from tkinter import ttk

import xlrd
import xlsxwriter


class CreateRecords(Tk):
    """a Subwindow class for create and edit the new records"""

    def __init__(self):
        """Initialize the attribute"""

        super().__init__()
        self.title("Create")
        self.items_order = []   # a empty list to store selected columns
        self.add_widgets()
        self.place_widgets()
        self.sub_resize_config()
    
    def add_widgets(self):
        """add Widgets into the Subwinodw"""

        #content
        self.content = ttk.Frame(self, padding=(2,2,3,3))

        #add widgets
        #frame
        self.frame = ttk.Frame(self.content, borderwidth=2, width=400, \
            height=800)
        #info_line
        info = "Create a new Excel by personalizing your own pattern."
        self.info_label = ttk.Label(self.content)
        self.info_label["text"] = info

        #Labels of Columns
        self.col_label_1 = ttk.Label(self.content)
        self.col_label_1["text"] = "No.1 Column: "
        self.col_label_2 = ttk.Label(self.content)
        self.col_label_2["text"] = "No.2 Column: "
        self.col_label_3 = ttk.Label(self.content)
        self.col_label_3["text"] = "No.3 Column: "
        self.col_label_4 = ttk.Label(self.content)
        self.col_label_4["text"] = "No.4 Column: "
        self.col_label_5 = ttk.Label(self.content)
        self.col_label_5["text"] = "No.5 Column: "
        self.col_label_6 = ttk.Label(self.content)
        self.col_label_6["text"] = "No.6 Column: "
        self.col_label_7 = ttk.Label(self.content)
        self.col_label_7["text"] = "No.7 Column: "
        self.col_label_8 = ttk.Label(self.content)
        self.col_label_8["text"] = "No.8 Column: "
        self.col_label_9 = ttk.Label(self.content)
        self.col_label_9["text"] = "No.9 Column: "

        
        #Comboboxes
        col_items = ('Serial_Number', 'Client', 'Date', 'Object', 'Unit_Price',\
            'Amount', 'Total_Units_Price', 'Transportation_Cost', 'Total_Cost')
        self.item_names_1= StringVar()
        self.combobox_1 = ttk.Combobox(self.content, textvariable=\
            self.item_names_1)
        self.combobox_1["values"] = col_items
        
        self.item_names_2= StringVar()
        self.combobox_2 = ttk.Combobox(self.content, textvariable=\
            self.item_names_2)
        self.combobox_2["values"] = col_items
        
        self.item_names_3= StringVar()
        self.combobox_3 = ttk.Combobox(self.content, textvariable=\
            self.item_names_3)
        self.combobox_3["values"] = col_items
        
        self.item_names_4= StringVar()
        self.combobox_4 = ttk.Combobox(self.content, textvariable=\
            self.item_names_4)
        self.combobox_4["values"] = col_items
        
        self.item_names_5= StringVar()
        self.combobox_5 = ttk.Combobox(self.content, textvariable=\
            self.item_names_5)
        self.combobox_5["values"] = col_items
        
        self.item_names_6= StringVar()
        self.combobox_6 = ttk.Combobox(self.content, textvariable=\
            self.item_names_6)
        self.combobox_6["values"] = col_items
        
        self.item_names_7= StringVar()
        self.combobox_7 = ttk.Combobox(self.content, textvariable=\
            self.item_names_7)
        self.combobox_7["values"] = col_items
        
        self.item_names_8= StringVar()
        self.combobox_8 = ttk.Combobox(self.content, textvariable=\
            self.item_names_8)
        self.combobox_8["values"] = col_items
        
        self.item_names_9= StringVar()
        self.combobox_9 = ttk.Combobox(self.content, textvariable=\
            self.item_names_9)
        self.combobox_9["values"] = col_items

        #Buttons
        self.preview_button = ttk.Button(self.content, text="Preview",\
            command=self.store_elections)
        self.save_button = ttk.Button(self.content, text="Save", \
            command=fdl.asksaveasfilename)
        self.quit_button = ttk.Button(self.content, text="Quit", \
            command=self.destroy)
    
    def place_widgets(self):
        """Place the widgets in subwindow"""

        self.content.grid(column=0, row=0, sticky=(N,S,E,W))
        self.frame.grid(column=0, row=0, columnspan=4, rowspan=11,\
            sticky=(N,S,E,W))
        self.info_label.grid(column=0, row=0, columnspan=4, rowspan=1,\
            sticky=(W))
            
        self.col_label_1.grid(column=0, row=1, columnspan=2, sticky=(E))
        self.col_label_2.grid(column=0, row=2, columnspan=2, sticky=(E))
        self.col_label_3.grid(column=0, row=3, columnspan=2, sticky=(E))
        self.col_label_4.grid(column=0, row=4, columnspan=2, sticky=(E))
        self.col_label_5.grid(column=0, row=5, columnspan=2, sticky=(E))
        self.col_label_6.grid(column=0, row=6, columnspan=2, sticky=(E))
        self.col_label_7.grid(column=0, row=7, columnspan=2, sticky=(E))
        self.col_label_8.grid(column=0, row=8, columnspan=2, sticky=(E))
        self.col_label_9.grid(column=0, row=9, columnspan=2, sticky=(E))

        self.combobox_1.grid(column=2, row=1, columnspan=2, sticky=(W))
        self.combobox_2.grid(column=2, row=2, columnspan=2, sticky=(W))
        self.combobox_3.grid(column=2, row=3, columnspan=2, sticky=(W))
        self.combobox_4.grid(column=2, row=4, columnspan=2, sticky=(W))
        self.combobox_5.grid(column=2, row=5, columnspan=2, sticky=(W))
        self.combobox_6.grid(column=2, row=6, columnspan=2, sticky=(W))
        self.combobox_7.grid(column=2, row=7, columnspan=2, sticky=(W))
        self.combobox_8.grid(column=2, row=8, columnspan=2, sticky=(W))
        self.combobox_9.grid(column=2, row=9, columnspan=2, sticky=(W))

        self.preview_button.grid(column=0, row=10, sticky=(S,W))
        self.save_button.grid(column=2, row=10,sticky=(S,E))
        self.quit_button.grid(column=3, row=10, sticky=(S,E))

    def sub_resize_config(self):
        """Set resizing feature of the subwindow"""
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.content.columnconfigure(0, weight=2)
        self.content.columnconfigure(1, weight=2)
        self.content.columnconfigure(2, weight=2)
        self.content.columnconfigure(3, weight=2)
        self.content.rowconfigure(0, weight=0)   #info_labels
        self.content.rowconfigure(1, weight=2)
        self.content.rowconfigure(2, weight=2)
        self.content.rowconfigure(3, weight=2)
        self.content.rowconfigure(4, weight=2)
        self.content.rowconfigure(5, weight=2)
        self.content.rowconfigure(6, weight=2)
        self.content.rowconfigure(7, weight=2)
        self.content.rowconfigure(8, weight=2)
        self.content.rowconfigure(9, weight=2)
        self.content.rowconfigure(10, weight=0)   #Buttons
    
    def store_elections(self):
        """store the Selections in subwindow"""

        self.items_order.append(self.combobox_1.get())
        self.items_order.append(self.combobox_2.get())
        self.items_order.append(self.combobox_3.get())
        self.items_order.append(self.combobox_4.get())
        self.items_order.append(self.combobox_5.get())
        self.items_order.append(self.combobox_6.get())
        self.items_order.append(self.combobox_7.get())
        self.items_order.append(self.combobox_8.get())
        self.items_order.append(self.combobox_9.get())


        i =1
        for item in self.items_order:
            if item == "":
                print("No Selection in Column No. %d has been recognised!" % i)
            else:
                print(item)
            
            i += 1

    
    #def output_excel(self):
       # """Get the pattern and output as an Excel file"""