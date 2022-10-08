#Program optimize for prime number
def prime_numbers(n):
    result=[2]
    if n<2:
        return False
    for i in range(3,n,2):
        if (n%i)==0:
            return False
        else:
            result.append(i)
    return result

def sum_prime_numbers(n):
    return sum(prime_numbers(n))