import time
import os

products = []
amounts = []
prices = []

while True:
    product = input("Что вы купили?: ")
    amount = input("Количество товара(шт, кг, гр...)?: ")
    price = int(input("Цена вашего товара?: "))

    products.append(product)
    amounts.append(amount)
    prices.append(price)

    print("Есть ли еще что-то что вы купили?")
    exitFlag = False

    for i in range(1):
        confirm = input("Если да то наберите 1, если нет то 0: ")
        if confirm == "0":
            exitFlag = True
            break
        elif confirm == "1":
            continue
        else:
            print("Число неправильное. Попробуйте снова ")
            continue

    if(exitFlag):
        break

    

total = 0
i = 3

while i > 0:
    print("Обработка данных....")
    time.sleep(1)
    i -= 1

if len(prices) >= 2:
    os.system('CLS')
    total = sum(prices)
    print("ваш товар: " + ", ".join(products))
    print("количество: " + ", ".join(amounts))
    print("Общая сумма: " + str(total))
else:
    os.system('CLS')
    print("ваш товар: " + ", ".join(products))
    print("количество: " + ", ".join(amounts))
    print("Цена: " + str(prices[0]))