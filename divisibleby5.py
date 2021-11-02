numbers_list = [10,20,33,36,55]

def divby(list_of_nums):
 
    for number in list_of_nums:

        if number%5 == 0:
            print(number)

print("List is ", numbers_list)
print("Numbers divisable by 5 are:")
divby(numbers_list)
