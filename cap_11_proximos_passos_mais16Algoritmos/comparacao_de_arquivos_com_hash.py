import hashlib

def file_hash(filename):
    hasher = hashlib.sha256()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

hash1 = file_hash("arquivo1.txt")
hash2 = file_hash("arquivo2.txt")
print(hash1 == hash2)
