#To convert Decimal number into Binary number
def decimalToBinary(n):
    if(n > 1):
        decimalToBinary(n//2)
        print(n%2, end=' ')
n = int(input( "Enter an integer number: "))
print("The equivalent Binary number is : ", end='')
decimalToBinary(n)
