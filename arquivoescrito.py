from pathlib import Path

conteudo = 'Quintou\n'
conteudo += "Dia de #tbt.\n"
conteudo += "Amanhã é sexta.\n"

caminho = Path('meu_texto.txt')
caminho.write_text(conteudo)