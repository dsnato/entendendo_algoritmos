import random

P = 23  # Número primo
G = 5   # Gerador

# Chave privada
a = random.randint(1, P-1)
b = random.randint(1, P-1)

# Chave pública
A = (G**a) % P
B = (G**b) % P

# Chave secreta compartilhada
shared_a = (B**a) % P
shared_b = (A**b) % P

print(shared_a == shared_b)  # Devem ser iguais
