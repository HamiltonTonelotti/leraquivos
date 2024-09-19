
from pathlib import Path

path=Path('pi_million_digits.txt')
conteudo = path.read_text()

linhas = conteudo.splitlines()
pi_string = ''
for linha in linhas:
    pi_string += linha.strip()
nasc = input("Digite sua data de Nascimento no formato ddmmaa:")
if nasc in pi_string:   
    print("Seu nascimento aparece no primeiro milhao de digitos do pi!:")
else:
    print("Seu nascimento nao aparecera no primeiro milhao do pi!")
