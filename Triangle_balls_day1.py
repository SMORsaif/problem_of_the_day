white = int(input("white : "))
black = int(input("black : "))

def suprit(num,type):
    listt=[]
    if type == "even":
        first=2
        while True:
            if num == 0:
                return listt
            elif (sum(listt) < num and sum(listt)+first <= num):
                listt.append(first)
                first+=2
            else:
                break
    elif type=="obb":
        first=1
        while True:
            if num ==0:
                return listt
            elif (sum(listt) < num and sum(listt)+first <= num):
                listt.append(first)
                first+=2
            else:
                break
    return listt

def lines(list1,list2):
    list_ = list1+list2
    reslt=0
    target_number = 1
    if len(list_) == 0:
        return 0
    for i in range(max(list_)):
        if target_number in list_:
            reslt+=1
            target_number+=1
        else:
            break
    return reslt

print(max(lines(suprit(white,"obb"),suprit(black,"even")),lines(suprit(black,"obb"),suprit(white,"even"))))
