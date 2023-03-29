"""
Игра "Быки и коровы"

Компьютер загадывает строку из n цифр.
Каждый ход игрок вводит догадку - тоже строку из n цифр, и получает в ответ
- количество "быков" - верно угаданных цифр на своих позициях
- количество "коров" - верно угаданных цифр, поставленных на неверные позиции

Например, при загаданной строке "4271" и догадке "1234" есть
- 1 бык - цифра "2" на второй позиции
- 2 коровы - цифры "1" и "4"

Реализуйте вспомогательные функции для этой игры:
- [a] create_secret, score, validate
- [b] computer
- [*] сделайте так, чтобы игрок-компьютер опирался на результаты
  предыдущих ходов и пытался делать основанные на них ходы
    > вам придется заметно изменить структуру игры, чтобы
      иметь возможность сообщать игроку результаты по-разному
      в зависимости от того, человек это или компьютер
"""
import copy
from typing import Callable
import random

def create_secret(n: int) -> str:
    """
    Функция принимает длину загадываемого числа
    и возвращает случайную строку из цифр указанной длины
    """
    s=''
    for i in range(n):
        s=s+str(random.randint(0,9))
    return s


def score(secret: str, guess: str) -> tuple[int, int]:
    """
    Функция принимает загаданную строку и догадку игрока
    и возвращает пару из количества "быков" и количества "коров"
        > можно для каждой цифры от '0' до '9' посмотреть на позиции
          ее вхождения в secret и guess
        > для нахождения числа общих позиций может быть полезно
          воспользоваться структурой данных "множество" (set)
    """
    bulls=0
    cows=0
    #print(secret)
    secret2=list(secret)
    guess2=list(guess)
    for i in range(len(secret)):
        if secret[i]==guess[i]:
            bulls+=1
            secret2.remove(secret[i])
            guess2.remove(secret[i])
    guess1=set(guess)
    secret1=set(secret2)
    for i in secret2:
        if guess2.__contains__(i):
            cows+=1
            guess2.remove(i)
    #cows=cows-bulls
    return bulls, cows


def validate(n: int, guess: str) -> bool:
    """
    Функция принимает параметр игры - длину загаданной строки, и догадку игрока
    и возвращает, правда ли игрок ввел корректную догадку (строку длины n из цифр)
    """
    flag=True
    if (len(guess)!=n):
        flag=False
    else:
        for i in guess:
            if (i<'0' or i>'9'):
                flag=False
    return flag


def computer_player(n: int) -> Callable:
    """
    Функция принимает параметр игры - длину загаданной строки,
    и возвращает ФУНКЦИЮ, генерирующую догадки
    """

    def guess():
        s=''
        for i in range(n):
            s=s+str(random.randint(0,9))
        return s

    return guess


def real_player(n: int) -> Callable:
    """
    Функция принимает параметр игры - длину загаданной строки,
    и возвращает ФУНКЦИЮ, получающую догадку от реального игрока
    """
    print(f'The secret word has length {n}')
    def input1():

        s=input()
        return s
    return input1


def play(n: int, player: Callable):
    """
    Функция реализует процесс игры с заданной длиной слова и игроком
    """
    secret = create_secret(n)
    attempts = 0
    while True:
        guess = player()
        attempts += 1
        if not validate(n, guess):
            print(f'Your guess should be a string of {n} digits')
            continue
        bulls, cows = score(secret, guess)
        if bulls == n:
            print(f'Correct! You\'ve won in {attempts} guesses')
            break
        else:
            print(f'Your guess has {bulls=} and {cows=}')


if __name__ == '__main__':
    n = 4
    play(n, real_player(n))