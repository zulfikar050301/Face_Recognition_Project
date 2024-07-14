import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import  storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://facerecognitionfirst-default-rtdb.firebaseio.com/",
    'storageBucket' : "facerecognitionfirst.appspot.com"
})


#Importing the mode images into a list
folderPath = 'Images'
pathList = os.listdir(folderPath) #list for every object inside the folder
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentIds.append(os.path.splitext(path)[0]) #make the title or ID separate from . and type file into list

    #OOP database image upload to Firebase
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # print(path)
    # print(os.path.splitext(path)[0]) #make the title or ID separate from . and type file into list
# print(len(imgList))
print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started....")
#read all image that stored in the folder image and turn it into RGB data array
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds] #Store the data from encodeListKnown and studentIds
# print(encodeListKnown)
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()



