#! python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 bmyjacks

import sys
import zipfile

version = "0.0.1"

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
        sys.exit()
    else:
        print("You input a wrong strings")
        print("Exit...")
        sys.exit()
print("Spliting input...")
file_name_list = [""]
file_name_list = file_name.split(".")
if "zip" in file_name_list:
    print("Check OK...")
else:
    print("You input a worng file name, Please input like 'test.zip' ")
    print("Exit...")
    sys.exit()
print("Start to unzip the file...")
zip_file = zipfile.ZipFile(file_name, 'r')
for file in zip_file.namelist():
    zip_file.extract(file, "./")
print("Unzip successfully")
