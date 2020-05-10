new = []
finished = []
class To_do_list:
    def __init__(self):
        new = []
        finished = []
#---------------------------------------------------------------------------------------------------------------------------        
    def newlist(self):
        rod = input("you canenter one task at a time")
        new.append(rod)    
        print("total number of task",len(new))
        return new
#---------------------------------------------------------------------------------------------------------------------------    
    def mark_done(self,d):
        q = int(input("enter the index of the task u wish to complete"))
        value = d.pop(q)
        finished.append(value)
        print("total task completed",len(finished))
        return
#----------------------------------------------------------------------------------------------------------------------------   
    def see_task(self,finished,d):   
        print("completed task")    
        for ct,ee in enumerate(finished,1): 
            print(ct,ee) 
        print("uncompleted task")      
        for countt,eel in enumerate(new,1): 
            print(countt,eel) 
        return          
obj = To_do_list()
def main():
    a=0
    while a<4:
        a = int(input("enter the option\n1.enter what to-do\n2.complete the task\n3. view all the thing u have to do\n4.exit\n"))
        if a==1:
            d = obj.newlist()
        elif a==2:
            obj.mark_done(d)
        elif a==3:
            obj.see_task(finished,d)
        elif a==4:
            exit()        
main()            