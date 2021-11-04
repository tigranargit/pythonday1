


file = open("/Users/tigran/Desktop/Tigran K/QA Academy/pythonqa/gitlab/wordlist.txt", 'r')
lines = file.readlines()

english_words = []
for l in lines:
    english_words.append(l.strip())


def conjug(word):
    for i in range(len(word)):
        for k in range(len(word)):
            newword = word[i:k]
            for j in english_words:
                if len(newword)>1 and newword == j:
                    print(newword)
    else:
        print("No English words found")

conjug("awesome")

file.close()
