num=int(input("Type a interger number:"))
temp=num;
reverse=0
while (num>0):
    reminder=num%10
    reverse=(reverse*10)+reminder
    num=num//10
print("Reverse number is: ",reverse)
if(reverse==temp):
    print("True")
else :
    print("False")

