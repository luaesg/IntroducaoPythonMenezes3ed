""" indique os tipos lógicos das operações as seguir """
a = True
b = False
c = True

print(f"{a} and {a}:", a and a) # True
print(f"{b} and {b}:", b and b) # False
print(f"not {c}:", not c) # False
print(f"not {b}:", not b) # True
print(f"not {a}:", not a) # False
print(f"{a} and {b}:", a and b) # False
print(f"{b} and {c}:", b and c) # False
print(f"{a} or {c}:", a or c) # True
print(f"{b} or {c}:", b or c) # True
print(f"{c} or {a}:", c or a) # True
print(f"{c} or {b}:", c or b) #True
print(f"{c} or {c}:", c or c) # True
print(f"{b} or {b}:", b or b) # False

