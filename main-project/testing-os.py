import os       # used the os to get terminal command in our system
import pyckng   # our own library to retreive info in aircrack

# Possible other commands using the devices.
class devices:

    def trusted(file_name):
        file = open(file_name, "r")
        file_lines = file.readlines()[1: ]
        for i in file_lines:
            print(i)

# trusted_devices("testing-os.txt")

print("\nRetrieving data using 'airodump-ng'...")
# Plans for implemeting this part:
# - Try to get data of connected devices
# - When detected an untrusted device, it will give out a warning (see line 23)
not_detected = "\n\033[32mThere is no untrsuted devices detected in your router!\033[0m"
detected = "\n\033[31mTHERE WAS AN UNTRUSTED DEVICE(s) DETECTED IN YOUR ROUTER!\nEnter : 'detection' to see more info\033[0m"
no_untrusted_device = True

print("Successfully retrived data")
# print("Setting up seperate modules...") Unsure about this one though

if not no_untrusted_device:
    print(detected, "\n")
else:
    print(not_detected, "\n")

# Creating our own terminal within the python program
while True:
    # Getting the users input
    usr_input = str(input("\n\033[95mnetDET\033[0m> "))

    # Giving the version and possible small info of the program
    if usr_input == "info" or usr_input == "i":
        print("\n\033[95m~+ netDET +~\033[0m")
        print("    ----")
        print("Version  0.1 \n    BETA \n")

    # This is for listing the trusted devices.
    elif usr_input == "trusted":
        print("\033[31mNote\033[0m: The file must be exact...")
        file_name_input = str(input("Name of file: "))
        try:
            devices.trusted(file_name_input)
        except FileNotFoundError:
            print("Could not find that file in:")
            os.system("pwd")

    # This is for leaving the program entirely
    elif usr_input == "quit" or usr_input == "exit" or usr_input == "q":
        print("\nTake care! o/ \n")
        break

    else:
        print(f"\033[95mnetDET\033[0m : Unable to find \"{usr_input}\" in our library... Enter in \"help\" for all commands")