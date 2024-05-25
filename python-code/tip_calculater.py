#this is an tip calculater by mayank 
bill = float(input("Enter how much the bill is : "))
tip = float(input("Enter the tip persent(%) : "))
person = int(input("Enter the no of persons : "))
TIP = (bill*tip)/100
if (person>=2):
     TIP = TIP/person
     TIP = str(TIP)
     print("The tip is "+TIP)
else:
 TIP = str(TIP)
 print("The tip is "+TIP)

total = float(TIP) + bill
print("The total amount is : ",total)