import numpy as np
import cv2 as cv
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands






def CreateMarks(cap):
	with mp_hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
		success, image = cap.read()
		
		image.flags.writeable = False
		image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
		results = hands.process(image)

		    
		image.flags.writeable = True
		image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
		if results.multi_hand_landmarks:
			for hand_landmarks in results.multi_hand_landmarks:
				mp_drawing.draw_landmarks(
					image,
					hand_landmarks,
					mp_hands.HAND_CONNECTIONS,
					mp_drawing_styles.get_default_hand_landmarks_style(),
					mp_drawing_styles.get_default_hand_connections_style())
	return image
