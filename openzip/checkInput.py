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
