"""
Description:
Count the number of prime numbers less than a non-negative number, n
"""
def countPrimes(n):
    if n < 3:
        # 2 is the smallest prime number
        return 0
    counts = [1]*n
    for i in range(4,n,2):
        # elimate the even number
        counts[i] = 0
    for i in range(3,n,2):
        if counts[i]:
            j = 3
            while i * j < n:
                counts[i * j] = 0
                j += 2
    return sum(counts[2:])






if __name__ == "__main__":
    print countPrimes(123213)






