#! python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 bmyjacks

import sys

version = "0.0.0"

file_name = "example.zip"


print("This is openzip " + version)
print("Welcome!")
print("Input the file name:")
file_name = str(input())
print("File name is "+ file_name + " right?(Y or N)")
correct = "Y"
correct = input()
if correct == "Y":
    print("Start to progress...")
else:
    if correct == "N":
        print("Exit...")
        sys.exit
    else:
        print("You input a wrong strings")
        print("Exit...")
print("OK")
