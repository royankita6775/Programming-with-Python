age = int(input("Insert your age: "))

if age < 13:
    print("Child")

elif 12 < age < 20:
    print("Teen")

elif 19 < age < 66:
    print("Adult")   
     
else:
    print("Senior")