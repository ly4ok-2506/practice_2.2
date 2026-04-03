import requests

urls = [
    "https://github.com/",
    "https://www.binance.com/en",
    "https://tomtit.tomsk.ru/",
    "https://jsonplaceholder.typicode.com/",
    "https://moodle.tomtit-tomsk.ru/"
]

print("Результаты проверки:")
print("-" * 60)

for url in urls:
    try:
        response = requests.get(url)
        code = response.status_code

        if code == 200:
            status = "доступен"
        elif code == 403:
            status = "вход запрещен"
        elif code == 404:
            status = "не найден"
        else:
            status = "не доступен"

        print(f"{url} – {status} – {code}")

    except:
        print(f"{url} – не доступен – ошибка")