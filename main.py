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
        if fingerUp == [1,0,0,0,0]:
            cv2.putText(frame, "Thumb", (20, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
        elif fingerUp == [0,1,0,0,0]:
            cv2.putText(frame, "Index", (20, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
        elif fingerUp == [0,0,1,0,0]:
            cv2.putText(frame, "Middle", (20, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
        elif fingerUp == [0,0,0,1,0]:
            cv2.putText(frame, "Ring", (20, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
        elif fingerUp == [0,0,0,0,1]:
            cv2.putText(frame, "Pinky", (20, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
    
    cv2.imshow("Frame", frame)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
