def convert(listt):
    result=[]
    for i in range(len(listt)):
        result.append([])
    listt.reverse()
    for i in range(len(listt)):
        for t in range(len(listt)):
            result[t].append(listt[i][t])
    print(result)
convert([[1,2,3],[4,5,6],[7,8,9]])
convert([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
