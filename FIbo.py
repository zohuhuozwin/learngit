# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
c = int(input("give a num:"))
while a < c:
    print(a)
    a, b = b, a+b
