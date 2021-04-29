# Return dnn label format
# Support Yolo, RCNN format in this version

global label_format_list 
label_format_list = ["yolo", "faster-rcnn"]

def label_format(model='yolo'):
    """
    Return dnn model annotation format
    
    model : used model name, default a yolo
    """
    try:
        model.lower()
    except AttributeError as e:        
        print(model, "is not String Type \n" + 
              "Debugging : Input String Parameters like 'yolo' \n" +
              "with AttributeError :", e)
    else:
        if "yolo" in model.lower():
            # Annotation File Type is txt
            # <x_center> <y_center> <width> <height>
            return "txt"
        elif "faster" and "rcnn" in model.lower():
            # Annotation File Type is xml
            # <x_min> <y_min> <x_max> <y_max>
            return "xml"
        else:
            print("Input Deep Learning Model like 'yolo', 'rcnn' ")
    
            
def test(**conv):
    for key,item in conv.items():
        print(key, item)
    
    
if __name__ == '__main__':
    print("This is the wrong label_format.py file to run")
