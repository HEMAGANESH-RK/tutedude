import math


number = 25

try:
    
    sqrt_result = math.sqrt(number)
    log_result = math.log(number)
    sine_result = math.sin(number)

 
    print(f"Enter a number: {number}")
    print(f"Square root: {sqrt_result}")
    print(f"logarithm: {log_result}")
    print(f"Sine: {sine_result}")

except ValueError as e:
    print(f"Error: {e}. Please enter a positive number greater than 0 for log and sqrt.")
