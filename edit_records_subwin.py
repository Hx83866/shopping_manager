# Copyright (c) 2019 Xiang Hu
#
# -*- coding:utf-8 -*-
# @Script: edit_records_subwin.py
# @Author: Xiang Hu
# @Email: huxiangtony@gmail.com
# @Create At: 2019-05-27 12:33:46
# @Last Modified By: Xiang Hu
# @Last Modified At: 2019-05-29 22:49:31
# @Description: Create a toplevel class as a subwindow, with which shopping records can be edit.

from tkinter import *
from tkinter import filedialog as fdl
from tkinter import messagebox, ttk

from xlrd import open_workbook, xldate_as_tuple
from xlutils.copy import copy
from xlwt import Workbook


class AppendRecords(Toplevel):
    """a Subwindow class for appending records into selected excel file"""

    def __init__(self, selected_filepath):
        """Initialize the attribute"""

        super().__init__()
        
        #self.header_list = ['Serial_Number', 'Client', 'Date', 'Object',\
           # 'Unit_Price','Amount', 'Total_Units_Price', 'Transportation_Cost',\
            #'Total_Cost']

        #information of selected file
        self.input_header = []
        self.rows_number = 0

        #input the filepath of the selected excel
        self.selected_filepath = selected_filepath
        
        #try to input the header of selected excel
        #the header items are the column label
        try:
            self.check_selected_file()
            #check whether the excel is empty or not
            if self.input_header[0]:

                #a container to store labels Widgets
                self.label_container = []
                #a container to store Entrys Widgets
                self.entrys_container = []
                #a container to store inputs
                self.input_container = []
                
                self.title("Append Records")
                self.add_widgets()
                self.place_widgets()
                self.sub_resize_config()

            else:
                messagebox.showerror(title="Empty Excel",\
                    message="Unfortunately! The Excel File is empty!")
                
        except:
            messagebox.showerror(title="Error!", message="No Valid Filepath!")
    
    def check_selected_file(self):
        """
            Check the input file whether valid or not,
            if valid, output the header of excel
        """

        with open_workbook(self.selected_filepath,\
            encoding_override="utf-8") as selected_workbook:
            sheets = selected_workbook.sheet_names()
            print(sheets)
            worksheet = selected_workbook.sheet_by_name(sheets[0])
            rows_number = worksheet.nrows
            self.rows_number = rows_number
            print("Sheet number in this workbook: {0}.".format(rows_number))

            #output header of selected file
            self.input_header = worksheet.row_values(0)
            print(self.input_header)
    
    def add_widgets(self):
        """add widgets into the Subwindow"""

        #content
        self.content = ttk.Frame(self, padding=(10,10,3,3))
        
        #widgets
        #main_frame
        self.main_frame = ttk.Frame(self.content, borderwidth=2,\
            width=400, height=600) #4 cols and 10 rows
        #buttons
        self.save_button = ttk.Button(self.content, text="Save",\
            command=self.append_rows)
        self.quit_button = ttk.Button(self.content, text="Quit",\
            command=self.destroy)
            
        #column_label
        #Text of each label stay undefinied
        #maxima columns number is 9
        #after definition append each of them into container
        self.col_num_1 = ttk.Label(self.content)
        self.label_container.append(self.col_num_1)
        self.col_num_2 = ttk.Label(self.content)
        self.label_container.append(self.col_num_2)
        self.col_num_3 = ttk.Label(self.content)
        self.label_container.append(self.col_num_3)
        self.col_num_4 = ttk.Label(self.content)
        self.label_container.append(self.col_num_4)
        self.col_num_5 = ttk.Label(self.content)
        self.label_container.append(self.col_num_5)
        self.col_num_6 = ttk.Label(self.content)
        self.label_container.append(self.col_num_6)
        self.col_num_7 = ttk.Label(self.content)
        self.label_container.append(self.col_num_7)
        self.col_num_8 = ttk.Label(self.content)
        self.label_container.append(self.col_num_8)
        self.col_num_9 = ttk.Label(self.content)
        self.label_container.append(self.col_num_9)

        #Entry
        self.str_var_1 = StringVar()
        self.str_var_2 = StringVar()
        self.str_var_3 = StringVar()
        self.str_var_4 = StringVar()
        self.str_var_5 = StringVar()
        self.str_var_6 = StringVar()
        self.str_var_7 = StringVar()
        self.str_var_8 = StringVar()
        self.str_var_9 = StringVar()
        self.entry_1 = ttk.Entry(self.content,\
            textvariable=self.str_var_1)
        self.entry_2 = ttk.Entry(self.content,\
            textvariable=self.str_var_2)
        self.entry_3 = ttk.Entry(self.content,\
            textvariable=self.str_var_3)
        self.entry_4 = ttk.Entry(self.content,\
            textvariable=self.str_var_4)
        self.entry_5 = ttk.Entry(self.content,\
            textvariable=self.str_var_5)
        self.entry_6 = ttk.Entry(self.content,\
            textvariable=self.str_var_6)
        self.entry_7 = ttk.Entry(self.content,\
            textvariable=self.str_var_7)
        self.entry_8 = ttk.Entry(self.content,\
            textvariable=self.str_var_8)
        self.entry_9 = ttk.Entry(self.content,\
            textvariable=self.str_var_9)
        #put them into container
        self.entrys_container.append(self.entry_1)
        self.entrys_container.append(self.entry_2)
        self.entrys_container.append(self.entry_3)
        self.entrys_container.append(self.entry_4)
        self.entrys_container.append(self.entry_5)
        self.entrys_container.append(self.entry_6)
        self.entrys_container.append(self.entry_7)
        self.entrys_container.append(self.entry_8)
        self.entrys_container.append(self.entry_9)
    
    def place_widgets(self):
        """Place the widgets in subwindow"""

        self.content.grid(column=0, row=0, sticky=(N,S,E,W))
        self.main_frame.grid(column=0, row=0, columnspan=4,\
            rowspan=10, sticky=(N,S,E,W))
        
        #The labels and entrys are grided in a loop
        for i in range(len(self.input_header)):
            #give column name to label
            self.label_container[i]["text"] = str(\
                self.input_header[i] + ":  ")
            #grid the label
            self.label_container[i].grid(column=0, row=i,\
                columnspan=1, rowspan=1, sticky=(E))
            #grid the entry
            self.entrys_container[i].grid(column=1, row=i,\
                columnspan=2, rowspan=1, sticky=(E,W))
        
        #buttons
        #last row
        self.save_button.grid(column=2, row=1+i, columnspan=\
            1, rowspan=1, sticky=(S,E))
        self.quit_button.grid(column=3, row=1+i, columnspan=\
            1, rowspan=1, sticky=(S,E))
    
    def sub_resize_config(self):
        """Set resizing feature of the subwindow"""

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.content.columnconfigure(0, weight=0)
        self.content.columnconfigure(1, weight=2)
        self.content.columnconfigure(2, weight=0)
        self.content.columnconfigure(3, weight=0)
        #resize the occupied rows only
        for i in range(len(self.input_header)):
            self.content.rowconfigure(i, weight=2)
        
        #buttons row
        self.content.rowconfigure(i+1, weight=0)
    
    def get_input_info(self):
        """
            get input infomation from the Entrys
            put the inputs into a list and return the lsit
        """

        #append the inputs into list in a loop
        for i in range(len(self.input_header)):
            self.input_container.append(\
                self.entrys_container[i].get())

    def append_rows(self):
        """append row into selected excel file"""

        self.get_input_info()
        #first sheet
        with open_workbook(self.selected_filepath,\
            encoding_override='utf-8') as workbook:

            output_workbook = copy(workbook)
            output_sheet = output_workbook.get_sheet(0)
            #append
            for element_index, element in enumerate(self.input_container):
                output_sheet.write(self.rows_number, element_index, element)
        
            #save
            try:
                output_workbook.save(self.selected_filepath)
                messagebox.showerror(title="Saved!", message=\
                    "Congratulations! You have successfully appended a new record!")
            except:
                messagebox.showerror(title="Error!", message="Someting goes wrong!")