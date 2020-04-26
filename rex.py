key = []
no = int(input("enter the number of students"))
zo = int(input("enter the number of subject"))
def loki():
    student = {}
    print("enter  details of student ")
    for i in range(zo):
        k = input("enter subject name")
        val = int(input("enter marks"))
        student[k] = val
    return student     
for i in range(no):
    ke = input("enter name of the student")
    key.append(ke)  
current = {}    
for name in key:
    b = loki()
    current[name] = b
l = input("enter the student name u want to cheak marks of")
m = input("enter the subject name u want to cheak marks of")   
print(current[l][m])