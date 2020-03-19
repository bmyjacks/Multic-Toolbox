#! python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 bmyjacks


import sys
import zipfile


version = "0.0.2"


file_str = "E:\test\test.zip"
correct = "Y"
file_str_list = [""]
output_str = "E:\test\test\test"

print("This is openzip " + version)
print("Welcome!")
print("Input the file path:")
file_str = str(input())
print("File path is "+ file_str + " right?(Y or N)")

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
file_str_list = file_str.split(".")
if "zip" in file_str_list:
    print("Check OK...")
else:
    print("You input a worng file name, Please input like 'E:\test\test.zip' ")
    print("Exit...")
    sys.exit()

print("Input the output path:")
output_str = str(input())

print("Start to unzip the file...")
zip_file = zipfile.ZipFile(file_str, 'r')
for file in zip_file.namelist():
    zip_file.extract(file, output_str)
print("Unzip successfully")
