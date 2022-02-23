import random

número_aleatório = random.randint(0, 10)
número_escolhido = int(input("Escolha um número: "))

if número_escolhido == número_aleatório:
    print("Parabéns você acertou!😁")
else:
    print("Que pena você errou!\N{crying face}")
    print(f"O número sortiado era {número_aleatório}")
