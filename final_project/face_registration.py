import cv2
import face_recognation 
import pickle
from datetime import datetime

# Creatr an imstance for videoCapture class
cap = cv2.VideoCapture(0)

# Set the image width and height
width, height = 320, 240

# Set the format of the captured image
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Create a face detector using the Haar cascade classifier
face_cascade = cv2.CascadeClassifier('haar_cascade_files/haarcascade_frontalface_default.xml')

# Name
name = input('Enter Your name: ')

# Rooms
access_input = input('Enter room acces (comma-seperated): ')
access_list = access_input.split(',')

# Initalize an empty list to store the face data
face_data = []

capture_count = 0

while True:
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighboors=5, minSize=(30, 30))

	for (x, y, w, h) in faces:
		rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)

		rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RBG)
		face_encodings = face_recognition.faceencodings(rbg_frame, [(y, x+w, y+h, x)]

		for face_encoding in face_encodings:
			face_data.append({"name" : name, 'face' : frame[y:y+h, x:x+w], 'face_encoding' : face_encoding, 'access' : access_list})
