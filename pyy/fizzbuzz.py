"""
FizzBuzz
Реализуйте функцию, которая принимает на вход начало и конец
полуинтервала и выводит для каждого числа в нем в отдельную строку
- fizz, если число делится на 3, но не на 5
- buzz, если число делится на 5, но не на 3
- fizzbuzz, если число делится на 15
- само число иначе
Например, fizzbuzz(11, 16) должен вывести
11
fizz
13
14
fizzbuzz
"""


def fizzbuzz(a: int, b: int):
    for i in range(a,b):
        if i%15==0:
            print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)


#fizzbuzz(11,16)