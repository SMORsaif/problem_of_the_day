def tranigler(listt):
    areas=[]
    indx=0
    for i in listt: 
        w=0 # w = width
        h=i # h = hight
        for t in range(indx-1,-1,-1):
            if listt[t] >= i:
                w+=1
            else:
                break
        for y in range(indx+1,len(listt),1):
            if listt[y] >= i:
                w+=1
            else:
                break
        indx+=1
        areas.append(((w+1)*h))
    print(max(areas))

tranigler([2,1,5,6,2,3])
tranigler([2,4])
