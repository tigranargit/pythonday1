class Student:

    def __init__(self,name, age, class_ = "student"):
        self.name = name
        self.age = age
        self.class_=class_

    def avtestscore (self, score1, score2, score3):
        average = round((score1 + score2 + score3)/3)
        return(average)    

Jane = Student("Jane", "24")
John = Student("John", "30", "non-student")

print(f"John's average score is:",John.avtestscore(30,30,30))
print(f"Jane's average score is:",Jane.avtestscore(60,43,10))

