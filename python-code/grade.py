#first make the two match case for grade to number and  vice varsa
#for that i first have to make one funtion and call in case 1 or 2 +
import time 

def select():
 print("<-- SELECT THE MODE -->")
 print("Press 1 for number to grade ")
 print("Press 2 for grade to number ")
 sm = int(input("==> "))
 match sm:
   case 1:
       print("<== WELCOME TO THE NUMBER TO GRADE CONVERTER ==>")
       time.sleep(1)
       g_to_n()
   case 2: 
       print("<== WELCOME TO THE GRADE TO NUMBER CONVERTER ==>")
       time.sleep(1)
       n_to_g()
def g_to_n ():# funtion to perform grade to number
    print("<-- NUMBER TO GRADE -->")
    print("Enter the number:")
    num = int(input("==>"))
    if num >=91 and num <=100:
        print("A+")
    elif num >=81 and num <=90:
       print("A")
    elif num >=71 and num <=80:
       print("B+")
    elif num >=61 and num <=70:
       print("B")
    elif num >=51 and num <=60:
       print("C+")
    elif num >=41 and num <=50:
       print("D")
    elif num >=31 and num <=0:
       print("Fail")
    else:
       time.sleep(1)
       g_to_n()
    
def n_to_g():
   print("<-- ENTER THE GRADE -->") 
   grade_set= {
      'A+' : (100 , 91),
      'A' : (90 , 81),
      'B+' : (80 , 71),
      'B' : (70 , 61),
      '+C' : (60 , 51),
      'C' : (50 , 41),
      'D' : (40 , 31),
      'F' : "FAIL"
   }
   time.sleep(1)
   grade = input("==>")
   res = grade_set.get(grade.upper())
   if res:
        if grade == 'F':
            print("Your number is:", res)
        else:
            print("Your number is between:", res[1], "and", res[0])
   else:
        print("Invalid grade")
while True:
 select()