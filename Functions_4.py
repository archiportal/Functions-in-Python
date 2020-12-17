def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def expo(a, b):
    return a**b


while True:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))

    print("1.Add\t2.Substract\t3.Multiply\n4.Divide\t5.Exponent\t6.Exit")
    p = int(input("Enter choice:"))

    if(p == 1):
        print("Sum is: ", add(num1, num2))
    elif(p == 2):
        print("Difference is: ", sub(num1, num2))
    elif(p == 3):
        print("Product is: ", mul(num1, num2))
    elif(p == 4):
        print("Quotient is: ", div(num1, num2))
    elif(p == 5):
        print("Answer: ", expo(num1, num2))
    elif(p == 6):
        break
    else:
        print("Wrong input.")