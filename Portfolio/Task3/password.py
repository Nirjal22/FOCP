import getpass #importing getpass module

def read_user_data(): #to read the file
    with open("passwd.txt", "r") as file: #read mode
        lines = file.readlines() #reads the entire lines
        return [line.strip().split(":") for line in lines]

def write_user_data(user_data): #to write in the file
    with open("passwd.txt", "w") as file: #write mode
        for user_info in user_data:
            file.write(":".join(user_info) + "\n") #join() function will joins the string using the ':' and prints on the new-line.

def check_login(user_name, password_enter, user_data): #checking if the user and password matches and exists or not
    for sublist in user_data: #for-loop
        saved_user_name = sublist[0] #checking
        saved_password = sublist[-1]
        if user_name == saved_user_name and password_enter == saved_password: #if the values matches, below code will excute
            return True
    return False #if not this will excute

def change_password(user_data, user_name): #to change the password
    for sublist in user_data:
        if user_name == sublist[0]: #if user-name matched this code below will run
            new_password = getpass.getpass("New password: ")
            checking_again = getpass.getpass("Confirm: ")
            
            if new_password == checking_again: #to check if the new entered password matches the confirmation password or not
                sublist[-1] = new_password
                write_user_data(user_data)
                print("Password changed successfully.")
            else: #if didn't match, below code will excute
                print("Password didn't match")
            return
# Taking user input
user_name = input("User: ")
password_enter = getpass.getpass("Current Password: ")
user_data = read_user_data() #calling the function and assigining to the variable
#if-condition
if check_login(user_name, password_enter, user_data):
    change_password(user_data, user_name) #calling the function
else: 
    print("Login failed")
