total = 0
count = 0
while True:
    user_input = input("Please enter a number. To stop the program enter -1:\n>>>")
    if user_input == '-1':
        break
    if not user_input.isnumeric():
        print("Hey, only digits are allowed!")
        continue
    
    user_input = int(user_input)
    total += user_input
    count += 1
    
average = total / count if count > 0 else 0
print("The average of the numbers entered is:", average)

