from datetime import datetime
from utils import load_operations
from utils import encryption, if_executed


data = load_operations()

for i in if_executed(data, 5):
    # Перевод формата даты в ДД.ММ.ГГГГ
    dt = " ".join(i['date'].split("T"))
    res_dt = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f').strftime('%d.%m.%Y')
    # если ключ 'from' есть в словаре выводим его значение
    if i.get('from') is not None:
        print(f"{res_dt} {i['description']}")
        print(f"{encryption(i['from'])} -> {encryption(i['to'])}")
        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")
    # если ключа 'from' нет
    else:
        print(f"{res_dt} {i['description']}")
        print(f"{encryption(i['to'])}")
        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")