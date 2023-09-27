# Check-In-Check-Out

The Purpose of the Check In Check Out System application is used to know the current
status of the student whether he/she present inside of the campus or outside of the campus. It
is applicable to implement in institutions to maintain student's status. We can use it at the
main entrance of the University/College to track student's status whether he or she are within
the campus or outside the campus.
More beneficially it can be implemented in Residential campuses to maintain student status of
presence/absence in the campus. Whenever student wants to go out of the campus or come
into the campus, student need to give his facial attendance at main entrance using this
software.
A message will be sent to registered mobile number (We use Parent mobile number for
conveying student status to their parents) which contains the name of the student, time stamp,
status of presence/absence of the student
  
Sample Snapshots :
  ![Screenshot from 2023-07-16 22-07-35](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/e82e5229-f826-43bf-97c6-914230f093b4)
  ![IMG_20230721_201323](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/eb955eb4-d351-4051-9cc5-7a81b6478b9c)
![Screenshot from 2023-07-15 10-49-29](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/810dc0b2-7227-4c08-b419-4383a290f54a)


It was done in Pycharm community. Need to use Pycharm .

Step 1 : Open terminal and enter " git clone https://github.com/Pavan19kumar19/Check-In-Check-Out.git  "

Step 2 : Unzip Check in Check Out folder

Step 3 : Open Pycharm and create virtual environment venv 
  For more details refer this link : https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env

Step 4 : Open check in check out folder in pycharm 

Step 5 : Now install Required packages 
        open setting > open interpreter > + packages>
            follow this order : cmake
                                dlib
                                face-recognition
                                cvzone
                                opencv version 4.5
       ![Screenshot from 2023-07-21 19-48-02](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/a8ab0219-fe6f-484b-b10f-8b4a847d6297)
            
Step 6 : 
        For RealTime Database I used Firebase application. 
        Follow below steps to setup Firebase Application        
        • Create firebase google account, get realtime database url and storage url from the site.        
        • Replace #firebase and #storage with above urls respectively and uncomment in these three files           main.py,AddDataToDatabase.py,EncodeGenerator.py 
        
  ![Screenshot from 2023-07-21 19-50-04](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/e1c86e83-64e8-451b-b156-e26bb09dadd1)

Step 7:
      In order to send sms alert to registered mobile, here I have linked my mobile with SMSCHEF website.
      Steps to link with SMSCHEF
      • First create account in smschef and link moblie with it. And then it sends application link and we need to download and link your phone with QR or login into the application and details of linked mobile/device will be displayed at android option in SMSCHEF website. 
      • After that you need to generate new api key under tools option of SMSCHEF website and copy it to the main.py file. Refer doc option to add api key to the file.
      
  ![Screenshot from 2023-07-21 20-02-08](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/2d055155-685e-46c0-995b-dacad829bdb8)

        add api in main.py at beginning like this

  ![Screenshot from 2023-07-21 20-04-19](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/644eb717-04a2-4c5b-a04b-6ac5558a69f5)

      Step 8 : 
            Add images of students in 216x216 ratio  in the image folder.
            
      SOFTWARE SETUP DONE. Now let's run the software by using below steps.
            • Run AddDataToDatabase.py file to add students details.
            • Then run EncodeGenerator.py to encode images and upload images to firebase storage.
            • Finally run main.py file to get software application.

   ![Screenshot from 2023-07-15 10-48-23](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/accb7adc-5163-46ec-ab52-83778031c4ce)

  ![Screenshot from 2023-07-15 10-49-29](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/f04c442d-ef8d-4838-8f54-db475cd944cd)
      
![Screenshot from 2023-07-16 22-16-34](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/e2fb2e34-a2e5-4ca8-9f9b-a209baa61a88)

![Screenshot from 2023-07-15 10-50-52](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/0c2d7e34-9aee-454e-9182-fa16c0d25c2d)


                      #Hurry !!!!!!!!!!!......... Project Done .

