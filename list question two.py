l=[23,65,19,90]
l[0]=19
l[2]=23
print(l)

list=[19,65,23,90]
get=list[0],list[2]
list[2],list[1]=get
print(list)

list1=[19,65,23,90]
get=list1[0],list1[2]
list1[2],list1[0]=get
print(list1)
