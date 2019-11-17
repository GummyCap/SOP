"""My first program."""
done = False  # Are we finished?

name = input("Hello, my name is Python! Please type your name to continue our conversation.")  # Get user name
while done is False:  # Loop until you get acceptable answer
    answer = input("Have you programmed before?.")  # Get yes or no answer
    if answer == "Yes":
        print("Congratulations, " + name + "! It will be a little bit easier for you.")
        done = True  # Exit Loop
    elif answer == "No":
        print("Don`t worry, " + name + "! You will learn everything you need.")
        done = True  # Exit Loop
    else:
        print("Your input is incorrect!")
