def division(x,y):
    if y!=0:
        return x/y
    
    else:
        print("enter the denominator greater than 0 or less than 0.")
def multiplication(x,y):
    return x*y
        
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y



while True:
    num1=float(input("Enter the first number"))
    num2=float(input("Enter the second number"))
    
    print("select the operation that you want:\n")
    print("choice 1: Division\n")
    print("choice 2: Multiplication\n")
    print("choice 3: Addiction\n")
    print("choice 4: Substraction\n")
    print("choice 5: Exit\n\n")
    
    choice=input("Enter the choice:")
    
    if choice=='5':
        print("Exiting from the program.")
        break
    
    if choice not in ("1","2","3","4","5"):
        print("Enter the valid choice between 1 to 5")
        continue
    if choice=="1":
        print("The division of",num1,"/",num2,"is :",division(num1,num2))
        
    elif choice=="2":
        print("The multiplication of",num1,"*",num2,"is :",multiplication(num1,num2))
        
    elif choice=="3":
        print("The addition of",num1,"+",num2,"is :",add(num1,num2))
        
    elif choice=="4":
        print("The substraction of",num1,"-",num2,"is :",subtract(num1,num2))
           
    else:
        print("Enter the valid choice") 