import random

numero_aleatório = random.randint(0, 10)
numero_escolhido = int(input("Escolha um número: "))

if numero_escolhido == numero_aleatório:
    print("Parabéns você acertou!😁")
else:
    print("Que pena você errou!\N{crying face}")
    print(f"O número sortiado era {numero_aleatório}")
