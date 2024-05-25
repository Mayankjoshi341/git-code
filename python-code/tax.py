#tax calculater 
def tax(income):
 income = float(input("Enter your income : "))
 if(income <300000):
    print("You don't have to pay any tax earn more.")
 elif(income>=300000 and income<=600000):
    low_income = str((income*5)/100)
    print("You have to pay 5% of your income. Which is "+low_income)
 elif(income>=600000 and income<=900000):
    mid_income = str((income*10)/100)
    print("You have to pay 10% of your income. Which is "+mid_income)
 elif(income>=900000 and income<=1200000):
    mid2_income = str((income*15)/100)
    print("You have to pay 15% of your income. Which is "+mid2_income)
 elif(income>=1200000 and income<=1500000):
    high_income = str((income*20)/100)
    print("You have to pay 20% of your income. Which is "+high_income)
 else:
    high2_income = str((income*30)/100)
    print("You have to pay 30% of your income. Which is "+high2_income)
 print("press 1 for exit and press any key to continue")
 con = int(input("==>"))
 if con == 1 :
    return exit()
while True:
   tax(input)