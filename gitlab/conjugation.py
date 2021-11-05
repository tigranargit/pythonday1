


file = open("/Users/tigran/Desktop/Tigran K/QA Academy/pythonqa/gitlab/wordlist.txt", 'r')
lines = file.readlines()

english_words = []
for l in lines:
    english_words.append(l.strip())


#def conjug(word):
 #   for i in range(len(word)):
  #      for k in range(len(word)):
   #         newword = word[i:k]
    #        for j in english_words:
     #           if len(newword)>1 and newword == j:
      #              print(newword)
    #else:
     #   print("No English words found")
def conjug(word):
    for i in english_words:
        if i in word and len(i) !=1: 
            print(i)
            if english_words[-1] == i: 
                print("Last word check")
           
conjug("awesome")

file.close()
