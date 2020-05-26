from testpack import Appointment
from testpack import Managedoctor
from datetime import datetime

Visit_doc_paticent_name = []
Medical_ledger = {}
print("Welcome To Speckbit Health Care Center")

while True:
    print("^^"*30)
    choice =  int(input("What would u like to do: \n\
        1. DOCTER\n\
        2. PATICENT\n\t\
        3. EXIT--> "))
    if choice == 1:
        doc_id = int(input("Please enter your id"))
        Doctor = Managedoctor(doc_id)


    if choice == 2:

        print("-*"*30)
        ch = int(input("What would u like to do: \n\
    		1. Get Appointment\n\
    		2. Visit Doctor\n\t\
            3. Medical_Certificate-->"))


        if ch == 1:
            Doctor.doc_avalabale()
            name = input(" paticent Name: ").upper()
            phno = input("paticent Phone: ")
            height = float(input("paticent height: "))
            weight = float(input("paticent weight: "))
            sex = input("paticent sex: ")
            date = datetime.now()

            appointment = Appointment(name, phno,  height, weight, sex,date)
            Medical_ledger[name] = appointment
            
        elif ch == 2:
            name = input(" paticent Name: ").upper()
            Visit_doc_paticent_name.append(name)
            if name in Medical_ledger.keys():
                print(Visit_doc_paticent_name)
                appointment.description()
            else:
                print("Please get the Appointment")    
        elif ch == 3:
            name = input(" paticent Name: ").upper()
            if name in Visit_doc_paticent_name:
                appointment = Medical_ledger[name]
                appointment.get_medical_report()
            else:
                print("Please Visit the Doctor")   
                

        else:
            break