import face_recognition
import cv2
import os
import numpy as np


def register(name):
    directory = os.getcwd() + '/imageAttendance/'
    # print(directory)
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        imgC = img.copy()
        # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)

        # Bounding Box
        if facesCurFrame:
            y1, x2, y2, x1 = facesCurFrame[0]
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.imshow('Webcam', img)
        key = cv2.waitKey(1)
        # Quit
        if key == ord('q'):
            break
        # Capture
        elif key == ord('c'):
            if facesCurFrame:
                saveImage = cv2.imwrite(directory + name + ".jpg", imgC)
                if saveImage:
                    print("Register Success")
                break
            else:
                print("No Face Detected")

def login():
    # Encoding List Image Known
    path = 'imageAttendance'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    directory = os.getcwd() + '/imageAttendance/'
    # print(directory)
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        imgC = img.copy()
        # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)

        # Bounding Box
        if facesCurFrame:
            y1, x2, y2, x1 = facesCurFrame[0]
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                # print(faceDis)
                matchIndex = np.argmin(faceDis)

                if faceDis[matchIndex] < 0.50:
                    name = classNames[matchIndex].upper()
                    print(name)
                else:
                    name = 'Unknown'
                    print(name)

        cv2.imshow('Webcam', img)
        key = cv2.waitKey(1)
        # Quit
        if key == ord('q'):
            break
