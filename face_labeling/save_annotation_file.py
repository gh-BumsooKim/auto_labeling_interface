# Save origin image and annotation file

def save_annotation_file(frame, label_format, output_path=None,
                         class_name=0, class_num=0, index=0, 
                         num_max=500, explain=False):
    try:
        import cv2
        import os
    except ModuleNotFoundError as e:
        print("cv2 is not imported \n" +
              "with ModuleNotFoundError :", e)
    else:
        if output_path is None :
            output_path = os.path.join(os.getcwd() + "\\" + class_name + "\\")
        else:   
            pass
        
        if index < num_max:
            # Support yolo mdoel : [yolo3 version, yolo4 version]
            if label_format is "txt":
                file_bbox = list()
                name = output_path + class_name + "_" + str(index)
                
                cv2.imwrite(name + ".jpg" , frame)
                with open(name + ".txt", 'w') as f:
                    bbox = file_bbox[index-1]
                    f.write(str(bbox[0]) + " " + bbox[1] + 
                            " " + bbox[2] + " " + bbox[3] + 
                            " " + bbox[4])
                    
                # Explainable Annotation File
                # for mismatched bbox in dataset
                if explain is True :
                    cv2.imwrite(name + "_explain.jpg", frame)
                    
            # Support rcnn model : [faster-rcnn]
            elif label_format is "xml":
                pass
            else:
                pass
        else:
            return False
        
if __name__ == '__main__':
    print("This is the wrong save_annotation_file.py file to run")