import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

detector = HandDetector(detectionCon=.8, maxHands=1)

video = cv2.VideoCapture(0)
last_key_pressed = "None"

while True:
    ret, frame = video.read()
    
    if not ret:
        print("Error: Failed to read frame from the video.")
        break
    
    hands, img = detector.findHands(frame)
    
    if hands:
        hand1 = hands[0]
        
        fingers = detector.fingersUp(hand1)
        print(fingers)
        if sum(fingers) == 5:
            cv2.putText(frame, "Palm Open", (20, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
            if last_key_pressed != "Palm Open":
                pyautogui.press('volume_up')
                last_key_pressed = "Palm Open"
        elif sum(fingers) == 0:
            cv2.putText(frame, "Palm Closed", (20, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
            if last_key_pressed != "Palm Closed":
                pyautogui.press('volume_down')
                last_key_pressed = "Palm Closed"
        elif fingers == [0,1,0,0,0]:
            if last_key_pressed != "Index":
                pyautogui.press('j')
                last_key_pressed = "Index"
        elif fingers == [0,1,1,0,0]:
            if last_key_pressed != "Index and Middle":
                pyautogui.press('l')
                last_key_pressed = "Index and Middle"
        elif fingers == [0,1,1,1,0]:
            if last_key_pressed != "Index, Middle, and Ring":
                pyautogui.press('space')
                last_key_pressed = "Index, Middle, and Ring"
        elif fingers == [0,1,1,1,1]:
            if last_key_pressed != "All Fingers":
                pyautogui.press('volume_mute')
                last_key_pressed = "All Fingers"
    
    cv2.putText(frame, f"Last Key Pressed: {last_key_pressed}", (20, 40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)
    
    cv2.imshow("Frame", frame)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
