number = 5
accountbalance = 110.54
print(number)
print(accountbalance)

number = 55
number2 = number + 2
# value of number2 is now 57
print("number2 is", number2)

#print("number2 is" + str(number2))

number = number * number2
print("number2 is", number)

number += 10
number = number + 10
print("number is", number)

print("type of variable number is", type(number))
print("type of variable accountbalance is", type(accountbalance))


# strings
# initialize a string from text
name = "Ankita"
lastName = "Roy"

# initialize string from another variable
fullNmae = name

# add strings
fullNmae = name + " " + lastName
print(fullNmae)

# use Format function
age = 21
fullNmae = "First name: {}. Last name: {}. Age: {}".format(name, lastName, age)
print(fullNmae)

fullNmae = "First name: " + name + ". Last name: " + lastName + ". Age: " + str(age)
print(fullNmae)

# access characters in a string
text = "ABC"
a = text[0]
b = text[1]
c = text[2]
print("Second char is " + b)   # or, "print(f"Second char is {b}")"

print("Text length is " + str(len(text)) + " characters.")


# compare strings
text2 = "ABD"
if text == text2:
    print("Texts are identical.")
else:
    print("Texts are different.")


# read text from console
line = input("Enter a line of text: ")
print("You entered: " + line)

line = input("Enter a number: ")
number = int(line)
print("Number is ", number)