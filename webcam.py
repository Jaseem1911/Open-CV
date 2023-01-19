
# import the opencv library
import cv2

cam = cv2.VideoCapture("http://192.168.227.225:4747/video")
#cam = cv2.VideoCapture(0)

while True:
    success, frame = cam.read()
    if success:
        cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF==ord('e'):
        break

cam.release()
cv2.destroyAllWindows()
