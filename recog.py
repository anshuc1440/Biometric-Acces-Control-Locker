import cv2
import numpy as np
import serial

cascadePath = "haarcascade_frontalface_default.xml"
cam = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer\\trainningData.yml")
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
id = 0

names = ['vikas', 'naman', 'none', 'Ilza', 'Z', 'W']

#minW = 0.1 * cam.get(3)
#minH = 0.1 * cam.get(4)

arduino = serial.Serial('COM14', 9600)  # Change 'COM14' to the correct port for your Arduino

while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,  # Adjust this value
        minNeighbors=5,   # Adjust this value
       # minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        if confidence > 60:
            detected_name = names[id]
            confidence = "  {0}%".format(round(confidence))

            if detected_name == 'naman':
                try:
                    arduino.write(b'1')  # Signal to turn on the LED
                except Exception as e:
                    print(f"Error communicating with Arduino: {e}")
        else:
            detected_name = "Unknown"
            confidence = "  {0}%".format(round(confidence))

        cv2.putText(img, str(detected_name), (x+5, y-5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x+5, y+h-5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
arduino.close()
