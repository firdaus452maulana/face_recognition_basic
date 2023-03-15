import face_recognition
import cv2

imgMessi = face_recognition.load_image_file('images/Lionel Messi.jpg')
imgMessi = cv2.cvtColor(imgMessi, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgMessi)[0]
cv2.rectangle(imgMessi, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2) # top, right, bottom, left
encodeMessi = face_recognition.face_encodings(imgMessi)[0]

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    if facesCurFrame:
        y1, x2, y2, x1 = facesCurFrame[0]
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

        encodeCam = face_recognition.face_encodings(imgS)[0]

        compareResult = face_recognition.compare_faces([encodeMessi], encodeCam)
        faceDistance = face_recognition.face_distance([encodeMessi], encodeCam)
        print(compareResult, faceDistance)
        cv2.putText(img, f'{compareResult} {round(faceDistance[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Webcam', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
# compareResult = face_recognition.compare_faces([encodeMessi], encodeRonaldo)
# faceDistance = face_recognition.face_distance([encodeMessi], encodeRonaldo)
# print(compareResult, faceDistance)
# cv2.putText(imgRonaldo, f'{compareResult} {round(faceDistance[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

# cv2.imshow('Lionel Messi', imgMessi)
# cv2.imshow('Cristiano Ronaldo', imgRonaldo)
# cv2.waitKey(0)