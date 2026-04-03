import requests

def show_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 404:
        print("Пользователь не найден")
        return

    data = response.json()

    print("\n" + "=" * 40)
    print("ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ")
    print("=" * 40)
    print(f"Имя: {data.get('name', 'Не указано')}")
    print(f"Ссылка на профиль: {data['html_url']}")
    print(f"Количество репозиториев: {data['public_repos']}")
    print(f"Количество обсуждений (Gists): {data['public_gists']}")
    print(f"Количество подписок: {data['following']}")
    print(f"Количество подписчиков: {data['followers']}")

def show_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 404:
        print("Пользователь не найден")
        return

    repos = response.json()

    print("\n" + "=" * 40)
    print(f"РЕПОЗИТОРИИ ПОЛЬЗОВАТЕЛЯ: {username}")
    print("=" * 40)

    for repo in repos:
        print(f"\nНазвание: {repo['name']}")
        print(f"Ссылка: {repo['html_url']}")
        print(f"Просмотры: {repo['watchers_count']}")
        print(f"Язык: {repo.get('language', 'Не указан')}")
        print(f"Видимость: {repo['visibility']}")
        print(f"Ветка по умолчанию: {repo['default_branch']}")
        print("-" * 30)

def search_repos(query):
    url = "https://api.github.com/search/repositories"
    params = {"q": query}
    response = requests.get(url, params=params)

    data = response.json()

    print("\n" + "=" * 40)
    print(f"РЕЗУЛЬТАТЫ ПОИСКА: {query}")
    print("=" * 40)

    for repo in data.get("items", [])[:5]:
        print(f"\nНазвание: {repo['name']}")
        print(f"Ссылка: {repo['html_url']}")
        print(f"Владелец: {repo['owner']['login']}")
        print("-" * 30)

def main():
    while True:
        print("\n" + "=" * 40)
        print("GITHUB API КЛИЕНТ")
        print("=" * 40)
        print("1 - Просмотр профиля")
        print("2 - Список репозиториев")
        print("3 - Поиск репозиториев")
        print("4 - Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя пользователя GitHub: ")
            show_profile(name)
        elif choice == "2":
            name = input("Введите имя пользователя GitHub: ")
            show_repos(name)
        elif choice == "3":
            query = input("Введите название для поиска: ")
            search_repos(query)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор")

main()