isbn="978030640615"
count=0
dig13sum=0

while count < 12:
    if count%2==0:
      dig13sum=dig13sum+int(isbn[count])
      count+=1
     # print('dig13sum=',dig13sum, "count=", count)
    else:
        dig13sum=dig13sum+3*int(isbn[count])
        count+=1
        #print('dig13sum=',dig13sum, "count=", count)
dig13=10-dig13sum%10
print("dig13=",dig13)

