import os

#   Saves/Adds data to datafile
def savedata(name, ip):
    f = open("datafile.txt", "at")
    f.write(name + "---" + ip + "," + "\n")
    f.close()

#   Loads data from datafile
def loaddata():    
    i = 0
    with open("datafile.txt", "rt") as file:
        for line in file:
            i = i + 1
            num = str(i)
            print (num + ".) " + line.strip())

#   Edit data
def editData(dataIndex, dataNameEdit, dataIPEdit):

    with open('dataFile.txt', 'rt') as f:
        #   Gets data into list
        data = f.readlines()

            
    dataIndex = int(dataIndex) - 1
    data[dataIndex] = f'{dataNameEdit}---{dataIPEdit},\n'


    #  Edits data on given index
    try:
        #   Writes everything back to file
        with open('dataFile.txt', 'wt') as f:
            f.writelines(data)
        
        print(f"<< Updated friend number: {dataIndex + 1} >>")

    except:
        print("<< Error Could not edit file >>")



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#   This while loop is here temp
while True:
    print("<< 1. AddFriend >>")
    print("<< 2. LoadFriends >>")
    print("<< 3. EditFriend >>")
    print("<< 4. RemoveFriend >>")
    print("<< 5. Quit >>")
    print("-------------------------------")

    userInput = input()
    userInput.lower()

    #   Option 1. AddFriend if statement
    if userInput == "addfriend" or userInput == "1":
        clearConsole()
        while True:
            print("<< Please input friends name >>")
            usernNameInput = input()

            print("<< Please enter friends IP adress >>")
            userIPInput = input()

            if len(usernNameInput) and len(userIPInput):
                try:
                    savedata(usernNameInput, userIPInput)
                    clearConsole()
                    print("<< DATA SAVED SUCCESSFULLY >>")
                    print("<< Returning to main menu... >>")
                    print("-------------------------------")
                    break

                except:
                    print("<< AN ERROR HAS OCCURED PLEASE TRY AGAIN >>")
            
            else:
                print("<< ERROR MISSING INPUT! PLEASE TRY AGAIN >>")

    #   Option 2. LoadFriends
    elif userInput == "loadfriends" or userInput == "2":
        clearConsole()
        try:
            print("<< Data >>")
            loaddata()
            print("-------------------------------")
            print("<< Type Anything to return to main menu >>")
            input()
            clearConsole()

        except: 
            print("<< ERROR NO DATA WAS FOUND >>")
            print("<< RETURN TO MAIN MENU >>")
            print("-------------------------------")

    #   Option 3. EditFriend
    elif userInput == "3" or userInput == "editfriend":
        clearConsole()
        print("<< Please Enter index of friend you wish to edit >>")
        loaddata()
        print("<< Type 'quit' if you wish to chancel")
        indexInput = input()
        if indexInput == "quit":
            break
            
        clearConsole()
        print("<< Please enter name >>")
        nameInput = input()

        clearConsole()
        print("<< Please enter ip >>")
        ipInput = input()

        clearConsole
        editData(indexInput, nameInput, ipInput)




                
              

    #   Option 4. RemoveFriend
    elif userInput == "4" or userInput == "removefriend":
        while True:
            print("<< Please enter user index... >>")
            userIndexInput = input
            break

    #   Quit App
    elif userInput == "quit" or userInput == "5":
        clearConsole()
        quit()

    #   Command Error
    else:
        clearConsole()
        print(f"<< ERROR: {userInput} COMMAND NOT VALID >>")