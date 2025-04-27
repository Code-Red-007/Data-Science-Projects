#********************Complusory 1***************************************************
# This program determines the award to given to each participant based on their total time.
# The awards are: 'Provincial colours', 'Provincial Half Colours', 'Provincial Scroll', 'No Award'.
# The program will then print out each participant and their corresponding awards.

# **************************************PART A User Input*********************************************************8
# User Inputs the participants name. Input validations includes;letters only; no null entry; 
#no characters less than 2; no characters more than 20 and no spaces.

#List created to valid user input and to sort user input
list_alphabet = ('a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm',
                 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z')
participants = []

#User first name input + validations
while True:
    print()
    print()
    participant_first_name = input("Enter the participant's first name or type 'quit' to exit:\n>>>")
    if participant_first_name.lower() == 'quit':
        if not participant_first_name.lower():
            break
        break
    while True:
        if len(participant_first_name) == 1:
            print("You have entered only one character for the first name.")
            participant_first_name = input(
                "Please enter more than one character for their first name:\n>>>")
            continue
        elif len(participant_first_name) == 0:
            print("You have not entered anything!")
            participant_first_name = input(
                "Please enter more than 2 letters or type 'quit' to exit:\n>>>")
            continue
        elif len(participant_first_name) > 20:
            print("You have entered more than 20 letters for their first name:\n>>>")
            participant_first_name = str(
                input("Please enter less than 20 letters for their first name:\n>>>"))
            continue
        elif any(char not in list_alphabet for char in participant_first_name):
            print("Invalid character, please check and re-enter.")
            participant_first_name = input(
                "Please enter the participant's first name, letters only:\n>>>")
            continue
        else:
            
#User Surname input + validations
            if participant_first_name.lower():
                participant_surname = input(
                    "Please enter the participant's surname:\n>>>")
            while True:
                if any(char not in list_alphabet for char in participant_surname):
                    print("Invalid character, please check and re-enter.")
                    participant_surname = input(
                        "Please enter the participant's surname, letters only:\n>>>")
                    continue
                elif len(participant_surname) == 0:
                    print("You have not entered anything!")
                    participant_surname = input(
                        "Please enter more than 2 letters or type 'quit' to exit:\n>>>")
                    continue
                elif len(participant_surname) > 20:
                    print(
                        "You have entered more than 20 letters for their first name:\n>>>")
                    participant_surname = str(
                        input("Please enter less than 20 letters for their first name:\n>>>"))
                    continue
                elif len(participant_surname) == 1:
                    print("You have entered only one character for the surname.")
                    participant_surname = input(
                        "Please enter more than one character for their surname:\n>>>")
                    break

#User events times + validations
                while True:
                    swim_times = input(
                        f"In minutes, enter the swim times for {participant_first_name} {participant_surname}:\n>>>")
                    try:
                        swim_times = float(swim_times)
                    except ValueError:
                        print("Invalid input, please enter a number.")
                        swim_times = input(
                            f"In minutes, enter the swim times for {participant_first_name} {participant_surname}:\n>>>")
                        continue
                    cycle_times = input(f"Enter the cycle times for {participant_first_name} {participant_surname}:\n >>>")
                    try:
                        cycle_times = float(cycle_times)
                    except ValueError:
                        print("Invalid input, please enter a number.")
                        cycle_times = input(
                            f"Enter the cycle times for {participant_first_name} {participant_surname}:\n >>>")
                        continue
                    run_times = input(
                        f"And lastly the run times in minutes for {participant_first_name} {participant_surname}:\n>>>")
                    try:
                        run_times = float(run_times)
                    except ValueError:
                        print("Invalid input, please enter a number.")
                        run_times = input(f"And lastly the run times in minutes for {participant_first_name} {participant_surname}:\n>>>")
                        break

#The program calculates the total time taken by adding all the events together
                    total_time = (swim_times + cycle_times + run_times)
                    break
                break
        break
    
#The program determines the award for each person   
    award = ""
    if total_time < 100:
        award = "Provincial Colours"
        print("They are awarded the PROVINCIAL COLOURS")
    elif 101 <= total_time <= 105:
        award = "Provincial Half Colours"
        print("They are awarded the PROVINCIAL HALF COLOURS")
    elif 106 <= total_time <= 110:
        award = "Provincial Scroll"
        print("They are awarded the PROVINCIAL SCROLL")
    elif total_time > 110:
       award = "No Award"
       print("NO AWARD")

#The program displays the total time for each participant and their subsequent award.
    print("Their total time is", total_time, "And their award is", award)

#The participant details are added to the list and the option to enter another participant is given.
#The program stops until the user says so.
    participants.append({'First Name': participant_first_name,
                        'Surname': participant_surname, 'Total Time': total_time, 'Award': award})
    print(f"{participant_first_name} {participant_surname} has been added to the list.\n")
    if len(participants) == 0:
         print("No participants have been entered.")
    else:
        print("Participants:")
        for participant in participants:
                  print(f"{participant['First Name']} {participant['Surname']}: {participant['Award']}")
                  
#*************************** End of Code****************************************************