#!/usr/bin/python3

find = "nard"
mainstr = "My name is Leonard Muchuki"

def findNrep(searchStr="", mainStr=""):
    if mainStr.find(searchStr):
        print("found")
    else:
        print("Not found")

findNrep(find, mainstr)
