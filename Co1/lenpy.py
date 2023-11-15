list=[1,2,3,4,5,6,5416571,9841,991,984,16,54,491,4,659,518,12,1,9165,1526,548,161,1515]
print(len(list))
print(max(list))
print(min(list))
list.append("80")
print(list)

list1=['abc',45,60,75,90,77]
list1.remove(60)
print(list1)
print(list1.index(75))

b=[3,4,6,7,89,0]
b.extend (list1)
print(b)

b.reverse()
print(b)

b.pop(2)
print(b)
list=list1.copy()
print(list)

del(list[1])
print (list)
