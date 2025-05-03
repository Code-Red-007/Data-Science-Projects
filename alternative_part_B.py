#*****************************Complusory Task 1 Part B ************************************
# The program converts each word in a sentence to  alternative between lower case and 
# upper case.

# Input validation to ensure that only letters are added.
user_input = (input("Input your sentence: \n>>>"))
if not user_input.replace(" ","").isalpha():
     print("Hey no digits allowed")
     user_input = (input("Please only enter sentences that contains letters:\n>>>"))
    
#Split the sentence into a list of words
user_split = user_input.split()  
new_user_sentence = ""
 
#Transforms each word into alternate lower and upper case.
for i in range (len(user_split)):
      if i % 2 == 0:
          new_user_sentence += user_split[i].lower()
      else:
          new_user_sentence += user_split[i].upper()
# Adds a space betweene each word
      new_user_sentence += " "          
print(new_user_sentence)

# #****************************************End of Code**********************************