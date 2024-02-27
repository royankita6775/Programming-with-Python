mylist = []
filename1 = "Int.txt"
filename2 = "Float.txt"
t = True
f = True
while t:
    number1 = (input("Enter first Number: "))
    try:
        number1 = int(number1)    
        t = False
    except ValueError:
        t = True
    try:
        number1 = float(number1)  
        t = False
   
    except ValueError:
        t = True

while f:
    number2 = (input("Enter second Number: "))
    try:  
        number2 = int(number2)
        f = False
    except ValueError:
        f = True
    try:
        number2 = float(number2)
        f = False
    except ValueError:
        t = True
        
        

mylist.append(number1)
mylist.append(number2)
for i in mylist :
        if i == int(i):
            newstr = str(i)
            with open (filename1, "a+") as nf1:
                nf1.write(str(number1))
                nf1.write("\n")
        elif i == float(i):
            with open (filename2, "a+") as nf2:
                nf2.write(str(number2))
                nf2.write("\n")
try:    
    with open(filename1, 'r') as f1:
       f12 = f1.readlines()   
       for line in f12:
           print("The Integer Numbers are : ", line)
except Exception:
        print("there are no such a file", filename1,"", filename1)
try:    
    with open(filename2,'r') as f1:
       f11 = f1.readlines()   
       for line1 in f11:
           print("The float Numbers are : ", filename2,"", line1)
except Exception:
        print("there are no such a file", filename2)
