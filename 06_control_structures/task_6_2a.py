# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите IP а формате 10.0.1.1: ").split(".")

correct = True

if len(ip) != 4:
    correct = False

for oct in ip:
    if not oct.isdigit():
        correct = False
        break
    if int(oct) < 0 or int(oct) > 255:
        correct = False
        break


if correct:
    if 0 < int(ip[0]) and int(ip[0]) < 224:
        print("unicast")
    elif 223 < int(ip[0]) and int(ip[0]) < 239:
        print("multicast")
    elif ip == ["255", "255", "255", "255"]:
        print("local broadcast")
    elif ip == ["0", "0", "0", "0"]:
        print("unassigned")
    else:
        print("unused")
else:
    print("Неправильный IP-адрес")