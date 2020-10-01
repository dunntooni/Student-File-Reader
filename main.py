"""
This program will read a list from a file of students
and display the class correctly.
Provides a name, grade, age in years,
and whether or not they're graduating this year.
"""

def promptFileName():
    fileName = input("Please enter the file name: ")
    return fileName

def readfile(fileName):
    print("Reading File...")
    f = open(fileName, "rt")
    classList = []
    classList = f.readlines()

    return classList

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
             + '{:13}'.format(2020 - int(studentInfo[2])) + studentInfo[3], end="")
    print("\n")

fileName = promptFileName()
classList = []
classList = readfile(str(fileName))
displayClassList(classList)