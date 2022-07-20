num=int(input("Type a interger number:"))
while (num>0):
    reminder=num%10
    if (reminder!=0 and reminder!=1):
        print("number is not binary ")
        break
    num=num//10
    if(num==0):
        print("Number is binary")
    # reverse=(reverse*10)+reminder
    #num=num//10
# print("Reverse number is: ",reverse)