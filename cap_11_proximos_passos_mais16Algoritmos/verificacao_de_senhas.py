import bcrypt

password = b"senha_secreta"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

if bcrypt.checkpw(password, hashed):
    print("Senha correta")
else:
    print("Senha incorreta")
