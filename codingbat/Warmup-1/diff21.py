def diff21(n):
    return n>21 and 2*abs(n-21) or abs(n-21)

print diff21(10)
print diff21(19)
print diff21(21)
print diff21(31)
