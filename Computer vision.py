import cvzone.SerialModule 
from cvzone.HandTrackingModule import HandDetector 
import cv2 
cap = cv2.VideoCapture(0) 
detector = HandDetector(detecƟonCon=1, maxHands=2) 
ser = cvzone.SerialModule.SerialObject("/dev/cu.usbserial-110") 
while True: 
 # Get image frame 
 success, img = cap.read() 
 # Find the hand and its landmarks 
 hands, img = detector.findHands(img) # with draw 
 # hands = detector.findHands(img, draw=False) # without draw 
 if hands: 
 # Hand 1 
 hand1 = hands[0] 
 lmList1 = hand1["lmList"] # List of 21 Landmark points 
 bbox1 = hand1["bbox"] # Bounding box info x,y,w,h 
 centerPoint1 = hand1['center'] # center of the hand cx,cy 
 handType1 = hand1["type"] # Handtype LeŌ or Right
 fingers1 = detector.fingersUp(hand1) 
 print(fingers1) 
 ser.sendData(fingers1) 
 # if len(hands) == 2: 
 # # Hand 2 
 # hand2 = hands[1] 
 # lmList2 = hand2["lmList"] # List of 21 Landmark points 
 # bbox2 = hand2["bbox"] # Bounding box info x,y,w,h 
 # centerPoint2 = hand2['center'] # center of the hand cx,cy 
 # handType2 = hand2["type"] # Hand Type "LeŌ" or "Right"
 # 
 # fingers2 = detector.fingersUp(hand2) 
 # Find Distance between two Landmarks. Could be same hand or 
different hands 
 # length, info, img = detector.findDistance(lmList1[8], lmList2[8], 
img) # with draw 
 # # length, info = detector.findDistance(lmList1[8], lmList2[8]) # 
with draw 
 # Display 
 cv2.imshow("Image", img) 
 cv2.waitKey(1) 
cap.release() 
cv2.destroyAllWindows() 


# Explanation :
# This code is wriƩen in Python and uses the OpenCV library to detect and 
# track hand movements in real-Ɵme from a video stream obtained from a 
# camera connected to the computer. It also uses the cvzone.SerialModule 
# module to establish serial communicaƟon with an external device, and 
# send data related to the hand movements. 
# import cvzone.SerialModule: ImporƟng the cvzone.SerialModule module 
# which provides a SerialObject class to establish serial communicaƟon.
# from cvzone.HandTrackingModule import HandDetector: ImporƟng the 
# HandDetector class from the cvzone.HandTrackingModule module which 
# provides a pre-trained hand detecƟon model.
# import cv2: ImporƟng the OpenCV library which provides funcƟons to 
# handle image and video input/output, and image processing. 
# cap = cv2.VideoCapture(0): CreaƟng a VideoCapture object to capture 
# frames from the default camera (camera index 0). 
# detector = HandDetector(detecƟonCon=0.8, maxHands=2): CreaƟng a 
# HandDetector object with a detecƟon confidence threshold of 0.8, and 
# maximum number of hands to detect set to 2. 
# ser = cvzone.SerialModule.SerialObject(portNo="COM5", 
# baudRate=9600): CreaƟng a SerialObject object to establish serial 
# communicaƟon over port COM5, with a baud rate of 9600.
# while True:: StarƟng an infinite loop to conƟnuously process video 
# frames. 
# success, img = cap.read(): Reading a video frame from the camera. 
# hands, img = detector.findHands(img): Using the findHands method of 
# the HandDetector object to detect hands in the current frame, and get 
# the hand landmarks. This method returns a list of detected hands, and 
# the original image with hand landmarks drawn on it. 
# if hands:: Checking if at least one hand is detected. 
# hand1 = hands[0]: Assuming the first detected hand is the primary hand, 
# and assigning its informaƟon to the hand1 variable.
# lmList1 = hand1["lmList"]: ExtracƟng the list of 21 landmark points for 
# the first hand, which include points for fingers, palm, and wrist. 
# bbox1 = hand1["bbox"]: ExtracƟng the bounding box informaƟon for the 
# first hand, which includes its x, y posiƟon and width, and height.
# centerPoint1 = hand1['center']: ExtracƟng the center point coordinates 
# of the first hand. 
# handType1 = hand1["type"]: ExtracƟng whether the first hand is a leŌ or 
# right hand. 
# fingers1 = detector.fingersUp(hand1): Using the fingersUp method of the 
# HandDetector object to get a list of booleans indicaƟng which fingers of 
# the first hand are up. 
# ser.sendData(fingers1): Sending the fingers1 data over the serial port to 
# the external device. 
# cv2.imshow("Image", img): Displaying the current frame with hand 
# landmarks drawn on it. 
# cv2.waitKey(1): WaiƟng for 1 millisecond for a keyboard event. If any key 
# is pressed, the loop will exit. 
# cap.release(): Releasing the camera and closing the video stream. 
# cv2.destroyAllWindows(): Closing all OpenCV windows.
