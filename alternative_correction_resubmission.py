#*****************************Complusory Task 1 ************************************
# The program converts a word inputed by a user and makes each alternative character an 
# upper case
final_word = ""

# Input validation to ensure that only letters are added.
user_input = (input("Input your word:\n>>>"))
if not user_input.replace(" ","").isalpha():
    print("Hey no digits allowed")
    user_input = (input("Please only enter letters:\n>>>"))
    
#converts user input to len and transfers it upper and lower 
word_length = len(user_input)



#Converts every alternative letter into Upper and lower case
for i in range(word_length):
    if i % 2 == 0:
        final_word += user_input[i].upper()
    else:
        final_word += user_input[i].lower()

print(final_word)

#**********please find part b of the complusory question under file alternative_part_b***************
#****************************************End of Code*********************************************************************