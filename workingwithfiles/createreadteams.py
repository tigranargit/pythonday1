file = open("/Users/tigran/Desktop/Tigran K/QA Academy/pythonqa/workingwithfiles/teams.txt", "w")

line1 = "Man City"
line2 = "Liverpool"
line3 = "Tottenham"
line4 = "Chelsea"
line5 = "Man United"

file.write(line1 +"\n")
file.write(line2 + "\n")
file.write(line3 + "\n")
file.write(line4 + "\n")
file.write(line5 + "\n")

file.close()

file = open("/Users/tigran/Desktop/Tigran K/QA Academy/pythonqa/workingwithfiles/teams.txt", "r")

lines = file.readlines()
print(lines[0])
print(lines[3])

file.close()