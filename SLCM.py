import re
import os
from Crypto.Cipher import AES


def getusername_passwd():
    passwordregex = ("^(?=.*[a-z])(?=." +
                     "*[A-Z])(?=.*\\d)" +
                     "(?=.*[-+_!@#$%^&*.,?]).+$")
    usernameregex = "@+.*.com|.edu|.gov|.biz|.net/Z"

    username = input("Enter your username: ")
    password = input(" 1. Must be 8 characters or more,"
                     "\n 2. Contains at least one Capital letter,"
                     "\n 3. Contains at least one lowercase letter,"
                     "\n 4. Contains at least one number,"
                     "\n 5. and has at least one {#,@,%,*}"
                     "\n Enter your password: ")

    if re.search(passwordregex, password) and (len(password) >= 8) and re.search(usernameregex, username):
        print("Password and username accepted")
        return username, password, 1
        #Tuples rule
    else:
        print("Password or username is not valid. Please Try again.")
        getusername_passwd()


def secure_store(username, password, fileChoice, count):
    #AES Encryption NOT WORKING
    obj = AES.new('1234123412341234', AES.MODE_CBC, 'This is an IV456')
    encryptPass = obj.encrypt(password)

    #Checks for first run, creates file if needed and writes to it
    if fileChoice == 'Y' and count == 0:
        file = open("credential.dat", "w")
        file.write('Username: ' + username + ' Encrypted Password: ' + encryptPass + '\n')
        file.close()
    #Checks for additional runs, appending if requested or needed
    if fileChoice == 'N' or count > 0:
        file = open("credential.dat", "a")
        file.write('Username: ' + username + ' Encrypted Password: ' + encryptPass + '\n')
        file.close()


def main():
    deleteFile = 'X'
    # Checks if file exists, asks user if deletion is necessary
    while deleteFile != 'Y' and deleteFile != 'N':
        print('1')
        if os.path.exists("credential.dat"):
            deleteFile = input("Would you like to delete the current credential.dat file? (Y/N)")
            if deleteFile == 'Y':
                os.remove("credential.dat")
            elif deleteFile == 'N':
                print("Answered no, will append to current file")
            else:
                print("Please answer with a Y or N")
        else:
            deleteFile = 'Y'
    count = 0
    loop = 'Y'
    #Loop for user to add more usernames/passwords
    while loop == 'Y':
        username, password, value = getusername_passwd()
        if value == 1:
            secure_store(username, password, deleteFile, count)
        count = count + 1
        loop = input("Would you like to add another (Y/N)")
        while loop != 'Y' and loop != 'N':
            print("Please answer with a Y or N")
            loop = input("Would you like to add another (Y/N)")

main()
