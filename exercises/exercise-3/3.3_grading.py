points = int(input("Insert your points: "))
if points == 0 or points == 1:
    print("Grade: 0")
    
elif 1 < points < 4:
    print("Grade: 1")
    
elif 3 < points < 6:
    print("Grade: 2")
    
elif 5 < points < 8:
    print("Grade: 3")
    
elif 7 < points < 10:
    print("Grade: 4")
    
elif 9 < points or points == 12:
    print("Grade: 5")
    
else:
    print("Invalid input")
