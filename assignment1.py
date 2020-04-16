key = []
value = []
student = {}
print("enter student details")
for i in range(0,3):
	ke = input("enter usn")
	key.append(ke)
	val = input("enter name")
	value.append(val)	
	
student = {key[0] : value[0],key[1] : value[1],key[2] : value[2] }

for key, value in student.items():
    print(key, ' : ', value)
