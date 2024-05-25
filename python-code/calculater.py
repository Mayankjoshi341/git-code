def add(num1, num2):
    sum = num1 + num2 
    print("the answer is " , sum)
    return sum
def subtract(num1, num2):
    sub = num1 - num2
    print("the answer is " , sub)
    return sub
def multiply(num1, num2):
    multi = num1 * num2
    print("the answer is " , multi)
    return multi
def divide(num1, num2):
    div = num1 / num2
    print("the answer is " , div)
    return div
def pow(num1, num2):
    pow = num1 ** num2
    print("the answer is " , pow)
    return pow

def sqrt(num1, num2):
    sqrt = num1 ** (1/num2)
    print("the answer is " , sqrt)
    return sqrt

def reminder(num1, num2):
    rem = num1 % num2
    print("the answer is " , rem)
    return rem

def factorial(num1, num2):
    fact = 1
    for i in range(1, num1 + 1):
        fact = fact * i
    print("the answer is " , fact)
    return fact
def multipal_operation():
    print("enter the operations")
    print("")

def mag():
    print("enter the first number")
    num1 = int(input("==> "))
    print("enter the second number")
    num2 = int(input("==> "))
    print("if you want to perfrom multiple operations then press 1")
    mul_op = int(input(""))
    return mul_op , num1, num2
def calculater(mul_op):
    print("<==WELCOME TO MY CALCULATOR==>")
    print('')
    mag()
    if mul_op == 1:      
    print("SELECT BELOW OPERTION TO PERFORM")
    print("Press 1 for addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    print("Press 5 for power")
    print("Press 6 for square root")
    print("Press 7 for reminder")
    print("Press 8 for factorial")
    print("Press 10 to perform multipal operation")
    print("Press 9 for exit")
    
    print("")
    opertion = int(input("==> "))
    match (opertion):
        case 1:
            add(num1, num2)
        case 2:
            subtract(num1, num2)
        case 3:
            multiply(num1, num2)
        case 4:
            divide(num1, num2)
        case 5:
            pow(num1, num2)
        case 6:
            sqrt(num1, num2)
        case 7:
            reminder(num1, num2)
        case 8:
            factorial(num1, num2)
        case 9:
            exit()
        case _:
            print("invalid opertion")   

while True:
    calculater()

