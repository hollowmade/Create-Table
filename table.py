from prettytable import PrettyTable

receipt = PrettyTable()
receipt.field_names = ['№','Название продукта', 'Цена','Количество', 'Стоимость',]

for i in range(3):
    product = input('Укажите название продукта: ')
    price = int(input('Введите цену продукта: '))
    quantity = int(input('Укажите количество продукта: '))
    receipt.add_row([i+1, product, f'{price} руб', f'{quantity} шт', f'{price*quantity} руб.'123])
print(receipt)
