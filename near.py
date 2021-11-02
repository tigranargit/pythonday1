def near (word1, word2):
    if len(word1)<=len(word2):
            return False
    
    count =0
    while count < len(word1):
        newword = word1[:count]+word1[(count+1):]
        if word2 == newword:
            return True
        else:
            #print(newword)
            count+=1
    return False

            
print(near("sleet","lets"))
    