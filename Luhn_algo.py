"""
The Luhn Algorithm is a checksum formula used to validate identification numbers, such as credit card numbers.
It checks whether a number is structurally valid by applying a mathematical calculation to its digits.
It is commonly used to detect accidental typing errors.

"""


def luhn_algo_check(card_number):
    digits = [int(digit) for digit in str(card_number)]
    
    # Reverse the digits
    digits.reverse()
    
    total = 0
    
    for i, digit in enumerate(digits):
        
        # Double every second digit
        if i % 2 == 1:
            digit *= 2
            
            #Subtract 9 if the resunt is greater than 9
            if digit > 9:
                digit -= 9
                
                
        total += digit
    
    # Check whether the total is divisible by 10
    return total % 10 == 0    
    
    
number = input("Enter Your Card Number: ")

if number.isdigit() and luhn_algo_check(number):
    print("This is a Valid Number")
else:
    print("This is a Invalid Number")