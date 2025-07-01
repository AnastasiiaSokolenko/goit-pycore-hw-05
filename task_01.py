def caching_fibonacci():
    """
    Returns a fibonacci(n) function which computes the nth Fibonacci number
    using recursion and caches computed results for efficiency.
    """
    cache = {}

    def fibonacci(n):
        """
        Recursively computes the nth Fibonacci number.
        Uses caching to avoid repeated calculations.

        Parameters:
            n (int): The index of the Fibonacci number to compute.

        Returns:
            int: The nth Fibonacci number.
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        # Recursively compute and store in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci



# ======= Usage Example =======

if __name__ == "__main__":
    # Get the fibonacci function
    fib = caching_fibonacci()

    # Use the fibonacci function to calculate Fibonacci numbers
    print(fib(10))  # Outputs 55
    print(fib(15))  # Outputs 610