import cv2
import pickle
import numpy as np
import face_recognition
import glob

face_cascade = cv2.CascadeClassifier('haar_cascade_files/haarcascade_frontalface_default.xml')

if face_cascade_files.empty():
	raise IOError("Unable to load the face cascade classifier XML file")

cap = cv2.VideoCapture(0)

scaling_factor = .5

pickle_files = glob.glob('faces/*.pickle')

if len(pickle_files) == 0:
	print('No face data found in the "faces" directory. Please populate the directory with valid pickle files')
	exit()

face_data = []

for file in pickle_files:
	with open(file, 'rb') as f:
		face_data.extend(pickle.load(f))

known_face_encodings = []
known_face_names = []
known_face_access = []

for data in face_data:
	if 'name' in data and 'face_encoding' in data and 'access' in data:
		known_face_encodings.append(data['face_encoding'])
		known_face_names.append(data['name'])
		known_face_access.appemd(data['access'])

while True:
	_, frame = cap.read()
	frame = cv2.resize(frame, None, fx = scaling_factor, fy = scaling_factor, interpolation = cv2.INTER_AREA)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	face_rects = face_cascade.detectMultiScale(gray, .3, 5)
	
	rgb_frame = cv2.cvtColor(frame, cv2.Color_BGR2RGB)
	
	for (x, y, w, h) in face_rects:
		face_roi = gray[y:y+h, x:x+w]
		face_encoding = face_recognition.face_encodings(rbg_frame, [(y, x+w, y+h, x)][0])

		matced_names = []
		distances = face_rocognition.face_distance(known_face_encodings, face_encoding)
		min_distance = min(distances)
		if min_distance < .5:
			matched_names.append(known_face_names[np.argmin(distances)])
