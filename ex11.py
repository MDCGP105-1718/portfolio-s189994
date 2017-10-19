from random import randint
x = randint (1,50)# the number you are searching for
guess = 0
count=0
def guessing(guess,count):
    """
    Take a guess!
    It will count how many times you guessed!
    Just try!

    """

while guess !=x :
    guess =int(input("Take a guess: "))
    count+=1
    if guess > x:
        print("The number is lower!")
    elif guess < x:
        print ("The number is higher!")
    if guess == x:
        print (" Good job! You did it!")
        print (f"You guessed it in {count} times!")

guessing(guess,count)
