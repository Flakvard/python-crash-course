#message = input("Tell me something, and I will repeat it back to you: ")
#print (message)

#name = input("Please enter your name: ")
#print(f"\nHello, {name}!")

# promt = "If you tell us who you are, we can personalize the message you see."
# promt += "\nWhat is your first name? "

# name = input(promt)
# print(f"\nHello, {name}!")

# height = input("How tall are you, in cm? ")
# height = int(height)

# if height >= 150:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# promt = "\nTell me something...: "
# promt += "\n Enter 'quit' to end the program. "
# message = ""

# while message != 'quit':
#     message = input(promt)
    
#     if message != "quit":
#         print(message)

#USING FLAGS active unactive (true/false)
promt = "\nTell me something...: "
promt += "\n Enter 'quit' to end the program. "
active = True
while active :
    message = input(promt)
    
    if message == "quit":
        active = False
    else:
        print(message)

