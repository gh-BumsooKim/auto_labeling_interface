# Save origin image and annotation file

def save_annotation_file(frame, output_path, label_format,
                         class_name=0,  index=0, 
                         num_max=500, explain=None):
    try:
        import cv2
    except ModuleNotFoundError as e:
        print("cv2 is not imported \n" +
              "with ModuleNotFoundError :", e)
    else:
        if index < num_max:
            # Support yolo version
            if label_format is "txt":
                file_bbox = list()
                name = output_path + class_name + "_" + str(index)
                
                if not explain:
                    cv2.imwrite(name + ".jpg" , frame)
                    with open(name + ".txt", 'w') as f:
                        bbox = file_bbox[index-1]
                        f.write(str(bbox[0]) + " " + bbox[1] + 
                                " " + bbox[2] + " " + bbox[3] + 
                                " " + bbox[4])
                else:
                    pass
            # Support rcnn model
            elif label_format is "xml":
                pass
            else:
                pass
        else:
            return False
        
if __name__ == '__main__':
    print("This is the wrong save_annotation_file.py file to run")