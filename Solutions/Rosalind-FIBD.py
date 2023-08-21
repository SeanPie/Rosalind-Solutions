n = 6 # Number of months
m = 3 # Number of months all rabbits live for

def fibonacci_recurrence(n, m):
    F = [1] * (n+1)
    F[1] = 1

    for i in range(2, n+1):
            F[i] = F[i-1] + (F[i-2]) - (F[i-(m)] if i >= m else 0)

    return F[n]

print(fibonacci_recurrence(6,3))