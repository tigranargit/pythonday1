file = open("/Users/tigran/Desktop/Tigran K/QA Academy/pythonqa/workingwithfiles/teams.txt", "w")

line1 = "Man City"
line2 = "Liverpool"
line3 = "Tottenham"
line4 = "Chelsea"
line5 = "Man United"

#Another way of doing it:
# teams = ["Man City", "Liverpool"..."Man United"]
# for i in teams:
#   file.write(i + "\n")

file.write(line1 +"\n")
file.write(line2 + "\n")
file.write(line3 + "\n")
file.write(line4 + "\n")
file.write(line5 + "\n")

file.close()

# Step 2 - Read and Display

file = open("/Users/tigran/Desktop/Tigran K/QA Academy/pythonqa/workingwithfiles/teams.txt", "r")

lines = file.readlines()
print(lines[0])
print(lines[3])

# Another way of doing it:
#print(file.readline()) - prints first line
#file.readline()
#file.readline()
#print(file.readline()) 


file.close()