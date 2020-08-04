def add(a,b):
    return (a+b)
def sub(c,d):
    return (c-d)
def div(e,f):
    return (e/f)
def mul(g,h):
    return (g*h)


g = int(input("Enter the First Number: "))
h = int(input("Enter the 2nd Number:"))
print("1.add")
print("2.sub")
print("3.div")
print("4.mul")
operation = int(input("Select The Operation (1/2/3/4): "))
if operation == 1:
    print(add(g, h))
if operation == 2:
    print(sub(g, h))
if operation == 3:
    print(div(g, h))
if operation == 4:
    print(mul(g,h))
else: print ("Error")