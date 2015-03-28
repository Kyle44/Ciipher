# File:        hw8.py
# Written by:  Kyle Fritz
# Date:        11/7/2013
# Lab Section: 10
# UMBC email:  fritzk1@umbc.edu
# Description: File Processing and using a Cipher to encode a .txt file
############### USE WITH PYTHON 3 ###########
# scl enable python33 bash


def printGreeting():
    print("This is the Cipher program.")

# input: The list of ciphers and the text file
# output: The text file is converted to the cipher in results.txt
def convertToCipher(listOfCiphers):
    results = open("results.txt", "w")
    flag = False
    codeList = []
    for i in range(26):
        codeList.append(listOfCiphers[i][2])
    # This determines if one or more codes are used more than once
    flag = validateCipher(codeList)
    if flag == False:
        print("At least one of your codes occur more than once in the cipher.")
        listOfCiphers = []
        return
    # This makes sure a correct file is chosen
    try:
        print("Enter the name of the file that", end = " ")
        regTextFile = input("you want to display to the screen: ")
        readRegText = open(regTextFile, "r")
    except FileNotFoundError:
        print("That is not a valid file name, please try again.")
        return
    textList = []
    textStr = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    newList = []
    # This makes the file into a string
    for i in readRegText:
        textStr = textStr + i
        textStr = textStr.lower()
    textList = list(textStr)
    # This converts the file using the cipher
    for i in textList:   
        if i in alpha:
            for j in listOfCiphers:
                if j[0] == i:
                    newList.append(j[2])
        else:
            newList.append(i)
    codeString = ""
    codeString= "".join(newList)
    results.write(codeString)
    print("The results are in results.txt now.")
        
# input: Contents of results.txt
# output: Contents displayed to the screen
def printResults():
    results = open("results.txt", "r")
    for i in results:
        print(i)
    results.close()
    
# input: The cipher text
# output: The cipher is displayed on the screen
def printCipher(listOfCiphers):
    for i in listOfCiphers:
        print(i)

# input: The regular text file
# output: Displays the text file to the screen
def printRegularTextFile():
    print("Enter the name of the file that", end = " ")
    regTextFile = input("you want to display to the screen: ")
    readRegText = open(regTextFile, "r")
    for i in readRegText:
        print(i)
    readRegText.close()

# input: The cipher file
# output: Whether or not the cipher file has 26 lines
def validateFileLength(cipher):
    flag = False
    readCipher = open(cipher, "r")
    listOfCiphers = []
    for i in range(26):
        try:
            readingCipher = readCipher.readline().strip()
            listOfCiphers.append(readingCipher.lower())
            flag = True
        except IndexError:
            flag = False
    if flag == False:
        print("Your cipher text is not the right file length (26).")
    if flag == True:
        return listOfCiphers
    cipher.close()

# input: The cipher section of the cipher list
# output: Whether or not a cipher appears more than once
def validateCipher(listOfCiphers):
    flag = True
    cipherCheck = []
    count = 0
    for i in listOfCiphers:
        cipherCheck.append(i)
        count += 1
        if i in listOfCiphers[count:]:
            flag = False
    return flag

def main():
    printGreeting()
    userChoice = "g"
    listOfCiphers = []
    results = open("results.txt", "w")
    while userChoice != "f":
        print("a.) Load cipher input (to be used later).")
        print("b.) Convert regular text to ciphered (cipher MUST be loaded).")
        print("c.) Display cipher to screen.")
        print("d.) Display regular text to screen.")
        print("e.) Display current results.txt to screen.")
        print("f.) Quit")
        userChoice = input("Enter a menu choice: ")
        userChoice = userChoice.lower()
        if userChoice == "a":
            cipher = input("Type in the name of the cipher text: ")
            listOfCiphers = validateFileLength(cipher)
        elif userChoice == "b":
            # This makes sure that there is a cipher list
            if listOfCiphers != None and listOfCiphers != []:
                convertToCipher(listOfCiphers)
            else:
                print("You nee to input a cipher first!")
        elif userChoice == "c":
            if listOfCiphers != None and listOfCiphers != []:
                printCipher(listOfCiphers)
            else:
                print("You need to input a cipher first!")
        elif userChoice == "d":
            printRegularTextFile()
        elif userChoice == "e":
            printResults()
        elif userChoice == "f":
            print("See you later!")
        else:
            print("That is not a valid option. Please pick another.")
main()
