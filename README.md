# Exercício 23 - Categoria de Votação em Python

Exercício 23: Categoria de votação

## 📋 Descrição

Programa em Python que verifica a categoria de votação de uma pessoa de acordo com sua idade, seguindo as regras eleitorais brasileiras.

## 🎯 Objetivo

Dado a idade de uma pessoa, o programa determina se:
- **NÃO PODE VOTAR** → menor de 16 anos
- **VOTO OPCIONAL** → entre 16 e 17 anos, ou maior de 70 anos
- **VOTO OBRIGATÓRIO** → entre 18 e 70 anos (inclusive)

## 💻 Como Usar

1. Execute o programa Python:
```bash
python seu_arquivo.py
```

2. Digite sua idade quando solicitado:
```
Digite a Idade: 25
```

3. O programa exibirá sua categoria de votação:
```
VOTO OBRIGATÓRIO
```

## 📝 Exemplos de Saída

| Idade | Resultado |
|-------|-----------|
| 15    | NÃO PODE VOTAR |
| 16    | VOTO OPCIONAL |
| 17    | VOTO OPCIONAL |
| 25    | VOTO OBRIGATÓRIO |
| 70    | VOTO OBRIGATÓRIO |
| 75    | VOTO OPCIONAL |

## 🔍 Estrutura do Código

```python
idade = int(input("Digite a Idade: "))

if idade < 16:
    print("NÃO PODE VOTAR")
elif idade < 18:
    print("VOTO OPCIONAL")
elif idade <= 70:
    print("VOTO OBRIGATÓRIO")
else:
    print("VOTO OPCIONAL")
```

## 📚 Conceitos Utilizados

- **Entrada de dados**: `input()` e conversão com `int()`
- **Estrutura condicional**: `if`, `elif`, `else`
- **Comparações**: `<`, `<=`
- **Saída de dados**: `print()`

## 🚀 Requisitos

- Python 3.x

## 📖 Referência

Este exercício aborda as regras de votação no Brasil:
- Menores de 16 anos não podem votar
- Entre 16 e 17 anos (inclusive) o voto é opcional
- Entre 18 e 70 anos (inclusive) o voto é obrigatório
- Maiores de 70 anos o voto é opcional
