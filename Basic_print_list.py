#*****************Complusory 2************************************
#The program executes a lists, on a separate line, of the customer's three favourite food items.
print ("You will asked to enter your 3 favourite food items.")  
item_1 = input ("Please enter your first favourite food item:")
item_2 = input ("Thank you.  Please enter your second favourite food item:")
item_3 = input ("Thank you. Please enter your third favourite food item:")
food_list = [item_1,item_2,item_3]  # This define the favourite foods as a list
print("Your order has been confirmed, you have ordered:")
print(*food_list, sep = "\n")  
#***************End of Code***************************************