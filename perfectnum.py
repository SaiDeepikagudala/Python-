#perfect number check 
==================== 
 
def perfect_number(num): 
    if num < 1: 
        return False 
    sum1 = 0 
    for i in range(1, num): 
        if num % i == 0: 
            sum1 += i 
    return sum1 == num 
 
num = int(input("Enter a number: ")) 
 
if perfect_number(num): 
    print("The given number is a perfect number.") 
else: 
    print("The given number is not a perfect number.")   
