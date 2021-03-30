# Return dnn label format
# Support Yolo, RCNN format in this version

def label_format(dnn_type):
    try:
        dnn_type.lower()
    except AttributeError as e:        
        print(dnn_type, "is not String Type \n" + 
              "Debugging : Input String Parameters like 'yolo' \n" +
              "with AttributeError :", e)
    else:
        if "yolo" in dnn_type.lower():
            # Annotation File Type is txt
            # <x_center> <y_center> <width> <height>
            return "txt"
        elif "rcnn" in dnn_type.lower():
            # Annotation File Type is xml
            # <x_min> <y_min> <x_max> <y_max>
            return "xml"
        else:
            print("Input Deep Learning Model like 'yolo', 'rcnn' ")
            
        return 0
    
            
if __name__ == '__main__':
    print("This is the wrong label_format.py file to run")