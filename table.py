from prettytable import PrettyTable
receipt = PrettyTable()
receipt.field_names = ['№','Название продукта', 'Цена','Количество', 'Стоимость',]

print(receipt)