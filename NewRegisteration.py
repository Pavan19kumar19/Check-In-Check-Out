from datetime import datetime
data = {}
print("<----------------------DETAILS OF STUDENTS TO THE REALTIME DATABASE --------------------->")
id = input("Enter the ID for New Registration:-")
yes = 'y'
while True:
    if 'y' == yes:
        details={}
        name = input("Enter Name:-")
        Gen = input("Gender :-")
        Branch = input("Branch :-")
        year = input("Year :-")
        GroupB = input("Blood Group:-")
        contact = input("Enter Contact with area code example: 91xxxxxx00:-")
        attend = 0
        details.update({'name':name,'Gender':Gen,'Branch':Branch,'Year':year,'BloodG':GroupB,'contact':"+91"+contact,'last_attended':datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'Total_Attendence':attend})
        data[id]=details
        print(data)
        q=''
        while True:
            a= input("!--------------Add Another Student Press 'y' or Exit to  Press 'q' --------->\n")
            if a =='y':
                id = input("Enter the ID for new Registration:-")
                break
            elif a=='q':
                q=a
                break
            else:
                print(" Enter a Valid key")
        if q=='q':
            break

for i,j in data.items():
    print(i," : ",j)