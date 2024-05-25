import time  #import time library
def main(opertion):   # main funtion which perform opertion
    if opertion == 1:
        print("")
        print("<-- ENTER THE TASK -->")#for adding a element to the list
        print("")
        add = input("==> ").split()
        task.append(add)
        print("")
        print("Task added ")
        msg() #recalling funtion                               
    elif opertion == 2:
        print("")
        print("<-- ENTER THE TASK TO REMOVE -->") #for removing a element form the list
        rmv = input("==> ")
        print("")
        for t in task:
            if rmv in t:
             task.remove(t)
             print("Task removed ")
             break
        else :
            print("Task is not found")
        msg()
        
    elif opertion == 3:
        print("")
        print("<-- DISPLAYING THE TASKS -->")  #Display the element in the list
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Your tasks is ",task)
        msg()

    elif opertion== 4:
        print("")
        count = len(task)
        print("No. of task is ",count) #to count no. of tasks
        msg()
    elif opertion == 5:
        print("")
        print("<-- CLEARING THE TASKS -->")
        task.clear
        time.sleep(2)
        print("Task cleared!!")
        msg()
    elif opertion == 6:
        print("")
        print("see you soon")
        return 2 #exit the program
task = []
def msg():
    print("<-- ENTER THE OPERTION -->")
    print("1 for enter task")
    print("2 for remove task")
    print("3 for display tasks")
    print("4 for no. of tasks")
    print("5 for clear all tasks")
    print("6 for exit")
    opertion = int(input("==> ") )   
    main(opertion)
while True:
    msg()
