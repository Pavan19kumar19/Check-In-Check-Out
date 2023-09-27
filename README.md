# Check-In-Check-Out-System(using Face-Recognition)

The Purpose of the Check In Check Out System application is used to know the currentstatus of the student whether he/she present inside of the campus or outside of the campus.

It is applicable to implement in institutions to maintain student's status. 

We can use it at the main entrance of the University/College to track student's status whether he or she are within the campus or outside the campus.

More beneficially it can be implemented in Residential campuses to maintain student status of presence/absence in the campus. Whenever student wants to go out of the campus or come into the campus, student need to give his facial attendance at main entrance using this software.

A message will be sent to registered mobile number (We use Parent mobile number for conveying student status to their parents) which contains the name of the student, time stamp,
status of presence/absence of the student.
  
# Snapshots of Check In Check Out System:

<img width="960" alt="Screenshot 2023-08-09 171403" src="https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/0353f986-7a08-409a-bca5-8d03d3d92a22">
<img width="960" alt="Screenshot 2023-08-10 110327" src="https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/6ee0f35a-13c0-4d66-9ae5-ad3177f4f667">
<img width="960" alt="Screenshot 2023-09-27 122654" src="https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/123aa1b6-1eb3-4e9c-8de5-b5a252760ead">


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
  
                In the Real time Database data format in FIREBASE.
  <img width="960" alt="Screenshot 2023-08-09 120539" src="https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/3fd7a188-74a7-4684-a11a-af52fe4f9830">


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
<img width="960" alt="Screenshot 2023-08-09 114724" src="https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/c16cd372-51ea-48f7-a62a-f610d8d52690">
<img width="960" alt="Screenshot 2023-09-27 123655" src="https://github.com/Pavan19kumar19/Check-In-Check-Out/assets/64640403/1e92fb5e-a9f8-44f5-818d-146070d0a000">


                                             Checking Individual student Status.

   

                      #Hurry !!!!!!!!!!!......... Project Done .



Project Done by

    Ediga Pavan Kumar
    
      9581494014
      
LinkedIn Profile: https://www.linkedin.com/in/pavan-kumar-ediga-7189291aa

