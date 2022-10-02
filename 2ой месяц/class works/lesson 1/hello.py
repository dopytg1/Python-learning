import time


userAnswer = input("Введите любое число:")

i = 3

while i > 0:
    print("Обработка данных....")
    time.sleep(1)
    i -= 1


print('Сессия завершена. Я устал твое число ' + userAnswer)

# print(int(userAnswer) + 1)