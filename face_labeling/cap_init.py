try:
    import cv2
except ImportError as e:
    print("Opencv lib is not imported\n"
        "with ImportError :", e)

def cap_init(**kwargs):
    try:
        import cv2
    except ModuleNotFoundError as e:
        print("cv2 library is not imported\n"
              "with ModuleNotFoundError :", e)
    else:
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        try:
            while True:
                ret, frame = cap.read()
                #####################
                #                   #
                if ret == True:
                    cv2.imshow("Hello world", frame)
                else:
                    print("Camera is not connected")
                    break
                #                   #
                #####################
        except KeyboardInterrupt:
            print("Error except : KeyboardInterrupt")
            pass
            
        cap.release()
        cv2.destroyAllWindows()

def cap():
    global test
    test = cv2.VideoCapture(0)
    test.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    test.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    while True:
        ret, frame = test.read()
        cv2.imshow("Hello world", frame)
        
    test.release()
    cv2.destroyAllWindows()        
    
        
if __name__ == '__main__':
    print("This is the wrong save_annotation_file.py file to run")