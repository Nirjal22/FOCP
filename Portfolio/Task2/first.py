import sys #importing module for command line argument.
def analyze_cat_shelter(file_name): #creating the function
    try:
        # opening file using file handling
        with open(file_name,'r') as my_file:
            final_file = my_file.readlines()
            # final_file is in list data-type.
            # creating the variables to assign the values
        correct_cat_entries = 0
        wrong_cat = 0
        total_time_correct_cat = 0
        correct_cat_visits = 0
        longest_visit = 0
        shortest_visit = float('inf') #floating point positive infinity
# using for-loop to loop each and every values inside the file
        for looping in final_file:
            if looping.strip() == "END":
                break

            ours_value = looping.strip().split(',') #using strip() and split() functions and assigning the values
            checking_cats = ours_value[0]
            time_start = int(ours_value[1])
            time_end = int(ours_value[2])
            stayed_time = time_end - time_start
            # checking using if-condition
            if checking_cats == "OURS":
                correct_cat_entries += 1
                total_time_correct_cat += stayed_time #total time 
                hours = total_time_correct_cat //60 #changing into hours
                minutes = total_time_correct_cat % 60 #finding the remaining minutes
                time_string = "{} Hours {} Minutes".format(hours, minutes) 
                correct_cat_visits += 1
                longest_visit = max(longest_visit, stayed_time)
                shortest_visit = min(shortest_visit, stayed_time)
            elif checking_cats == "THEIRS":
                wrong_cat += 1

        if correct_cat_visits == 0:
            avg_duration = 0
        else:
            avg_duration = int(total_time_correct_cat / correct_cat_visits) #finding the average time.
        # displaying the results
        print(f"Cat visit: {correct_cat_entries}")
        print(f"Other cat: {wrong_cat}\n")
        print(f"Total time in house: {time_string} Minutes \n")
        print(f"Average visit length: {avg_duration} Minutes")
        print(f"Longest visit: \t\t{longest_visit} Minutes")
        print(f"Shortest visit: \t{shortest_visit} Minutes")
        
        # exceptional handling
    except ValueError:
        print("Error! File not found.")

if __name__ == "__main__":
        print("Log File Analysis\n==================\n")
# If the entered values by the user is invalid then it asks the user to enter again until the user enter the correct input.
# taking command-line arguments
        while True:
            if len(sys.argv) != 2:
                print("Invalid Input!")
                user_input = input("Usage: python analyze_cat_shelter.py <file_path>\nEnter correct input: ")
                sys.argv = ["analyze_cat_shelter.py", user_input]  # Update sys.argv with user input
            else:
                file_name = sys.argv[1]
                analyze_cat_shelter(file_name)
                break  # Exit the loop once the correct input is provided
