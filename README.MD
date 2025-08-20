# 📂 Manipulando Arquivo-Texto em Python

Manipular arquivos de texto em Python permite automatizar tarefas rotineiras, como leitura, escrita e processamento de dados. Essa prática é essencial no desenvolvimento de **scripts que gerenciam logs, processam grandes volumes de dados ou geram relatórios**.  

Além disso, compreender como manipular arquivos eficientemente contribui para criar aplicações mais **robustas e escaláveis**, garantindo melhor organização das informações.

---

## 🎯 Situação-Problema

Uma **editora** recebe frequentemente textos de autores que contêm inconsistências no uso de **maiúsculas e minúsculas**, dificultando o processo de revisão.  

O desafio é criar um **programa em Python** que:  
1. Capture trechos de texto digitados pelo editor.  
2. Salve-os em um arquivo (`meu_arquivo.txt`).  
3. Leia o conteúdo e converta todo o texto para **maiúsculas**.  
4. Sobrescreva o arquivo original com o texto padronizado.  

---

## 🚀 Objetivo

Facilitar a **revisão preliminar** dos textos antes da edição final, garantindo que o material esteja formatado de forma consistente.

---

## 🛠️ Passos do Programa

### 1️⃣ Captura de dados
- Solicita ao usuário que digite frases ou parágrafos.  
- O processo continua até que o usuário digite **`sair`**.  
- As entradas são armazenadas em uma lista.

### 2️⃣ Criação e armazenamento
- As frases digitadas são salvas no arquivo `meu_arquivo.txt`.  
- Cada frase é gravada em uma nova linha.

### 3️⃣ Manipulação do arquivo
- O arquivo é aberto no modo de leitura.  
- O conteúdo é convertido para **maiúsculas**.  
- As linhas modificadas são armazenadas em uma nova lista.

### 4️⃣ Sobrescrita do arquivo
- O arquivo `meu_arquivo.txt` é reaberto no modo escrita.  
- O conteúdo convertido é salvo, substituindo o texto original.

### 5️⃣ Confirmação
- Exibe mensagem informando que o arquivo foi atualizado com sucesso.

---

## 💻 Exemplo de Código (Python 3.8.1)

```python
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
    dados_modificados = [linha.strip().upper() for linha in arquivo]  # strip: remove espaços extras / upper: converte em maiúsculas

# Sobrescrita do arquivo
with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
    for linha in dados_modificados:
        arquivo.write(linha + "\n")

print("✅ Arquivo sobrescrito com o texto em maiúsculas.")
