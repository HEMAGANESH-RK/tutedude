def factorial(n):
    # Calculates factorial using a loop
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Get input from the user
number = int(input("Enter a number: "))

# Call the factorial function and print the result
print(f"Factorial of {number} is: {factorial(number)}")
