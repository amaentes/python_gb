# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите количество монет лежащих гербом "))
m = int(input("Введите количество монет лежащих решкой "))

if n < m:
    print("Нужно перевернуть", n, "монеты лежащие гербом")
elif n == m:
    print("Можно перевернуть или лежащие гербом", n, "монет/ы или монеты лежащие решкой", m, "монет/ы")
else:
    print("Нужно перевернуть", m, "монеты лежащие решкой")
    




