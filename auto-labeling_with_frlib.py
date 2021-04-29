## pip install pyinstaller X
## pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip


import face_recognition
import cv2
import numpy as np
import os
from tkinter import *
from tkinter import ttk
import threading
import time


def test():   
    global cap
    cap = cv2.VideoCapture(0)
    
def get_userID():
    global user_id
    global user_num
    user_id = entry_name.get()
    user_num = entry_num.get()
    window.destroy()

if __name__ == "__main__":
    AUTO = False
    
    th = threading.Thread(target=test)
    th.start()
    
    '''
    Set
    
    0 - output_path, detector path
    1 - max_num
    2 - class_name
    3 - class_num
    
    '''
    
    
    
    #
    #   interface
    #
    
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
    ttk.Button(window, text="OK", command=get_userID).grid(row = 1, column = 2, padx = 10, pady = 10)
    
    ttk.Label(window, text = "Username \n\n" +
              "professor_seo \n" +
              "jaeseok \n" +
              "hun \n").grid(row = 2, column = 1, padx = 10, pady = 10)
    
    ttk.Label(window, text = "| Class Name\n\n" +
              "| 0\n| 1\n| 2\n").grid(row = 2, column = 2, padx = 10, pady = 10)
    
    window.mainloop()
    
    print(user_id, user_num)
    
    #
    #   Dataset 
    #
    
    os.makedirs(user_id)
    output_path = os.path.join(os.getcwd() + "\\" + user_id + "\\")
    ##output_path = "C:/Users/GRlab/Downloads/darknet-master/darknet-master/build/darknet/x64/data/obj/na/"
    
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #Absolute Path
    #haarcascade_profileface.xml
    
    
    
    th.join()
    
    
    #
    #   ML Image Capture
    #<kbd>w</kbd> | Capture 1 Image |
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    while True:
        ret, frame = cap.read()
        cv2.imshow("Image Capture, Press 'w'",frame)
    
        if cv2.waitKey(1) & 0xFF == ord('w'):
            cv2.imwrite(user_id + "_ml.jpg", frame)
            cap.release()
            cv2.destroyAllWindows()
            break
        
    cap_dataset = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    print(cap_dataset.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap_dataset.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = cap_dataset.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap_dataset.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    file_bbox = list()
    index = 0
    max_num = 2000
    class_name = user_id
    class_num = user_num
    
    # -- Comparision --
    # -- Origin      --
    # -- 1 Image     --
    
    custom_image = face_recognition.load_image_file(user_id + "_ml.jpg")
    custom_face_encoding = face_recognition.face_encodings(custom_image)[0]
    
    known_face_encodings = [
        custom_face_encoding
    ]
    known_face_names = [
        class_name
    ]
    
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    
    #detector = cv2.CascadeClassifier('C:/Users/GRlab/Desktop/haarcascade_frontalface_default.xml') #Absolute Path
          
    
    while True:
        ret, frame = cap_dataset.read()
        
        img_org = frame.copy()
        img_cv = frame.copy()
        gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
        rgb_small_frame = small_frame[:, :, ::-1]
    
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                
                # START = comparision
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    #name = "Matched"
                # END = comparision
                face_names.append(name)
    
        process_this_frame = not process_this_frame
    
    
        for (top, right, bottom, left), name in zip(face_locations, face_names):    
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
    
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    
            cv2.rectangle(frame, (left, bottom), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            
            x=left
            y=top
            w=right-left
            h=bottom-top
            
            X = format(round((x+w/2)/width,6),".6f")
            Y = format(round((y+h/2)/height,6),".6f")
            W = format(round(w/width,6),".6f")
            H = format(round(h/height,6),".6f")
            
            #print(X, Y, W, H)
            #print(top,bottom,right,left)
            #print(face_names)
            
        # OpenCV Haar Method
        faces = detector.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            
        # OpenCV window imshow
        #cv2.imshow('Opencv_haar',img_cv)
        #cv2.imshow('f-r-lib', frame)
        
        #add_img = np.hstack((img_cv, frame))
        cv2.imshow("window, (Quit = press 'q' / Capture = press 'w' "
                   "/ Auto Capture = 'e'", frame)
        
        if AUTO == False:
            if cv2.waitKey(1) & 0xFF == ord('e'):
                AUTO = True
            
        if cv2.waitKey(1) & 0xFF == ord('w') or AUTO == True:
            if index!=max_num:
                if class_name in face_names : #and len(faces) != 0:
                    if len(name) != 0:
                        file_bbox.append([class_num,X,Y,W,H])
                        index+=1   
                        
                        name = output_path + class_name + "_" + str(index)
                        cv2.imwrite(name + ".jpg" , img_org)
                        with open(name + ".txt", 'w') as f:
                            bbox = file_bbox[index-1]
                            f.write(str(bbox[0]) + " " + bbox[1] + 
                                    " " + bbox[2] + " " + bbox[3] + 
                                    " " + bbox[4])
                            
                        print(index)
                        print(X, Y, W, H)
                else: print("Not matched")                
            else:
                print("num_file is " + str(index))
                print('\007') #alart
                cap_dataset.release()
                cv2.destroyAllWindows()
                break
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            print('\007')
            cap_dataset.release()
            cv2.destroyAllWindows()
            break
        else: pass
    
    #cap.release()
    #cv2.destroyAllWindows()