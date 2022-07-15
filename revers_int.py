# #Ask for enter the number from the use  
# num= int(input("Enter the integer number: "))  
  
# # Initiate value to null  
# revs_num = 0  
  
# # reverse the integer number using the while loop  
  
# while (num > 0):  
#     # Logic  
#     remainder = num % 10  
#     revs_number = (revs_number * 10) + remainder  
#     number = number // 10  
  
# # Display the result  
# print("The reverse number is : {}".format(revs_number))  
# from math import remainder


# num=5624
# rev_num=0
# while (num>0):
#     remainder=num%10
#     rev_num=(rev_num*10)+remainder
#     num=num//10
# print("The reverse number is:{}".format(rev_num))
#yuki method
number = int(input("Type the number:"))
reverse=0
while number!=0:
    remainder= number%10
    reverse=reverse*10+remainder
    number=number//10
print("The reverse number is:{}".format(reverse))