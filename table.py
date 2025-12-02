from prettytable import PrettyTable
import matplotlib.pyplot as diagram

receipt = PrettyTable()
receipt.field_names = ['№','Название продукта', 'Цена','Количество', 'Стоимость',]
#Списки для данных диаграммы
products = []
pay = []

for i in range(1):
    product = input('Укажите название продукта: ')
    price = int(input('Введите цену продукта: '))
    quantity = int(input('Укажите количество продукта: '))
    receipt.add_row([i+1, product, f'{price} руб.', f'{quantity} шт.', f'{price*quantity} руб.'])
    products.append(product)
    pay.append(price*quantity)

print(receipt)
#Сборка и вывод диаграммы
diagram.bar(products,
            pay,
            color = 'purple'
            )
diagram.show()
