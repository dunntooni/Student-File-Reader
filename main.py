"""
This program will read a list from a file of students
and display the class correctly.
Provides a name, grade, age in years,
and whether or not they're graduating this year.
Also provides the option to add a new student
to the roster.
"""

# Gets a file name from the user. There's no input handling
# in this version, so be careful. If the file name isn't valid,
# the program will not work.
def promptFileName():
    fileName = input("Please enter the file name: ")
    return fileName

# Reads the file line by line and stores it in a list of strings
def readFile(fileName):
    print("Reading File...")
    f = open(fileName, "rt")
    classList = []
    classList = f.readlines()
    f.close()
    return classList

# Displays the information contained in the files. Converts
# their age to a birth year just for fun. I get that it
# could be inaccurate depending on their birthday, but
# I don't care too much.
def displayClassList(classList):
    print(" ")
    print("Class Info:\n")
    print("Student Name   Grade   Birth Year   Graduating")
    print("------------   -----   ----------   ----------")
    for x in classList:
        #print('{:15}'.format(x))
        #print('{:15}'.format('test') + '{:8}'.format('test') + "test")
        studentInfo = x.split(" ")
        print('{:15}'.format(studentInfo[0]) + '{:8}'.format(studentInfo[1])\
             + '{:13}'.format(str(2020 - int(studentInfo[2]))) + studentInfo[3], end="")
    print("\n")

# Prompts the user for all the information about the student
# that it needs. Be careful not to input invalid information.
# I didn't do any input checking on this one either.
def writeFile(fileName):
    f = open(fileName, "a")
    name = input("Please input the student's name: ")
    grade = input("Please input the student's current grade out of 100: ")
    bYear = input("Please input the student's birth year: ")
    graduating = input("Is the student set to graduate this year? (Y/N) ")
    if graduating == "Y" or graduating == "y" or graduating == "yes"\
        or graduating == "YES" or graduating == "Yes":
        graduating = "Yes"
    elif graduating == "N" or graduating == "n" or graduating == "no"\
        or graduating == "NO" or graduating == "No":
        graduating = "No"
    else:
        graduating = "Unknown"
    f.write("\n" + name + " " + grade + " " + str(2020 - int(bYear)) + " " + graduating)
    f.close()


fileName = promptFileName()
classList = []
classList = readFile(str(fileName))
displayClassList(classList)
writeFilePrompt = input("Would you like to add a student to this roster? (Y/N)")
if writeFilePrompt == "y" or writeFilePrompt == "Y" or writeFilePrompt == "yes"\
    or writeFilePrompt == "Yes" or writeFilePrompt == "YES":
    writeFile(fileName)
    classList = readFile(str(fileName))
    print("\nUpdating class list...")
    displayClassList(classList)