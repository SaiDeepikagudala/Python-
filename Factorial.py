def fact(num):
    if num==0 | num==1:
        return 1
    else:
        return num*fact(num-1)
num=int(input("ENter the number: "))
print(fact(num))
