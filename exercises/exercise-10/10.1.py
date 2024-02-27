from os import linesep
import pickle

lname = input("Please enter your last name: ")
filename = "file_names.txt"

with open(filename, "a+") as write_names:
    write_names.write(lname)
    write_names.write("\n")
try:
    with open ("file_names.txt", "r") as read_name:
       read_file=read_name.readlines()
       
except Exception:
    print("there are no such a file", filename)
for line in read_file:
    print(line)

