
def EuclidGCD(a,b):
    if b==0:
        print(a)
        return a
    a_prime = a%b
    return EuclidGCD(b, a_prime)

EuclidGCD(357,234)