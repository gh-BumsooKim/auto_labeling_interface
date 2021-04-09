import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    
    if ret == True:
        cv2.imshow("Hello world", frame)
        print("Hello while")
    else:
        print("NOT")
        break
    
cap.release()
cv2.destroyAllWindows()
print("Cap release")