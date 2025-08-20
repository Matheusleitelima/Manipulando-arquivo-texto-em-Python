# Captura de dados
frases = []
print("Digite frases (digite 'sair' para encerrar):")

while True:
    entrada = input("> ")
    if entrada.lower() == "sair":
        break
    frases.append(entrada)

# Criação e armazenamento no arquivo
with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
    for frase in frases:
        arquivo.write(frase + "\n")

# Leitura e manipulação (convertendo para maiúsculas)
with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
    dados_modificados = [linha.strip().upper() for linha in arquivo] #strip: Tira os espaços Upper: Deixa as letras em maisculas

# Sobrescrita do arquivo
with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
    for linha in dados_modificados:
        arquivo.write(linha + "\n")

print("✅ Arquivo sobrescrito com o texto em maiúsculas.")
