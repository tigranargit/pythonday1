writing_file = open("/Users/tigran/Desktop/Tigran K/QA Academy/pythonqa/workingwithfiles/randometext.txt", "w")

for i in range(1,11):
    newline  = "This is a line of text" + str(i) + "\n"
    writing_file.write(newline)

writing_file.close()

with open("/Users/tigran/Desktop/Tigran K/QA Academy/pythonqa/workingwithfiles/randometext.txt", "w") as example_file:
    #if error - will close file automatically
    line1 = "This is a line of number that are part of a lopp"
    writing_file.write(line1)

    #closes file automatically
