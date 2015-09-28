def print_prime(n):
    for i in range(2,n):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print '{0} is a prime number'.format(str(i))
print_prime(18)


