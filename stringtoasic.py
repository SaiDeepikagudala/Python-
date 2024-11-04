#WAP to find sum of ascii values of all the special characters present inside the string. 
 
def ascii_sum(input_string): 
    ascii_sum = 0 
    for char in input_string: 
        if not char.isalnum() and not char.isspace(): 
            ascii_sum += ord(char) 
    return ascii_sum 
input_string = "Hello! How are you doing? I'm fine, thank you." 
print("Sum of ASCII values of special characters:", ascii_sum(input_string)) 
