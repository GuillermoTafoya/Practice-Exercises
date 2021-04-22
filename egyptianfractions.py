"""This problem was asked by Palantir.

The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. 
For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction."""


def egyptian_fraction(n):
    getFraction = lambda n: 1/n
    fractions = []
    running_sum = 0
    denominator = 1
    while running_sum != n:
        attemp = getFraction(denominator)
        if running_sum + attemp <= n:
            running_sum += attemp
            fractions.append(f'1/{denominator}')
        else:
            denominator += 1
    string = " + ".join(fractions)
    return string

#print("Pi 1:",egyptian_fraction(3.14159))           # 1/1 + 1/1 + 1/1 + 1/8 + 1/61 + 1/5088 + 1/60618750
#print("Pi 2:",egyptian_fraction(3.14159265359))     # 1/1 + 1/1 + 1/1 + 1/8 + 1/61 + 1/5020 + 1/128538029
print("4/13:",egyptian_fraction(4 / 13))            # 1/4 + 1/18 + 1/468


