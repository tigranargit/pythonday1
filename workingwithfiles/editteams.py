file = open("/Users/tigran/Desktop/Tigran K/QA Academy/pythonqa/workingwithfiles/teams.txt", "r")

line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
line4 = file.readline()
line5 = file.readline()

newline = "This is a new line"

file.close()

file = open("/Users/tigran/Desktop/Tigran K/QA Academy/pythonqa/workingwithfiles/teams.txt", "w")

line1 = newline + "\n"
file.write(line1)
file.write(line2)
file.write(line3)
file.write(line4)
file.write(line5)

file.close()

file = open("/Users/tigran/Desktop/Tigran K/QA Academy/pythonqa/workingwithfiles/teams.txt", "r")

lines = file.readlines()
print(lines)