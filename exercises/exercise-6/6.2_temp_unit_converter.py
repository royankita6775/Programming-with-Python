# 6.2

def celToFah():
    cel = float(input("Please enter temperature in celsius to convert into fahrenheit: "))
    fah = (cel*1.8) + 32
    print("%.1f" %fah)
    
celToFah()

def fahToCel():
    fah = float(input("Please enter temperature in fahrenheit to convert into celsius: "))
    cel = (fah-32) / 1.8
    print("%.1f" %cel)
    
fahToCel()