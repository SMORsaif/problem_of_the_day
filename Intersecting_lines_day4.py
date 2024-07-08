def mn(listt):
    list1=[]
    list2=[]
    for i in range(len(listt)):
        
        if i % 2 ==0:
            list1.append(listt[i])
        else:
            list2.append(listt[i])
    result1=False
    result2=False
    for i in range(len(list1)-1):
        if list1[i] >= list1[i+1]:
            result1=True
            break
    for i in range(len(list2)-1):
        if list2[i] >= list2[i+1]:
            result2=True
            break
    return(result1 or result2)
print(mn([2,1,1,2]))
print(mn([1,2,3,4]))
print(mn([1,1,1,2,1]))

