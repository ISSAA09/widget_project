import json


def load_operations():
    """
    Извлекает данные из файла формата JSON
    :return: Список операций
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        raw_json = file.read()
        operations = json.loads(raw_json)
        return operations


def encryption(data_type):
    """
    Шифрование данных карты или счета
    :param data_type: тип данных
    :return: замаскированнй номер карты или счет
    """
    if 'Счет' in data_type.split():
        return data_type[:-20] + '*' * len(data_type[19:-4]) + data_type[-4:]
    else:
        card_number = data_type.split()[-1]
        name_of_card = " ".join(data_type.split()[:-1])
        private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
        chunks, chunk_size = len(private_number), len(private_number) // 4
        return name_of_card + " " + " ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])


def if_executed(data, operations_amount):
    """
    :param data: Список банковских операций
    :param operations_amount: Число операций
    :return: Отсортированные по дате и последние 5 выполненных (EXECUTED) операций
    """
    executed_operations = [operation for operation in data if operation.get('state') == 'EXECUTED']
    sorted_last_operations = sorted(executed_operations, key=lambda x: x.get('date'), reverse=True)
    return sorted_last_operations[:operations_amount]

