# Examples of Operator Precedence

# Precedence of '+' & '*'
expr = 10 + 20 * 30
print(expr)

# Precedence of 'or' & 'and'
name = "Alex"
age = 0

if name == "John" or name == "Alex" and age >= 2:
	print("Hello! Welcome.")
else:
	print("Good Bye!!")

print("")
# Examples of Operator Associativity

# Left-right associativity
# 100 / 10 * 10 is calculated as
# (100 / 10) * 10 and not
# as 100 / (10 * 10)
print(100 / 10 * 10)

# Left-right associativity
# 5 - 2 + 3 is calculated as
# (5 - 2) + 3 and not
# as 5 - (2 + 3)
print(5 - 2 + 3)

# left-right associativity
print(5 - (2 + 3))

# right-left associativity
# 2 ** 3 ** 2 is calculated as
# 2 ** (3 ** 2) and not
# as (2 ** 3) ** 2
print(2 ** 3 ** 2)

print("")
a=10
b=20
print("a is equal to b" if a==b else "a is greater than b" if a>b else "b is greater than a")


if(a!=b):
    if(a>b):
        print("a is greater than b")
    else:
        print("b is greater than a")
        
else:
    print("a and b are equal")



