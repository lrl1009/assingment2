
import re

def getusername_paswd():
    passwordregex = ("^(?=.*[a-z])(?=." +
                     "*[A-Z])(?=.*\\d)" +
                     "(?=.*[-+_!@#$%^&*., ?]).+$")
    usernameregex = (".[.com, .gov, .edu, .net, .biz]{1}$" +
                     ".@{1}")

    username = input("Enter your username: ")
    password = input("Enter your password: "
                     "\n 1. Must be 8 characters or more,"
                     "\n 2. Contains at least one Capital letter,"
                     "\n 3. Contains at least one lowercase letter,"
                     "\n 4. Contains at least one number,"
                     "\n 5. and has at least one {#,@,%,*}")



 #   if (".com" or ".edu" or ".gov" or ".net" or ".biz") in username and "@" in username:
 #       return 1
 #   else:
 #       return None

    if re.search(passwordregex, password):
        print("Password accepted")
        return 1
    else:
        print("Password is not valid. Please Try again.")

    if re.search(usernameregex, username):
        print("Username accepted")
        return 1
    else:
        print("Username is not valid. Please try again.")
