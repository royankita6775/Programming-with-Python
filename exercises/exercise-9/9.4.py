list = ['a','b','c','d','e']
t = True
count = 0

for i in list:
    count += 1
while t :
    try:
        replace_index=int(input("Enter index location: ")) 
        if replace_index in range(count):
            t = False
        else:
            print("Wrong index! Please try again")
    except Exception:
            t = True     

new_text = input("Enter your new text:")  
list[replace_index] = new_text
print(*list)
