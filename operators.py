# In python Expression is anything that can be calculated to return a value.

a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a ** b)   # 1728
print(a // b)   # 4 integer division, rounded down towards minus infinity
print(a % b)    # 0 modulo: the remainder after integer division

print()

# by adding two // we coverted float to integer and performed integer division
for i in range(2, a // b):
    print(i)

print()

# Excercise:

bun_price = 2.40
money = 15
print(money // bun_price)


# Math operations:
print(a + b / 3 * 12)
print(a+(b / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)
