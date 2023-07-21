""" Identifique os tipos lógicos das operações a seguir """
a = 4
b = 10
c = 5.0
d = 1
f = 5

print(f"{a} == {c} é", a == c) # falso
print(f"{a} < {b} é", a < b) # verdadeiro
print(f"{d} > {b} é", d > b) # falso
print(f"{c} != {f} é", c != f) # falso
print(f"{a} == {b} é", a == b) # falso
print(f"{c} < {d} é", c < d) # falso
print(f"{b} > {a} é", b > a) # verdadeiro
print(f"{c} >= {f} é", c >= f) # verdadeiro
print(f"{f} >= {c} é", f >= c) # verdadeiro
print(f"{c} <= {c} é", c <= c) # verdadeiro
print(f"{c} <= {f} é", c <= f) # verdadeiro 
