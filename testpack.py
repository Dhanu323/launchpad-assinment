from tabulate import tabulate
class Appointment:
    """Parent / Base Class"""

    def __init__(self, name, phone, height, weight,sex,date):
        self.name = name
        self.phno = phone
        self.height = height
        self.body_weight = weight
        self.sex = sex
        self.datetime = date 
        

    def description(self):
        self.description = input("enter the description")
        print("Enter the prescription")
        self.no = int(input("enter the tottal"))
        self.prescription = {}
        
        for i in range(self.no):
            self.medic_name = input("enter medicin")
            self.medic_quantity = int(input("enter quantity"))
            self.prescription[self.medic_name] = self.medic_quantity
             
        
    def get_medical_report(self):
        print("\t\t\t\t\t\tSpeckbit Health Care Center")
        table = self.prescription.items()
        print(self.datetime,"paticent name: ",self.name,"paticent phone number :",self.phno, "paticent height :",self.height,"paticent weight :",self.body_weight ,"paticent sex:",self.sex ,sep="\n")
        print(tabulate(table, headers=["Medicen","Quantity","consume_timeing"],tablefmt="rst"))

class Managedoctor:
    

    def __init__(self,doc_id):
        self.doc_id = doc_id
        self.doc_ava = []
        self.doc_list = {1:"Dr.vidyadhr : OTHOPEDITION ",2:"Dr.Ashwini : DERMATOLOGIST"}
        if self.doc_id in self.doc_list:
           self.doc_ava.append(self.doc_list[self.doc_id])
           
   
    def doc_avalabale(self):
        print("DOCTERS present today\n")
        table = self.doc_ava
        print(tabulate(table, headers=["Docter "," Specialization"],tablefmt="simple"))