def parrot_trouble(talking, hour):
    return (hour<7 or hour>20) and talking


print parrot_trouble(True, 6)
print parrot_trouble(True, 7)
print parrot_trouble(False, 6)
print parrot_trouble(True, 22)
