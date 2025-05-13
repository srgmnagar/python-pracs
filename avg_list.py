def avg(lst):
    sum = 0
    for i in range(len(lst)):
        sum+= lst[i]
    return sum/len(lst)

lst=[2,3,4,7,5,8,4,2]
sum=avg(lst)
print("Average of list is: ", sum)