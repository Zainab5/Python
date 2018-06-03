def add(num1, num2):
    """"Returns a value"""
    return num1 + num2


def sub(num1, num2):
    return num1-num2


def multiply(num1,num2):
    return num1*num2


def divide(num1, num2):
    return num1/num2

def main():
    num1= int(input("Enter number 1"))
    num2= int(input("Enter number 2"))
    operation = int(input("What do you want to do? 1.Add 2.Subtract 3.Multiply 4. Divide.  Enter your choice: "))
    if(operation==1):
         addVar = add(num1, num2)
         print("The result after adding", num1, "and", num2, "is:")
         print(addVar)
    elif(operation==2):
         subVar = sub(num1, num2)
         print("The result after subtracting", num1, "and", num2, "is:")
         print(subVar)
    elif(operation==3):
         multVar = multiply(num1, num2)
         print("The result after multiplying", num1, "and", num2, "is:")
         print(multVar)
    elif(operation==4):
        diviVar = divide(num1, num2)
        print("The result after dividing", num1, "and", num2, "is:")
        print(diviVar)
    else:
        print("Enter a valid value")








main()



