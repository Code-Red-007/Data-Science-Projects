#*********************** COMPLUSORY TASK PART A *****************************************
# Per the instructions of the task I followed to the tee.  Where the user has to input their name.
# If the user fails to meet the requirements of 4-25 character inclusie then an error message would
# be printed out.

user = input ("Please enter your full name:\n>")

if len(user)==0:
        print("You haven’t entered anything.")            
elif len(user)<4:
        print("You have entered less than 4 characters. Please make sure that you have entered your name and your surname.")
elif len(user) >24:
        print("You have entered more than 25 characters.  Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")

#***************** END OF CODE - However I found that the above code to be unrealistic*****************


# I was thinking about what would happen in real life.  
# I wrote this program because I was thinking what if the user were to repeatedly make the same mistakes.  
# I wanted the program to keep going until the user had entered the correct information, then the 
# the program would end.
#
# I've decided to use a while True command as it would give me the endless lopp.  I paired this with the 
# continue function.
# The program would keep on going until the condition was met.
# I could adapt the code even more by adapting a forced format, but I don't know how to do this.


user = input ("Please enter your full name:\n>")

while True:
        if len(user)  == 0 :
                print("You haven’t entered anything.")
                user = input ("Please enter your full name and your surname:\n>") 
                continue
                 
        elif len(user) >25 :          
                print("You have entered more than 25 characters.")
                user = input ("Please make sure that you have only entered your full name.:\n>") 
                continue
                                                
        elif len(user) <4 :
                print ("You have entered less than 4 characters.")
                user = input ("Please make sure that you have entered your name and your surname:\n>")
                continue
                
        else:   
                print("Thank you for entering your name")

        break
        #************************ END OF CODE ************************************************
