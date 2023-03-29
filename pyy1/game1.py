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
print('сколько цифр будет в вашем числе? ')
from typing import Callable


def create_secret(n: int) -> str:
    """
    Функция принимает длину загадываемого числа
    и возвращает случайную строку из цифр указанной длины
    """
    from random import choice
    z = '0123456789'
    secret = choice(z)  # Создаём строку x из одного случайно выбранного символа из z
    for i in range(n - 1):  # В цикле из n повторений
        secret += choice(z)  # добавляем к строке x случайно выбранные символы из строки z
    return (secret)
def score(secret, dogadka) -> tuple[int, int]:
    """
    Функция принимает загаданную строку и догадку игрока
    и возвращает пару из количества "быков" и количества "коров"
        > можно для каждой цифры от '0' до '9' посмотреть на позиции
          ее вхождения в secret и guess
        > для нахождения числа общих позиций может быть полезно
          воспользоваться структурой данных "множество" (set)
    """
    b = list(map(int, str(secret)))
    a = list(map(int, str(dogadka)))
    bulls = 0
    cows = 0
    i = 0
    for a[i] in a:
        if a[i - 1] == b[i - 1]:
            bulls += 1
        elif a[i - 1] in b:
            cows += 1
        i += 1
    return (bulls, cows)
def validate(n: int, guess: str) -> bool:
    """
    Функция принимает параметр игры - длину загаданной строки, и догадку игрока
    и возвращает, правда ли игрок ввел корректную догадку (строку длины n из цифр)
    """
    zn = [str(i) for i in range(10)]
    if len(guess) == n:
        for i in range(len(guess)):
            if guess[i] not in zn:
                return False
        return True
    else:
        return False
def computer_player(n: int) -> Callable:
    """
    Функция принимает параметр игры - длину загаданной строки,
    и возвращает ФУНКЦИЮ, генерирующую догадки
    """

    def guess():
        from random import choice
        z = '0123456789'
        variant = choice(z)  # Создаём строку x из одного случайно выбранного символа из z
        for i in range(len_ - 1):  # В цикле из len_ повторений
            secret += choice(z)  # добавляем к строке x случайно выбранные символы из строки z
        return (secret)

    return guess


def real_player(n: int) -> Callable:
    """
    Функция принимает параметр игры - длину загаданной строки,
    и возвращает ФУНКЦИЮ, получающую догадку от реального игрока
    """
    print(f'The secret word has length {n}')
    return input


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















