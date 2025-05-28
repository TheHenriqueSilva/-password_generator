import random
import string

senha_gerada = () 


def gerador_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha


    senha_gerada = gerador_senha(12)
    print(senha_gerada) 

print(gerador_senha(12))  # Chama a função para gerar uma senha de comprimento 12
    
      