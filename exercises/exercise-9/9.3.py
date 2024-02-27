# The function raises error when called by a different datatype and says that (could not convert string to float: 'a'), 
# it is because the function can only be called when the parameter is number

def isthiszero(num): 
    try: 
        if num == 0 :
            return True
        elif (num == float(num) or num == int(num)) and num != 0:
            return False
    except TypeError:
        return ("Wrong input")
def main():
    print(isthiszero(5))
    print(isthiszero(0.52))
    print(isthiszero('salla'))
    print(isthiszero('a'))
    print(isthiszero(7.00))
   
    
if __name__ == "__main__":
    main()
