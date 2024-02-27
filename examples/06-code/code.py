# import the datetime to show current date and time
import datetime

def my_function(x):
    """ purpose of this function is to increase given parameter by one 
    
    Parameters
    ---------
    x: int
        a numeric value that will be increased by one

    returns
    ----
    int
        increases parameter 'x' by one and returns result from the functions

    """

    return x + 1

# print current date and time
print(datetime.datetime.now())

# declare variable 'name' and assign some text into it
name = "ankita"


# print contents of variable 'name'
print(name)

# call the function
value = my_function(100)
print(value)