from tkinter import *
from tkinter import ttk

def get_class_info():
    global user_id
    global user_num
    user_id = entry_name.get()
    user_num = entry_num.get()
    window.destroy()

def class_info_interface():
    window = Tk()
    window.title("Auto Labeling Input Class Name")
    
    user_id = StringVar()
    user_num = StringVar()
    
    ttk.Label(window, text = "Username : ").grid(row = 0, column = 0, padx = 10, pady = 10)
    entry_name = ttk.Entry(window, textvariable = user_id)
    entry_name.grid(row = 0, column = 1, padx = 10, pady = 10)
    
    ttk.Label(window, text = "Class number : ").grid(row = 1, column = 0, padx = 10, pady = 10)
    entry_num = ttk.Entry(window, textvariable = user_num)
    entry_num.grid(row = 1, column = 1, padx = 10, pady = 10)
    ttk.Button(window, text="OK", command=get_class_info).grid(row = 1, column = 2, padx = 10, pady = 10)
    
    ttk.Label(window, text = "Username \n\n" +
              "professor_seo \n" +
              "jaeseok \n" +
              "hun \n").grid(row = 2, column = 1, padx = 10, pady = 10)
    
    ttk.Label(window, text = "| Class Name\n\n" +
              "| 0\n| 1\n| 2\n").grid(row = 2, column = 2, padx = 10, pady = 10)
    
    window.mainloop()