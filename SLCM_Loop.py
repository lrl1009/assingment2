import re
import os
from Crypto.Cipher import AES


def getusername_paswd():
    Valid = False
    while Valid == False:
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
            Valid = True
            return 1, Valid
        else:
            print("Password or username is not valid. Please Try again.")
            Valid = False

def secure_store(username, password, fileChoice, count):
    #AES Encryption
    obj = AES.new('JG9A90cqiveJ8K7n'.encode("utf8"), AES.MODE_CFB, 'g4vhFIR1KncRIyvO'.encode("utf8"))
    encryptPass = obj.encrypt(password.encode("utf8"))

    #Checks for first run, creates file if needed and writes to it
    if fileChoice == 'Y' and count == 0:
        file = open("credential.dat", "w")
        file.write('Username: ' + username + ' Encrypted Password: ' + str(encryptPass) + '\n')
        file.close()
    #Checks for additional runs, appending if requested or needed
    if fileChoice == 'N' or count > 0:
        file = open("credential.dat", "a")
        file.write('Username: ' + username + ' Encrypted Password: ' + str(encryptPass) + '\n')
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
        username, password, value = getusername_paswd()
        if value == 1:
            secure_store(username, password, deleteFile, count)
        count = count + 1
        loop = input("Would you like to add another (Y/N)")
        while loop != 'Y' and loop != 'N':
            print("Please answer with a Y or N")
            loop = input("Would you like to add another (Y/N)")

main()
