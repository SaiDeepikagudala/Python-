#STRONG NUMBER 
def strong_num(num): 
    sum = 0 
    temp = num 
    while num > 0: 
        i = 1 
        fact = 1 
        rem = num % 10 
        while i <= rem: 
            fact *= i 
            i += 1 
        sum += fact 
        num //= 10 
    return sum 
 
num = int(input("Enter a number: ")) 
 
# Check if the number is a strong number 
if strong_num(num) == num: 
    print("The given number is a strong number.") 
else: 
    print("The given number is not a strong number.")
