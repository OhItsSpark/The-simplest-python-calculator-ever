def sum(a,b):
    sum=a+b
    return sum

def differ(a,b):
    dif=a-b
    return dif

def prod(a,b):
    produ=a*b
    return produ

def div(a,b):
    divi=a/b
    return divi


print("----")

option = int(input("Select one of the following operations:\n1.- To sum\n2.- To substract\n3.- To multiply\n4.- To divide\n----\nSelect Option: "))

if option == 1:
    v1=int(input("Insert First number: "))
    v2=int(input("Insert Second Number: "))
    print(sum(v1,v2))
elif option == 2:
    v1=int(input("Insert First number: "))
    v2=int(input("Insert Second Number: "))
    print(differ(v1,v2))
elif option == 3:
    v1=int(input("Insert First number: "))
    v2=int(input("Insert Second Number: "))
    print(prod(v1,v2))
elif option == 4:
    v1=int(input("Insert First number: "))
    v2=int(input("Insert Second Number: "))
    print(div(v1,v2))
else:
    print("ERROR")