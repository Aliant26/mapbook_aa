# definicja prostej struktury danych obejmującej przykładowego użytkownika

users = [
    {"name": "Alicja", "location": "Bugzy Płoskie", "posts": ["Sprzedam Mercedesa",
                                                              "Kupię skrzynię biegów", "Ratunku! Co robić po wypadku?",
                                                              "Kto dzisiaj idzie biegać?"]},
    {"name": "Patrycja", "location": "Krasnosielc", "posts": ["Mój kod nie działa. Pomocy!"]},
    {"name": "Oliwia", "location": "Uciekajka", "posts": ["Czy ktoś zrobił już sprawozdanie z PPyt?"]}
]


def read_users(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']} z miejscowości {user['location']} opublikował post: {user['posts'][-1]}")


def add_user(users_data: list) -> None:
    users_data.append({"name": input("Podaj imię użytkownika: "), "location": input("Podaj miejscowość: "),
                       "posts": ["Dołączyłem do aplikacji!"]})


def remove_user(users_data: list) -> None:
    user_to_remove = input("Kogo chcesz usunąć? ")

    for user in users_data:
        if user["name"] == user_to_remove:
            users.remove(user)

def update_user(users_data: list) -> None:
    user_to_update = input("Podaj imię znajomego do edycji: ")
    for user in users_data:
        if user["name"] == user_to_update:
            user["name"] = input("Podaj nowe imię użytkownika: ")
            user["location"] = input("Podaj nową lokalizację: ")

def update_user_post(users_data: list) -> None:
    user_to_update = input("Podaj imię znajomego do edycji: ")
    for user in users_data:
        if user["name"] == user_to_update:
            user["posts"].append(input("Co słychać? "))

while True:
    print("===============MENU================")
    print("0 - zakończ program")
    print("1 - wyświetl znajomych")
    print("2 - dodanie znajomego")
    print("3 - usuwanie znajomego")
    print("4 - edytowanie znajomego")
    print("5 - edytowanie posta")

    choice = input("Wybierz opcję menu: ")
    print(f"Wybrano opcję {choice}")

    if choice == "0":
        break

    if choice == "1":
        read_users(users)

    if choice == "2":
        add_user(users)

    if choice == "3":
        remove_user(users)

    if choice == "4":
        update_user(users)

    if choice == "5":
        update_user_post(users)