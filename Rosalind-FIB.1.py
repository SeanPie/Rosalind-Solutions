n = 5

def factorial_recurrence(n):
    if n == 0:
        return 1
    # Factorial: n! = n * (n - 1)!
    return n * factorial_recurrence(n-1)

print (factorial_recurrence(n))