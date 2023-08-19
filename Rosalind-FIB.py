# Read more about dynamic programming

n = 5
k = 3

def fibonacci_recurrence(n, k):
    F = [0] * (n+1)
    F[1] = F[2] = 1

    for i in range(3, n + 1):
        F[i] = F[i -1] + (k * F[i-2])

    return F[n]

print (fibonacci_recurrence(n, k))