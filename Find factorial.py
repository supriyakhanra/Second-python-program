def factorial(n):
    """Calculates the factorial of a non-negative integer."""

    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Get input from the user
num = int(input("Enter a non-negative integer: "))

# Calculate and print the factorial
print("The factorial of", num, "is", factorial(num))
