x = 0
y = 0

def FizzBuzz (x,y):
    """
    Insert the range you want to search:
    Return FizzBuzz
    """
x=int(input("Minimum value"))
y=int(input("Maximum value"))

for a in range (x,y+1):
    if (a % 3 == 0) and (a%5 == 0):
        print ("FizzBuzz")
    elif a % 3 == 0:
        print ("Fizz")
    elif a % 5 == 0:
        print ("Buzz")
        
    else: print(a)

FizzBuzz:(x,y)
