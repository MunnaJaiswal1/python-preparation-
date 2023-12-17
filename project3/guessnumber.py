#guess the number
import random

def guess(): 
 print("Here the system will generate the random number between 1 and 100")
 generate=random.randint(1,100)
 attempts=0
 print("the system numberr is:",generate)
 
 while True:
     
    user=int(input("Enter the number:"))
    attempts+=1
        
    if user==generate:
        print("congratulation!!! Your number match with system")
        break
        
    elif user<generate:
        print("Your guess number is smaller than system number")
        attempts+=1
        continue
    
    elif user>generate:
        print("Your number is greater than the system number")
        attempts+=1
        continue
    else:
        print("Invalid input try to input between 1 and 100")


guess()
