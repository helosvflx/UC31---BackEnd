from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

senha = input("Digite uma senha: ")

hash_senha = generate_password_hash(senha)

print("\nHash gerado: ")
print(hash_senha)

tentativa = input("\nDigite novamente a senha: ")

if check_password_hash(hash_senha, tentativa):
    print("Senha correta!")
else:
    print("Senha incorreta!")