x=[12,35,9,56,24]
y=[1,2,3]
x[0],x[-1]=x[-1],x[0]
print(x)
first=y.pop(0)
last=y.pop()
y.insert(0,last)
y.append(first)
print(y)

z=[12,35,58,24]
f=z.pop(0)
l=z.pop()

print(f)
print(l)

print(z)

z.insert(0,l)
print(z)
z.append(f)
print(z)
