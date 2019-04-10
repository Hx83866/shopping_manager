#It is a GUI for managment of data, which are generated during the purchasing oversea.

from application import Application

#generate a object
shopping_manager = Application()
shopping_manager.master.title("Shopping Manager")
shopping_manager.mainloop()