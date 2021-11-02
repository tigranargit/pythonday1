mark = int(input("Please, enter your mark:"))

if mark > 85:
    print("Distinction")
else:
    if 85> mark > 65:
        print("Pass")
    else:
        print("Fail")