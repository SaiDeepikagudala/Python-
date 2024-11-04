#calculator  
 
def add(a, b): 
    return a + b 
 
def subtract(a, b): 
    return a - b 
 
def multiply(a, b): 
    return a * b 
 
def divide(a, b): 
    if b == 0: 
        return "Error: Division by zero" 
    return a / b 
 
def calculator(): 
    print("Basic Calculator") 
    print("1. Addition") 
    print("2. Subtraction") 
    print("3. Multiplication") 
    print("4. Division") 
     
    choice = int(input("Enter your choice (1/2/3/4): ")) 
     
    if choice in [1, 2, 3, 4]: 
        num1 = float(input("Enter the first number: ")) 
        num2 = float(input("Enter the second number: ")) 
         
        if choice == 1: 
            print(f"The result of addition is: {add(num1, num2)}") 
        elif choice == 2: 
            print(f"The result of subtraction is: {subtract(num1, num2)}") 
        elif choice == 3: 
            print(f"The result of multiplication is: {multiply(num1, num2)}") 
        elif choice == 4: 
            print(f"The result of division is: {divide(num1, num2)}") 
    else: 
        print("Invalid choice. Please enter a number between 1 and 4.") 
 
calculator()
