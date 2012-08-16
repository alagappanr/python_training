"""
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative. 

pos_neg(1, -1, False)  True
pos_neg(-1, 1, False)  True
pos_neg(-4, -5, True)  True
"""

def pos_neg(a, b, negative):
    if negative:
        return a<0 and b<0
    if (a<0 and b>0) or (b<0 and a>0):
        return True
    return False


print pos_neg(1, -1, False)
print pos_neg(-1, 1, False)
print pos_neg(-1, 1, False)
print pos_neg(-1, -1, False)
print pos_neg(-1, -1, True)
print pos_neg(1, 1, True)
print pos_neg(1, -1, True)
print pos_neg(-1, 1, True)
