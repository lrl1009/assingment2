import re


def getusername_paswd():
    passwordregex = ("^(?=.*[a-z])(?=." +
                     "*[A-Z])(?=.*\\d)" +
                     "(?=.*[-+_!@#$%^&*.,?]).+$")
    usernameregex = ("@+.*.com|.edu|.gov|.biz|.net/Z")

    username = input("Enter your username: ")
    password = input(" 1. Must be 8 characters or more,"
                     "\n 2. Contains at least one Capital letter,"
                     "\n 3. Contains at least one lowercase letter,"
                     "\n 4. Contains at least one number,"
                     "\n 5. and has at least one {#,@,%,*}"
                     "\n Enter your password: ")

    if re.search(passwordregex, password) and (len(password) >= 8) and re.search(usernameregex, username):
        print("Password and username accepted")
        return 1
    else:
        print("Password or username is not valid. Please Try again.")
        getusername_paswd()


def main():
    getusername_paswd()


main()
