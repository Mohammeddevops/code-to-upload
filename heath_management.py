import datetime
def getdate():
    return datetime.datetime.now()
# print(getdate())        

def take(k):
    if k==1:
        c=int(input("enter 1 for exercise and 2 for food "))
        if c==1:
            value=input("type here \n")
            with open("harryex.txt","a") as op:
                op.write(str([str(getdate())])+":"+value+"\n")
            print("successfull written")    
        elif c==2:
            value=input("type here \n")
            with open("harryfood.txt","a") as op:
                op.write(str([str(getdate())])+":"+value+"\n")
            print("successfull written")
    elif k==2:            
        c=int(input("enter 1 for exercise and 2 for food "))
        if c==1:
            value=input("type here \n")
            with open("rohanex.txt","a") as op:
                op.write(str([str(getdate())])+":"+value+"\n")
            print("successfull written")    
        elif c==2:
            value=input("type here \n")
            with open("rohanfood.txt","a") as op:
                op.write(str([str(getdate())])+":"+value+"\n")
            print("successfull written")
    elif k==3:            
        c=int(input("enter 1 for exercise and 2 for food "))
        if c==1:
            value=input("type here \n")
            with open("hammadex.txt","a") as op:
                op.write(str([str(getdate())])+":"+value+"\n")
            print("successfull written")    
        elif c==2:
            value=input("type here \n")
            with open("hammadfood.txt","a") as op:
                op.write(str([str(getdate())])+":"+value+"\n")
            print("successfull written")
    else:
        print("please enter the valid input 1for harry 2for rohan 3for hammad")

def retrive(k):
    if k==1:
        c=int(input("enter 1 for exercise and 2 for food "))
        if c==1:
            with open("harryex.txt") as op:
                for i in op:
                    print(i,end="")
                    
        elif c==2:
            with open("harryfood.txt") as op:
                for i in op:
                    print(i,end="")
                    
    elif k==2:
        c=int(input("enter 1 for exercise and 2 for food "))
        if c==1:
            with open("rohanex.txt") as op:
                for i in op:
                    print(i,end="")
                    
        elif c==2:
            with open("rohanfood.txt") as op:
                for i in op:
                    print(i,end="")
                    
    elif k==3:
        c=int(input("enter 1 for exercise and 2 for food "))
        if c==1:
            with open("hammadex.txt") as op:
                for i in op:
                    print(i,end="")
                    
        elif c==2:
            with open("hammadfood.txt") as op:
                for i in op:
                    print(i,end="")
    else:                
        print("please enter the valid input 1for harry 2for rohan 3for hammad")
                    
a=int(input("enter 1 to lock and 2 for retriive"))
if a==1:
    b=int(input("enter 1 for harry 2 for rohan and 3 for hammad "))
    take(b)
else:
    b=int(input("enter 1 for harry 2 for rohan and 3for hammad "))
    retrive(b) 