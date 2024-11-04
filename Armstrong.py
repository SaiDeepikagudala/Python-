#WAP to check weather the given number is Armstrong number or not. 
 
def armstrong(input_num): 
    original_num=input_num 
    summ=0 
    while(input_num>0): 
        rem=input_num%10 
        summ+=rem**3 
        input_num=input_num//10 
    if summ==original_num: 
        return True 
    else: 
        return False 
input_num= 153 
print("armstrong : ",armstrong(input_num))  
