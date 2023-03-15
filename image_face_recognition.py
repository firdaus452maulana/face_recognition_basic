import face_recognition
import cv2
import numpy as np

imgMessi = face_recognition.load_image_file('images/Lionel Messi.jpg')
imgMessi = cv2.cvtColor(imgMessi, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgMessi)[0]
cv2.rectangle(imgMessi, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2) # top, right, bottom, left

imgRonaldo = face_recognition.load_image_file('images/Cristiano Ronaldojpg.jpg')
imgRonaldo = cv2.cvtColor(imgRonaldo, cv2.COLOR_BGR2RGB)

faceLocRonaldo = face_recognition.face_locations(imgRonaldo)[0]
cv2.rectangle(imgRonaldo, (faceLocRonaldo[3], faceLocRonaldo[0]), (faceLocRonaldo[1], faceLocRonaldo[2]), (255, 0, 255), 2)

encodeMessi = face_recognition.face_encodings(imgMessi)[0]
encodeRonaldo = face_recognition.face_encodings(imgRonaldo)[0]

compareResult = face_recognition.compare_faces([encodeMessi], encodeRonaldo)
faceDistance = face_recognition.face_distance([encodeMessi], encodeRonaldo)
print(compareResult, faceDistance)
cv2.putText(imgRonaldo, f'{compareResult} {round(faceDistance[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Lionel Messi', imgMessi)
cv2.imshow('Cristiano Ronaldo', imgRonaldo)
cv2.waitKey(0)



# imgElon = face_recognition.load_image_file('images/Elon Musk.jpg')
# imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
# imgTest = face_recognition.load_image_file('images/Bill Gates.jpg')
# imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
#
# faceLoc = face_recognition.face_locations(imgElon)[0]
# encodeElon = face_recognition.face_encodings(imgElon)[0]
# cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
#
# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)
#
# results = face_recognition.compare_faces([encodeElon], encodeTest)
# faceDis = face_recognition.face_distance([encodeElon], encodeTest)
# print(results, faceDis)
# cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
#
# cv2.imshow('Elon Musk', imgElon)
# cv2.imshow('Elon Test', imgTest)
# cv2.waitKey(0)