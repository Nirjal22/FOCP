import getpass #importing getpass module 

def read_user_data(): #to read the user data
    with open("passwd.txt", "r") as file: #read mode
        lines = file.readlines() #reads the entire file
        return [line.strip().split(":") for line in lines]

def check_login(user_name, password_enter, user_data): 
    for sublist in user_data:
        saved_user_name = sublist[0] #checking the values
        saved_password = sublist[-1]
        if user_name == saved_user_name and password_enter == saved_password: #if it matches the values, below line of code will be excuted
            return True
    return False #if not then this code will excute
#getting user input
user_name = input("User: ")
password_enter = getpass.getpass("Password: ") #getpass is used to make the password invisible 
user_data = read_user_data() #calling the function and assigining to the variable
#if-else condition
if check_login(user_name, password_enter, user_data): #if True this will excute
    print("Access granted.")
else:
    print("Access denied. ") #if not then this will excute
