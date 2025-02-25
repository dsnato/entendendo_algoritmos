from datasketch import MinHash

m1, m2 = MinHash(), MinHash()
for d in "minhash exemplo".split():
    m1.update(d.encode('utf8'))
for d in "minhash teste".split():
    m2.update(d.encode('utf8'))

print(m1.jaccard(m2))
