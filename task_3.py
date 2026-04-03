import requests
import json
import os

FILE_NAME = "save.json"


def load_groups():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_groups(groups):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(groups, f, indent=4, ensure_ascii=False)


def get_rates():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()
    return data["Valute"]


def show_all(rates):
    print("\nВсе валюты:")
    for code, info in rates.items():
        print(f"  {code} - {info['Name']}: {info['Value']} руб.")


def show_one(rates, code):
    if code in rates:
        info = rates[code]
        print(f"\n{code} - {info['Name']}: {info['Value']} руб.")
    else:
        print(f"\nВалюта {code} не найдена")


def create_group(groups):
    name = input("Введите название группы: ")
    if name in groups:
        print("Такая группа уже есть")
    else:
        groups[name] = []
        save_groups(groups)
        print(f"Группа '{name}' создана")


def add_currency(groups, rates):
    name = input("Введите название группы: ")
    if name not in groups:
        print("Группа не найдена")
        return

    code = input("Введите код валюты (USD, EUR и т.д.): ").upper()
    if code not in rates:
        print("Такой валюты нет")
        return

    if code in groups[name]:
        print("Валюта уже в группе")
    else:
        groups[name].append(code)
        save_groups(groups)
        print(f"Валюта {code} добавлена в группу '{name}'")


def remove_currency(groups):
    name = input("Введите название группы: ")
    if name not in groups:
        print("Группа не найдена")
        return

    print(f"Валюты в группе: {groups[name]}")
    code = input("Введите код валюты для удаления: ").upper()

    if code in groups[name]:
        groups[name].remove(code)
        save_groups(groups)
        print(f"Валюта {code} удалена")
    else:
        print("Такой валюты нет в группе")


def show_groups(groups):
    if not groups:
        print("\nНет сохраненных групп")
    else:
        print("\nВаши группы:")
        for name, currencies in groups.items():
            print(f"  {name}: {currencies}")


def main():
    groups = load_groups()
    rates = get_rates()

    while True:
        print("\n" + "=" * 40)
        print("КУРС ВАЛЮТ")
        print("=" * 40)
        print("1 - Все валюты")
        print("2 - Найти валюту по коду")
        print("3 - Создать группу")
        print("4 - Добавить валюту в группу")
        print("5 - Удалить валюту из группы")
        print("6 - Показать все группы")
        print("7 - Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_all(rates)
        elif choice == "2":
            code = input("Введите код валюты: ").upper()
            show_one(rates, code)
        elif choice == "3":
            create_group(groups)
        elif choice == "4":
            add_currency(groups, rates)
        elif choice == "5":
            remove_currency(groups)
        elif choice == "6":
            show_groups(groups)
        elif choice == "7":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова")


main()