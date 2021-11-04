from os import read


read_only = open("/Users/tigran/Desktop/Tigran K/QA Academy/pythonqa/workingwithfiles/randometext.txt", "r")
read_only.readline()
read_only.readline()
read_only.readline()
read_only.readline()
line1 = read_only.readline()
line2 = read_only.readline()

print(line1)
print(line2)

read_only.close()

write_only = open("/Users/tigran/Desktop/Tigran K/QA Academy/pythonqa/workingwithfiles/randometext.txt", "w")

write_only.write(line1)
write_only.write(line2)
text = "This is an example of how we save bits of text and add this to the new file"
write_only.write(text)

write_only.close()