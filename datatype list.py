list=['prateek',(1,2),(2,3),[0,1,2],{'key':"value"}]
print(list)
print("")
#append method
list.append('using append method')
print(list)
print("")
#insert method
list.insert(2,"we have replaced the tuple with this string")
print(list)
print("")
#extend method
list.extend(["we are extending this list to",10,11,12])
print(list)
print("")
list.reverse()
print(list)

y=[1,2,3,4]
for i in range(2,len(y)):
    y.remove(i)
print(y)

str="my name is prateek"
print(str[::-1])

print(y[::-1])
