def read_user_data(): #created this function to read the file
    with open("passwd.txt", "r") as file:
        lines = file.readlines() #reads the entire file
        return [line.strip().split(":") for line in lines]

def write_user_data(user_data): #function created to write 
    with open("passwd.txt", "w") as file:
        for user in user_data:
            file.write(f"{user[0]}:{user[1]}:{user[2]}\n") #f-string 

def remove_user(username, user_data): #to remove the user
    new_user_data = [user for user in user_data if username != user[0]] #if user name is not equals to existed user it returns the value
    return new_user_data
#taking user input
user_name = input("Enter username: ")
user_data = read_user_data() #calling the function and assigining to another variable

updated_user_data = remove_user(user_name, user_data) #calling the function and assigning it to another variable
#checking if the user is deleted or not
if len(updated_user_data) < len(user_data): #if deleted then it excute the below statement
    print("User deleted")
    write_user_data(updated_user_data) #calling the function 
else: #if not it excute this statement
    print("User not found")
