import os

class devices:

    def trusted(file_name):
        file = open(file_name, "r")
        file_lines = file.readlines()[1: ]
        for i in file_lines:
            print(i)

# trusted_devices("testing-os.txt")

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
        print("\033[31mNote\033[0m: The file you are listing off must be found in the same directory...")
        file_name_input = str(input("Name of file: "))
        devices.trusted(file_name_input)

    # This is for leaving the program entirely
    elif usr_input == "quit" or usr_input == "exit" or usr_input == "q":
        break

    else:
        print("\033[95mnetDET\033[0m : Unable to find that command")