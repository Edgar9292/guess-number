from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Muito Alto.")
    return turns - 1
  elif guess < answer:
    print("Muito Baixo.")
    return turns - 1
  else:
    print(f"Parabéns!! A resposta é: {answer}.")

def set_difficulty():
  level = input("Escolha a Dificuldade: 'Fácil' ou 'Difícil' ")
  if level == "facil":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def game():
  print("Bem-Vindo ao Jogo da Adivinhação do Número!")
  print("Escolha um número de 1 a 100 e Boa Sorte!")
  answer = randint(1, 100)

  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"Você Tem {turns} Tentativas Faltando para Adivinhar o Número.")


    guess = int(input("Dê Seu Palpite: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("Fim das Tentativas. Você Perdeu!")
      return
    elif guess != answer:
      print("Tente de Novo.")


game()