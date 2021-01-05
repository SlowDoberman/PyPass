import string
import random
import time

path = "" #replace with your path to the password file

# generate a randomized password
def randompassword():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 8
    return ''.join(random.choice(chars) for x in range (size, 20))


# user can choose to look up, add or replace a password (in a txt file called pw.txt)
def useraction():
    print("What do you wish to do? Please type 'call', 'add' or 'replace'")
    print("Type help for more information")
    cmdlist = ["call", "add", "replace"]
    cmd = getcmd(cmdlist)

    if cmd == "call":
        callpw()
    elif cmd == "add":
        addpw()
    elif cmd == "replace":
        replacepw()

# lets the user look up a certain password and checks if is there one
def callpw():
        print("For which platform do you want to see the password?")
        platform = input(">")
        searchfile = open(path, "r")
        for line in searchfile:
            if platform in line:
                print(line)
                break
        else:
            print("No password found")
        searchfile.close()



# lets the user add a new platform and replace a password for it
def addpw():
    print("Enter the platform you would like to add.")
    platform = input(">")
    t = open(path, "a")
    t.write("\n")
    t.write(platform)
    t.write(": ")
    t.write(randompassword())
    t.close()
    print("Your password for", platform, "has been added")

#replaces the password password for an already saved platform
def replacepw():
    print("For which platform do you want to replace the password?")
    platform = input(">")
    searchfile = open(path, "rt")
    for line in searchfile:
        if platform in line:
            replacement = f"{platform} : {randompassword()}"
            print(replacement)
            t = open(path, "r+")
            t.write(line.replace(str(line), str(replacement)))
            #line.replace(str(line), str(replacement))
            break
            t.close()


def getcmd(cmdlist):
    cmd = input("I wish to...")
    if cmd in cmdlist:
        return cmd
    elif cmd == "help":
        print("\nCall: Look up a certain password")
        print("\nAdd: replace a random password for a new platform")
        print("\nReplace: Replace a platform's password")
        print("\nQuit: Quit the program")
        return getcmd(cmdlist)
    elif cmd == "quit":
        print("\n---------")
        time.sleep(0.5)
        print("Program is shutting down...")
        time.sleep(0.5)
        exit()

while True:
    time.sleep(0.05)
    print("\n")
    useraction()

if __name__ == "__main__":
    useraction()
