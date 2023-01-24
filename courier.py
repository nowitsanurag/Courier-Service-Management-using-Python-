import pickle
import os

def addItem():
    itemno = int(input("Enter the unique item no : "))
    tid = input("Enter the tracking id : ")
    desc = input("Enter the product description : ")
    wt = input("Enter the weight of the Courier : ")
    dadr = input("Enter the destination address : ")
    sadr = input("Enter the sender address : ")
    status = "Packed"
    cost = int(input("Enter the cost of Shipping : "))

    cdata = [itemno,tid,desc,wt,dadr,sadr,status,cost]
    f = open("courier.dat","ab")

    pickle.dump(cdata,f)

    print("Details Added Successfully ")
    f.close()

def display():
    f = open("courier.dat","rb")
    try:
        while True:
            cdata = pickle.load(f)
            print(cdata[2] + " weights " + str(cdata[3]) + " will be delivered to " + cdata[4])
    except:
        f.close()
        print("-" * 40)
        
def search():
    td = input("Enter tracking id to be searched : ")
    found = False
    f = open("courier.dat","rb")
    try:
        while True:
            cdata = pickle.load(f)
            if cdata[1] == td:
                print("Found, Here are the details ")
                found = True
                print(cdata[2] + " weights " + str(cdata[3]) + " will be delivered to " + cdata[4])
                break
    except:
        if found == False:
            print("No Courier Found with Such a Tracking Id ")
        f.close()
        print("-" * 40)

def remove():
    td = input("Enter tracking id to be removed : ")
    found = False
    f = open("courier.dat","rb")
    g = open("temp.dat","wb")
    try:
        while True:
            cdata = pickle.load(f)
            if cdata[1] == td:
                print("Found, Here are the details ")
                found = True
                print(cdata[2] + " weights " + str(cdata[3]) + " will be delivered to " + cdata[4])
            else:
                pickle.dump(cdata,g)
    except:
        if found == False:
            print("No Courier Found with Such a Tracking Id ")
        else:
            print("Courier Deleted Successfully")
        f.close()
        g.close()
        print("-" * 40)
        os.remove("courier.dat")
        os.rename("temp.dat","courier.dat")

"""login() allows a user to either login as an admin or as a member. If the user chooses to login as an admin, they are prompted to enter a password. If the password is correct, the user is then prompted to enter a new user name and password, which are then stored in a file called "users.dat" using the pickle module. If the user chooses to login as a member, they are prompted to enter their user name and password. The function then searches the "users.dat" file for a matching user name and password and grants access if a match is found. If no match is found, the function displays an error message. The function returns a boolean value indicating whether the login was successful or not."""

def login():
    print("^" * 50)
    print("\t ABC Courier Services ")
    print("^" * 50)
    print("Press 1 - Login as Admin")
    print("Press 2 - Login as Member ")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        password = input("Enter password ")
        if password == "1221":
            usrname = input("Enter the New User name : ")
            pwd = input("Enter the new Password : ")
            f = open("users.dat","ab")
            pickle.dump([usrname,pwd],f)
            f.close()
            print("^" * 50)
            print("User Added Successfully ")
            print("^" * 50)
    elif ch == 2:
        usrname = input("Enter the User name : ")
        pwd = input("Enter the Password : ")
        f = open("users.dat","rb")
        found = False
        try:
            while True:
                d = pickle.load(f)
                if d[0] == usrname and d[1] == pwd:
                    print("Access Granted ")
                    found = True
                    break
        except:
            if found == False:
                print("Invalid User Name or Password ")
            f.close()
        return found


if login():
    
    while True:
        print("-" * 30)
        print("Press 1 - Add New Product")
        print("Press 2 - Display All Couriered Products")
        print("Press 3 - Search a Courier")
        print("Press 4 - Delete a Courier")
        # print("Press 5 - Change Courier Status")
        # print("Press 6 - Display all UnDelivered")
        print("Press 5 - Exit")
        ch = int(input("Enter your choice : "))
        if ch == 1:
            addItem()
        elif ch == 2:
            display()
        elif ch == 3:
            search()
        elif ch == 4:
            remove()
        elif ch == 5:
            break