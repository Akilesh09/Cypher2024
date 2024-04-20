import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=.8, maxHands=1)

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    
    if not ret:
        print("Error: Failed to read frame from the video.")
        break
    
    hands, img = detector.findHands(frame)
    
    if hands:
        lmList = hands[0]
        
        fingerUp = detector.fingersUp(lmList)
        print(fingerUp)
    
    cv2.imshow("Frame", frame)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
