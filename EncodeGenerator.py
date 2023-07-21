import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://check-in-check-out-a0fbc-default-rtdb.firebaseio.com/",
    'storageBucket':"check-in-check-out-a0fbc.appspot.com"
})


#importing the student Images
folderPath = 'Images'
Pathlist = os.listdir(folderPath)
imgList = []
studentIds = []
for path in Pathlist:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    #spliting of path to get id's
    studentIds.append(os.path.splitext(path)[0])

    fileName =os.path.join(folderPath,path)
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    print("Uploaded image successfully")
print(studentIds)
#encoding for each image
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
print("Encoding Started")
encodeListKnown = findEncodings(imgList)
encodeListwithID = [encodeListKnown,studentIds]
print("Encoding Complete")

#saving in a pickle file
file = open("EncodeFile.p",'wb')
pickle.dump(encodeListwithID,file)
file.close()
print("File Saved")