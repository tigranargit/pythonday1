example_file = open("workingwithfiles/randometext.txt", "r")
print(example_file.readline()) #1st line
example_file.readline()
example_file.readline()
print(example_file.readline()) #4th line
example_file.seek(0)
print(example_file.readline()) #1st line

example_file.close()