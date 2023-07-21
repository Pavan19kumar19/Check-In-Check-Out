import os
import pickle
import cv2
import cvzone
import face_recognition
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime
import requests
apiSecret ="ae0bfc03972ab23bc363d5f0537ed71dcb6fb1fe"
deviceId = "00000000-0000-0000-67fa-04c5ab830c8f"
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://check-in-check-out-a0fbc-default-rtdb.firebaseio.com/",
    'storageBucket':"check-in-check-out-a0fbc.appspot.com"
})
bucket = storage.bucket()

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
imgBackground = cv2.imread('Resources/background.png')
#importing the mode image into a list
folderModePath = 'Resources/Modes'
modePath = os.listdir(folderModePath)
imgModeList = []
for path in modePath:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
#load the Encoding file
print("Loading Encode file ....")
file = open("EncodeFile.p",'rb')
encodeListwithID = pickle.load(file)
encodeListKnown,studentIds =encodeListwithID
print("Encode File Loaded")

modeType = 0
counter = 0
id = -1
imgStudent = []
status = True
while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #encode live face regnition in the frame
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)

    imgBackground[162:162+480,55:55+640] = img
    imgBackground[44:44+633,808:808+414] = imgModeList[modeType]
    if faceCurFrame:
        for encodeFace,faceloc in zip(encodeCurFrame,faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            # print("match",matches)
            # print("FaceDis",faceDis)
            matchIndex  = np.argmin(faceDis)
            # print(matchIndex)
    #finding matches Face
            if matches[matchIndex]:
                # print("Know Face Detected")
                # print(studentIds[matchIndex])
                y1,x2,y2,x1 = faceloc
                y1 ,x2, y2, x1 = y1 * 4,x2 * 4 ,y2 * 4, x1 * 4
                bbox = 55+x1 ,162+y1,x2-x1,y2-y1
                imgBackground =cvzone.cornerRect(imgBackground,bbox,rt=0)#bounding box
                id = studentIds[matchIndex]
                if counter == 0:
                    counter = 1
                    modeType = 1
        if counter!= 0:
            if counter == 1 :
                studentInfo = db.reference(f'Student/{id}').get()
                #get image from storage
                blob  = bucket.get_blob(f'Images/{id}.jpg')
                array = np.frombuffer(blob.download_as_string(),np.uint8)
                imgStudent = cv2.imdecode(array,cv2.COLOR_BGR2RGB)
                #update data of attendance
                datatimeObject = datetime.strptime(studentInfo['last_attended'],
                                                  "%Y-%m-%d %H:%M:%S")

                secondsElapsed = (datetime.now()-datatimeObject).total_seconds()
                print(secondsElapsed)
                if secondsElapsed >20:
                    ref= db.reference(f'Student/{id}')
                    studentInfo['Total_Attendence'] += 1
                    ref.child('Total_Attendence').set(studentInfo['Total_Attendence'])
                    ref.child('last_attended').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    modeType = 3
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
            if modeType !=3 :
                if 10<counter<20:
                    if status:
                        modeType = 2
                        status = False
                    else:
                        modeType = 4
                        status = True
                imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
                if counter <=10:
                # print(studentInfo)
                    sen = True
                    cv2.putText(imgBackground,str(studentInfo['Total_Attendence']),(861,125),
                                cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)#adding attendance
                    cv2.putText(imgBackground, str(studentInfo['Gender']), (1006, 550),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1)  # adding Gender
                    cv2.putText(imgBackground, str(id), (1006, 493),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1)  # adding id
                    cv2.putText(imgBackground, str(studentInfo['Branch']), (910, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100,100,100), 1)  # adding branch
                    cv2.putText(imgBackground, str(studentInfo['Year']), (1025, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100,100,100), 1)  # adding year
                    cv2.putText(imgBackground, str(studentInfo['BloodG']), (1125, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)  # adding year
                    (w,h),_ = cv2.getTextSize(studentInfo['name'],cv2.FONT_HERSHEY_COMPLEX,1,1)
                    offset = (414-w)//2 #middle name
                    cv2.putText(imgBackground, str(studentInfo['name']), (808+offset, 445),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)  # adding name
                    imgBackground[175:175+216,909:909+216] = imgStudent
                    phone = str(studentInfo["contact"])
                    message = "Hello, Your child " +str(studentInfo['name'])+ " was went for out of the Campus at "+ datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    message = {
                        'secret': apiSecret,
                        'mode': 'devices',
                        'device': deviceId,
                        'sim': 1,
                        'priority': 1,
                        'phone': phone,
                        'message': message
                    }
                    if sen == True:
                        r = requests.post(url="https://www.cloud.smschef.com/api/send/sms", params=message)
                        status= r.json()
                        print(status)
                        sen = False

            counter += 1
            if counter>=500:
                counter = 0
                modeType = 0
                studentInfo = []
                imgStudent = []
                imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
                sen = True
    else:
        modeType = 0
        counter = 0
    cv2.imshow("FAce Recognition",imgBackground)
    cv2.waitKey(1)
