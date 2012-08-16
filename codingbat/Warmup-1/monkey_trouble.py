def monkey_troube(a_smile, b_smile):
    if (a_smile and b_smile) or (not a_smile and not b_smile):
        return True
    return False

def monkey_trouble(a_smile, b_smile):
    return a_smile==b_smile

print monkey_troube(True, True)
print monkey_troube(True, False)
print monkey_troube(False, True)
print monkey_troube(False, False)
