# 6.1

def convert():
    seconds = int(input("Please enter seconds:"))
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(hour,":", minutes,":", seconds)
    
    
convert()
