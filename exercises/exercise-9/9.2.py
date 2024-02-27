# 9.2

import os

path = '/Users/Ankita Roy/'

try:
    files = os.listdir(path)
    for f in files:
        print(f)
except:
    print("Failed to read file")

filename = "ayho.txt"
try:
    file = open("C:\\" + filename, "w")
    file.write("Add file to root")
    file.close()

except:
    print("Failed to create file to root")
    
# I would need admin permission to make changes to root
# Or we can add the permission to write and excute by the user 
# sudo chmod u+w /root/

