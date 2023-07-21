# Check-In-Check-Out

  It is applicable to implemented in institutions for security of students. Their parents trust institutes and leave their child they don't know how they are and what they doing. students went out of the campus with intimating their parents so from my project when student went they need to scanned their faces and recognized their identity based on data immediately one sms send to their parents moblie about time and count in and out details. 

Sample Snapshots :
  ![Screenshot from 2023-07-16 22-07-35](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/e82e5229-f826-43bf-97c6-914230f093b4)
  ![IMG_20230721_201323](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/eb955eb4-d351-4051-9cc5-7a81b6478b9c)
![Screenshot from 2023-07-15 10-49-29](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/810dc0b2-7227-4c08-b419-4383a290f54a)


It was Done in Pycharm community so need to  install Pycharm.

Step 1 : Open terminal and enter " git clone https://github.com/Pavan19kumar19/Check-In-Check-Out.git  "

Step 2 : unzip Check in Check Out folder

Step 3 : open Pycharm and create virtual environment venv 
      For more How to create refer this link : https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env

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
        For RealTime Database I was used Firebase application from google provided here is setup to follow.
        create firebase google account and get api key and realtime database url and storage url from the site
        add  at this #firebase and #storage url and uncomment in main.py, AddDataToDatabase.py,EncodeGenerator.py 
        
  ![Screenshot from 2023-07-21 19-50-04](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/e1c86e83-64e8-451b-b156-e26bb09dadd1)

Step 7:
      For send sms in market we need buy the service so i used my mobile to send sms by linking my moblie to smschef site it will sms gateway by our own phone.
      first create account in smschef and add moblie  it send application link need download and link your phone with QR or login by app name smschef details you device linked status visible at android option 
      after that in tools option in website add api key and copy it in the main.py for help refer documentation is present how to use api key in file.
      
  ![Screenshot from 2023-07-21 20-02-08](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/2d055155-685e-46c0-995b-dacad829bdb8)

        add api in main.py at beginning like this

  ![Screenshot from 2023-07-21 20-04-19](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/644eb717-04a2-4c5b-a04b-6ac5558a69f5)

      Step 8 : 
            Add images of students in 216x216 ratio  in the image folder 
            AddDataToDatabase.py file to add students details
             after that run EncodeGenerator.py to encode images and upload to firebase storage
             finally run main.py file to see out puts 

   ![Screenshot from 2023-07-15 10-48-23](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/accb7adc-5163-46ec-ab52-83778031c4ce)

  ![Screenshot from 2023-07-15 10-49-29](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/f04c442d-ef8d-4838-8f54-db475cd944cd)
      
![Screenshot from 2023-07-16 22-16-34](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/e2fb2e34-a2e5-4ca8-9f9b-a209baa61a88)

![Screenshot from 2023-07-15 10-50-52](https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/0c2d7e34-9aee-454e-9182-fa16c0d25c2d)


                      #Hurry !!!!!!!!!!!......... Project Done .

