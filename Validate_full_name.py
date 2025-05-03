user = input ("Please enter your full name:\n>")
if len(user)==0:
        print("You haven’t entered anything.")            
elif len(user)>0 <4:
        print("You have entered less than 4 characters.")
elif len(user)>= 25:
        print("You have entered more than 25 characters.  Please make sure that you have only entered your full name")
else:
    print("Thank you for entering your name.")