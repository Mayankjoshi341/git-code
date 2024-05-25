import time #importing time library

'''This is the main function which take the input from the user.
 The input then displayed on the screen and retruns the final result.'''
def main():
    print("<=- welcome to date to day finder -=>")
    print("Enter the following")
    print("Enter the date ")
    date = int(input("==> "))
    print("Enter the month")
    month = int(input("==> "))
    print("Enter the year")
    year = str(input("==> "))
    print("processing...")
    print("you enterd " + str(date) + "/" + str(month) + "/" + str(year)) # dispaly the input
    time.sleep(0.5)
    print("....")
    time.sleep(0.5)
    s1 = int(year[2:])
    s2 = s1//4 
    m = {1:0, 2:3 , 3:3 , 4:6 , 5:1 , 6:4 , 7:6 , 8:2 , 9:5 , 10:0 , 11:3, 12:5}
    monthcode =(m[month])
    s3 = date+monthcode
    year = int(year)
    if year >=1600 and year<=1699:
        year = 6
    elif year >=1700 and year<=1799:   #The functing of this code block is to do main calculation of the date to day finder 
        year = 4                       #and return the main result of the calculation to the next function.
    elif year >=1800 and year<=1899:
        year = 2
    elif year >=1900 and year<=1999:
        year = 0
    elif year >=2000 and year<=2099:
        year = 6
    s4 = int(s1+s2+s3+year)
    final = s4%7
    time.sleep(1.5)
    day = {0: "The day is sunday!", 1: "The day is monday!",
            2: "The day is tuesday!", 3: "The day is wednesday!",
              4: "The day is thursday!", 5: "The day is friday!",
                6:"The day is saturday!"}
    print(day[final])
    print("<=- thanks for visiting -=>")
    print("")
    print("")
    time.sleep(5)
    print("Press 1 to continue or press 2 to exit.")
    con = int(input("==>"))
    if con == 2 :
      return exit()
while True:
    main()