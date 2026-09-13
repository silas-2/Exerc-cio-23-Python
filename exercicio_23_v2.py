"""
Exercício 23 - Categoria de Votação (Versão 2)
Usando operador OR para simplificar a lógica - MAIS ELEGANTE!
"""

idade = int(input("Digite a Idade: "))

if idade < 16:
    print("NÃO PODE VOTAR")
elif idade < 18 or idade > 70:
    print("VOTO OPCIONAL")
else:
    print("VOTO OBRIGATÓRIO")
