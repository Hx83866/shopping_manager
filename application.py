#define a class for a GUI
from tkinter import ttk
import tkinter.messagebox as msgb

class Application(ttk.Frame):
    """继承ttk中的Frame为父类"""
    
    def __init__(self, master=None):
        """初始化属性"""
        
        ttk.Frame.__init__(self, master)
        #self.master = master
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        """创建组件"""
        
        self.search_button = ttk.Button(self)
        self.search_button["text"] = "Search"
        self.search_button["command"] = self.search
        self.search_button.pack(side="left")
        
        self.edit_button = ttk.Button(self)
        self.edit_button["text"] = 'Edit'
        self.edit_button["command"] = self.edit
        self.edit_button.pack(side="right")
        
    def search(self):
        """提供搜索数据库的功能"""
        
        msgb.showinfo(title='Search', message="Under Construction!\nPlease Wait!")
        
    def edit(self):
        """提供修改数据库的功能"""
        
        msgb.showinfo(title='Edit', message="Under Construction!\nPlease Wait!")