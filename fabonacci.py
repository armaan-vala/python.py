# Get the number of terms from the user
num_terms = int(input("Enter the number of Fibonacci terms: "))

# Initialize the first two terms
fibonacci_series = [0, 1]

                                        #gen
for i in range(2, num_terms):
    next_fib = fibonacci_series[i - 1] + fibonacci_series[i - 2]
    fibonacci_series.append(next_fib)

print("Fibonacci series:")
for term in fibonacci_series:
    print(term, end=" ")
