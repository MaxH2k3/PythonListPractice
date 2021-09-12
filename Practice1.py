#Exercise 1: Remove odd number
def remove_event(MyList):         #case1
    NewList = []
    for index in range(0, len(MyList)):
        if MyList[index] % 2 == 0:
            NewList.append(MyList[index])
    if NewList == []:
        return None
    else:
        return NewList

def remove_odd1(MyList):        #case2
    New_List = MyList[:]
    for i in range(0, len(MyList)):
        if MyList[i] % 2 != 0:
            New_List.remove(MyList[i])
    return New_List

def remove_odd2(MyList):        #case3
    for i in range(len(MyList)-1, -1, -1):
        if MyList[i] % 2 != 0:
            MyList.remove(MyList[i])
    return MyList

#Exemple
MyList = [1, 2, 88, 5, 24]

NewList = remove_odd2(MyList)
print(NewList)


#Exercise 2: find people donate
def donate(name, DonateList):
    SumDonate = 0
    for index in range(0, len(DonateList)):
        if name == DonateList[index][0]:
            SumDonate = SumDonate + DonateList[index][1]
    return (name, SumDonate)

#Exemple 1
donate_list1 = [("Duong", 109090), ("Huy", 1097), ("Vu", 98000), ("Duong", 80090), ("Vu", 698000)]
result1 = donate("Duong", donate_list1)
print(result1)
#Exemple 2
donate_list2 = []
result2 = donate("Duong", donate_list2)
print(result2)



