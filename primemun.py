# x=0
# y=10
# print("print number between",x, "and", y, "are:")
# for num in range(x,y):
#   if num >1 :
#     for i in range (2,num):
#       if (num%i)==0:
#         break
#       else:
#         print(num)

# n=1
# while n <100:
#   print(n)
#   n=n+2
#if all(num%i!=0
#from operator import truediv


amount=0
prime = True
for num in range (100,200):
  for i in range (2,num):
     if all(num%i!=0):
      prime=False
      break
  if(prime):
     print(num)
     amount=amount+1
     prime=True
print(amount)