import HRDB

company = HRDB.DataBase("hr company")

def help():
    print("""[1] Добавить кандидата
[2] Просмотреть всех кандидатов
[3] Найти кандидата (по ID или ФИО)
[4] Фильтровать по статусу
[5] Редактировать кандидата
[6] Удалить кандидата
[7] Сохранить данные
[8] Загрузить данные
[9] Выход
""")
def add_candidate(*args):
    if len(args):
        company.add_candidate(*args)
    else:
        full_name = input("ФИО: ")
        age = input("Возраст: ")
        email = input("Почта: ")
        status = input("Статус: ")
        company.add_candidate(full_name, age, email, status)

def print_candidates():
    print(company)

def find_candidate():
    pass

def filter_status():
    pass

def edit_candidate():
    pass

def delete_candidate():
    pass

def save_DB():
    pass

def load_DB():
    pass

def exit():
    pass

commands = {
    "help": help,
    "1": add_candidate,
    "2": print_candidates,
    "3": find_candidate,
    "4": filter_status,
    "5": edit_candidate,
    "6": delete_candidate,
    "7": save_DB,
    "8": load_DB,
    "9": exit
}


commands["1"]("Свешникова Анна Александровна", 28, "anna@mail.com", "rejected")
commands["2"]()


def main():
    while True:
        command = input("Выберите действие (1-9): ")
        if command not in commands.keys():
            print(f"Действие \"{command}\" не найдено, введите \"help\" для справки")
        else:
            print('\n' * 10)
            if commands[command]():
                break
            print('\n')


main()