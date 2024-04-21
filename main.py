import cv2
from cvzone.HandTrackingModule import HandDetector
import math

detector = HandDetector(detectionCon=.8, maxHands=1)

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    
    if not ret:
        print("Error: Failed to read frame from the video.")
        break
    
    hands, img = detector.findHands(frame)
    
    if hands:
        hand1 = hands[0]
        
        fingerUp = detector.fingersUp(hand1)
        centerPoint = hand1["center"]
        print(fingerUp)
        if fingerUp == [1,0,0,0,0]:
            cv2.putText(frame, "Thumb", (20, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
        elif fingerUp == [0,1,0,0,0]:
            cv2.putText(frame, "Index", (20, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
            #indexFinger = lmList[8:12]
            #dx = indexFinger[0][0] - indexFinger[1][0]
            #dy = indexFinger[0][1] - indexFinger[1][1]
            #angle = math.atan2(dy, dx)
            #angle = math.degrees(angle)
            #cv2.putText(frame, f"Angle: {int(angle)}", (20, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
        elif fingerUp == [0,0,1,0,0]:
            cv2.putText(frame, "Middle", (20, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
        elif fingerUp == [0,0,0,1,0]:
            cv2.putText(frame, "Ring", (20, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
        elif fingerUp == [0,0,0,0,1]:
            cv2.putText(frame, "Pinky", (20, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
        elif sum(fingerUp) >= 4:
            cv2.putText(frame, "Open: " + str(centerPoint), (20, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
    
    cv2.imshow("Frame", frame)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
