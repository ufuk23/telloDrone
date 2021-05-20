import cv2
from easytello import tello
import time

drone = tello.Tello()
time.sleep(3)
print("land")

# Turning on stream
drone.streamon()

telloVideo = cv2.VideoCapture("udp://@0.0.0.0:11111")
#telloVideo = cv2.VideoCapture("udp://@192.168.10.1:11111")


ret = False
scale = 3

while True:

    ret, frame = telloVideo.read()
    if ret:
        height, width, layers = frame.shape
        new_h = int(height / scale)
        new_w = int(width / scale)
        resize = cv2.resize(frame, (new_w, new_h))
        cv2.imshow('Tello', resize)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("test.jpg", resize)  # writes image test.jpg to disk
        print("Take Picture")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
telloVideo.release()
cv2.destroyAllWindows()