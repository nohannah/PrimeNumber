# #sort function
# Numbers = [1,5,3,6,2,7,9,8,4]# list of number
# Numbers.sort()# use function sort to sort the number
# print(Numbers)
#sort number
num = [1,5,3,6,2,7,9,8,4] 
for i in range (len(num)):
    for j in range(i+1 , len(num)):
        if num[i]>num[j]: #< is from big to small , > is from small to big 
            num[i],num[j]=num[j],num[i]
print(num)
#ifstatement
