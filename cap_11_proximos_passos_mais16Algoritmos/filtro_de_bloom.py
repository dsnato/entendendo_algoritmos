from pybloom_live import BloomFilter

# Criar um filtro de Bloom com capacidade para 1000 elementos e taxa de erro de 1%
bloom = BloomFilter(capacity=1000, error_rate=0.01)

# Adicionando elementos ao filtro
bloom.add("teste")
bloom.add("python")

# Verificando a presença de elementos
print("teste" in bloom)  # Deve retornar True
print("python" in bloom)  # Deve retornar True
print("código" in bloom)  # Pode retornar False (se não foi adicionado)
