def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers

    # Generate Fibonacci sequence up to the nth number
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]  # Calculate the next Fibonacci number
        fib_sequence.append(next_number)

    return fib_sequence

# Test the function
n = int(input("Enter the number of Fibonacci numbers you want to generate: "))
print(fibonacci(n))