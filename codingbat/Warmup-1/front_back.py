"""
swap first and last characters
"""

def front_back(str):
    return len(str)>2 and str[-1:]+str[1:-1]+str[:1] or str
