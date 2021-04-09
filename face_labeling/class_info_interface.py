from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    print("This is the wrong label_format.py file to run")

def get_class_info():
    global user_name
    global user_num
    global dnn_model
    
    try:        
        user_name = entry_name.get()
        user_num = entry_num.get()
        dnn_model = entry_model.get()
    except NameError as e:
        print("Input Class_name and Class_number is not String Type\n"
              "with NameError :", e)
    window.destroy()

def class_info_interface():
    global window
    window = Tk()
    window.title("Auto Labeling Input Class Name")
    
    global entry_num
    global entry_name
    global entry_model
    
    ttk.Label(window, text = "DNN Model : ").grid(row = 0,
                                                  column = 0, 
                                                  padx = 10, pady = 10)
    entry_model = ttk.Entry(window)
    entry_model.grid(row = 0, column = 1, padx = 10, pady = 10)
    
    ttk.Label(window, text = "Class name : ").grid(row = 1,
                                                   column = 0,
                                                   padx = 10, pady = 10)
    entry_name = ttk.Entry(window)
    entry_name.grid(row = 1, column = 1, padx = 10, pady = 10)
    
    ttk.Label(window, text = "Class number : ").grid(row = 2, 
                                                     column = 0,
                                                     padx = 10, pady = 10)
    entry_num = ttk.Entry(window)
    entry_num.grid(row = 2, column = 1, padx = 10, pady = 10)
    ttk.Button(window, text="OK", command=get_class_info).grid(row = 2,
                                                               column = 2, 
                                                               padx = 10, 
                                                               pady = 10)
    
    ttk.Label(window, text = "Username \n\n" +
              "professor_seo \n" +
              "jaeseok \n" +
              "hun \n").grid(row = 3, column = 1, padx = 10, pady = 10)
    
    ttk.Label(window, text = "| Class Name\n\n" +
              "| 0\n| 1\n| 2\n").grid(row = 3, column = 2, 
                                      padx = 10, pady = 10)
    
    window.mainloop()
    
    return user_name, user_num, dnn_model