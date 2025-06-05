import cv2
from utils import get_limits
from PIL import Image

while True:
    cap = cv2.VideoCapture(2)
    ret, frame = cap.read()

    color = (0, 255, 0)  # Green color in BGR format
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, get_limits(color)[0], get_limits(color)[1])

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()
    if bbox:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()