#------------------------------------------------ L I B R A R Y   S E C T I O N ------------------------------------------------

from prettytable import PrettyTable 
from datetime import datetime, timedelta
import os
import time

#--------------------------------------- U S E R  -  D E F I N E D   F U N C T I O N S -----------------------------------------

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')


def calculateDueDate(daysToAdd):
    currentDate = datetime.now()
    dueDate = currentDate + timedelta(days=daysToAdd)
    return dueDate


def addTask(task, dueDate):
    table.add_row([len(table._rows)+1,task,"Pending",calculateDueDate(dueDate)])
    print("Task has been added successfully.")


def removeTask(id):
        for i,row in enumerate(table):
            if(i>id-1):
                table._rows[i][0] -= 1
        del table._rows[id-1]
        print("\nTask has been removed successfully.")
        

def completeTask(id):
    table._rows[id-1][2] = "Completed"
    print("\nTask has been completed successfully.")

    
#------------------------------------------------ P R O G R A M   S E C T I O N ------------------------------------------------

table = PrettyTable()
table.field_names = ["ID","Tasks","Status","Due Date"]
choice = int()
task = ""
daysToaAdd = int()

clear_screen()


while(True):
    print("\n\t- W E L C O M E   T O   T H E   T O - D O  L I S T   A P P - \n")
    if len(table._rows)>0:
       print(table)
    else:
        print("\nNo tasks in the list. Take a break and enjoy your day!")

    print("\n1. Add Task\n2. Complete Task\n3. Remove Task\n4. Exit")
    choice = int(input("\nEnter the Desired Option : "))

    if(choice==1):
        print("\n\t\t- A D D   T A S K - ")
        task = input("\nEnter the Task : ")
        daysToAdd = int(input("Enter the Days for the task : "))
        addTask(task, daysToAdd)

    elif(choice==2):
        print("\n\t\t- C O M P L E T E   T A S K - ")
        id = int(input("\nEnter the ID of the task : "))
        completeTask(id)

    elif(choice==3):
        print("\n\t\t- R E M O V E   T A S K - ")
        id = int(input("\nEnter the ID of the task : "))
        removeTask(id)

    elif(choice==4):
        clear_screen()
        print("Exiting.")
        exit()

    else:
        print("\nInvalid Input. Please enter the valid input.")
    time.sleep(4)
    clear_screen()
