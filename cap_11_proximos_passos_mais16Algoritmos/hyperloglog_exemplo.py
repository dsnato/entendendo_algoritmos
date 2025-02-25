from hyperloglog import HyperLogLog

# Criar um HyperLogLog com precisão 0.01
hll = HyperLogLog(0.01)

# Adicionando elementos ao estimador
hll.add("python")
hll.add("código")
hll.add("dados")
hll.add("python")  # Elemento repetido

# Estimativa do número de elementos únicos
print(f"Estimativa de elementos únicos: {len(hll)}")
