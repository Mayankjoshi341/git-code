import time
def add(num1, num2):
    sum = num1 + num2 
    print(f"The answer of {num1}+{num2} is :" , sum)
    return sum
def subtract(num1, num2):
    sub = num1 - num2
    print(f"The answer of {num1}-{num2} is :" , sub)
    return sub
def multiply(num1, num2):
    multi = num1 * num2
    print(f"The answer of {num1}*{num2} is " , multi)
    return multi
def divide(num1, num2):
    div = num1 / num2
    print(f"The answer of {num1}/{num2} is " , div)
    return div
def pow(num1, num2):
    pow = num1 ** num2
    print(f"The answer of {num1}^{num2} is " , pow)
    return pow
def sqrt(num1, num2):
    sqrt = num1 ** (1/num2)
    print("the answer is " , sqrt)
    return sqrt
def reminder(num1, num2):
    rem = num1 % num2
    print("the answer is " , rem)
    return rem
def factorial(num1):
    fact = 1
    for i in range(1, num1 + 1):
        fact = fact * i
    print(f"the answer of {num1}! is " , fact)
    return fact

"""================================================================================="""

def calculate():
    print("")
    print("")
    print("Welcome please select the calculator according to your use.")
    print("")
    print("press 1 for simple calculation like : add , sub , multi , div")
    print("press 2 for intermidate calculation like : sq , cube , sqroot , factoral , ")
    print("press 3 for exit calculater")
    cal_inter = int(input("==> "))
    match cal_inter:
        case 1:
            print("welcome please enter the numbers")
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            print("now enter the operation")
            op = input("==> ")
            print("The entered is :" + str(num1) +"" + op + "" + str(num2))
            time.sleep(1)
            match op:
                case "+":
                    add(num1, num2)
                case "-":
                    subtract(num1,num2)
                case "*":
                    multiply(num1 , num2)
                case "/":
                    divide(num1,num2)

        case 2:
            print("welcome please enter the opertion.")
            print("""
                  Enter 1 for power
                  Enter 2 for square root  
                  Entre 3 for remainder 
                  Enter 4 for factorization
                             """)
            op = int(input("==>"))
            time.sleep(1)
            match op:
                case 1 :
                    print("Enter the number")
                    num1 = int(input("==>"))
                    print("Enter the power")
                    num2 = int(input("==>"))
                    pow(num1,num2)
                case 2 :
                    print("Enter the first number")
                    num1 = int(input("==>"))
                    print("Enter the second number")
                    num2 = int(input("==>"))
                    sqrt(num1,num2)
                case 3 :
                    print("Enter the first number")
                    num1 = int(input("==>"))
                    print("Enter the second power")
                    num2 = int(input("==>"))
                    reminder(num1,num2)
                case 4:
                    print("Enter the number for factorization")
                    num1 = int(input("==>"))
                    factorial(num1)
        case 3:
            print("Thank you for using our calculater.")
            time.sleep(1)
            exit()    
                    
               


while True:
    calculate()




