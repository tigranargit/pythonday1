

def timestable(number):

    show_result = ""

    for i in range(1,number+1):
        for j in range(1,number+1):
            multiply= i*j
            show_result = show_result + str(multiply) + "\t"
        print(show_result)
        show_result = ""
        
timestable(5)


#
# Another student's solution
# input_value = int(input("Enter value for which you would like to see multiplication"))



#counter1 = 1

#counter2 = 1

#show_result = ""


#for counter1 in range(1,input_value+1):

    #for counter2 in range(1,input_value+1):

        #result = counter1 * counter2

        #show_result = show_result + str(result) + "\t"

        #counter2 += 1

    #print(show_result)

    #show_result = ""

    #counter1 += 1