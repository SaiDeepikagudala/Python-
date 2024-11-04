# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:21:08 2021

@author: SRINIVAS
"""

'''checking for indian pincode'''
import re
def is_valid_pin(pin_code):
    '''pincode rergular expression'''
    regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
    check_pin = re.compile(regex)
    if pin_code == '':
        return False
    match_pin = re.match(check_pin, pin_code)
    if match_pin is None:
        return False
    else:
        return True
if __name__ == "__main__":
    NUM_1 = "503124"
    print(NUM_1, ": ", is_valid_pin(NUM_1))
    NUM_2 = "201 305"
    print(NUM_2, ": ", is_valid_pin(NUM_2))
    NUM_3 = "014205"
    print(NUM_3, ": ", is_valid_pin(NUM_3))
    NUM_4 = "5000967"
    print(NUM_4, ": ", is_valid_pin(NUM_4))
