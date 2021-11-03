def near (word1, word2):
    if len(word1)<=len(word2):
        return False
    
    
    for i in range(len(word1)):
        newword = word1[:i]+word1[(i+1):]
        if word2 == newword:
            return True
    else:
        return False
            
print(near("reset", "rest"))

print(near("dragoon", "dragon"))

print(near("eave", "leave"))

print(near("sleet", "lets"))
    