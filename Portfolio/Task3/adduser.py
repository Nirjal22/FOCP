def read_user_data(): #creating fuction to read the file
    with open("passwd.txt", "r") as file: #read method 
        lines = file.readlines() #reads the entire file 
        return [line.strip().split(":") for line in lines] 
    
def check_login(user_name): #to check if the user is already created or not.
    for sublist in user_data1:
        saved_user_name = sublist[0]
        if user_name == saved_user_name:
            return True  # Return True if the username is found
    return False  # Return False if the username is not found in any sublist
        
def adduser(user_data): #to add new user to the file
    with open("passwd.txt", "a") as myfile: # append method is used
        myfile.write(user_data + "\n") # write in the new line
        print("User Created") 
#taking user inputs
user_data1 = read_user_data()
user_name = input("Enter new username: ").lower()
real_name = input("Enter real name: ")
password = input("Enter password: ")
# create user string
user_data = f"{user_name}:{real_name}:{password}"
#if-else condition 
if not check_login(user_name):
    adduser(user_data) #calling the function
else:
    print("Cannot add. Most likely username already exists.")
