A = 5
B = 10

print(f"A: {A}")
print(f"B: {B}")

# X é uma variável auxiliar, que vai servir de balde vazio para armazenar um valor de outra variável
X = A
A = B
B = X

print(f"A: {A}")
print(f"B: {B}")