"""
Exercício 23 - Categoria de Votação (Versão 1)
Usando múltiplos elif para cada faixa etária
"""

idade = int(input("Digite a Idade: "))

if idade < 16:
    print("NÃO PODE VOTAR")
elif idade < 18:
    print("VOTO OPCIONAL")
elif idade <= 70:
    print("VOTO OBRIGATÓRIO")
else:
    print("VOTO OPCIONAL")
