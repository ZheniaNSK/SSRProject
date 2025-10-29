import HRDB
import sys









def this_path():
    path_sys_argv = sys.argv[0].replace("/", "\\")

    my_path = ""
    if path_sys_argv.count("\\") > 0:
        my_path = path_sys_argv[:path_sys_argv.rfind("\\") + 1]

    return my_path

def help(_):
    print("""
──────────────────────────────────────────────────────
          🎯 HR-СИСТЕМА: Управление кандидатами
──────────────────────────────────────────────────────

Список действий:
\t[help] Вывести список действий
\t[1] Добавить кандидата
\t[2] Просмотреть всех кандидатов
\t[3] Найти кандидата (по ID или ФИО)
\t[4] Фильтровать по статусу
\t[5] Редактировать кандидата
\t[6] Удалить кандидата
\t[7] Сохранить данные
\t[8] Загрузить данные
\t[9] Выход
""")
def add_candidate(company, *args):
    if len(args):
        company.add_candidate(*args)
    else:
        full_name = input("Введите ФИО: ")
        age = input("Введите возраст: ")
        email = input("Введите почту: ")
        status = input(f"Введите статус ({", ".join(list(map(lambda x: x.name.lower(), HRDB.CandidateStatus)))}): ")
        company.add_candidate(full_name, age, email, status if len(status) else HRDB.CandidateStatus.NEW)

def print_candidates(company):
    print(company)

def find_candidate(company):
    output_zero = "🔍 Найдено 0 кандидатов"
    output_above_zero = "🔍 Найдено {} кандидата:"

    find_value = input("Введите имя или ID: ")

    if find_value.isdigit():
        find = company.get_candidate(int(find_value))

        if find:
            print(f"{output_above_zero.format(1)}\n\t{find}")
        else:
            print(output_zero)
    else:
        find = company.find_candidates_by_name(find_value)

        if find and len(find):
            print(output_above_zero.format(len(find)) + "".join((f"\n\t{i};" for i in find)))
        else:
            print(output_zero)



def filter_status(company):
    output_zero = "🔍 Найдено 0 кандидатов"
    output_above_zero = "🔍 Найдено {} кандидата:"

    find_value = input(f"Введите статус ({", ".join(list(map(lambda x: x.name.lower(), HRDB.CandidateStatus)))}): ")

    find = company.find_candidates_by_status(find_value.strip().lower())

    if find and len(find):
        print(output_above_zero.format(len(find)) + "".join((f"\n\t{i};" for i in find)))
    else:
        print(output_zero)

def edit_candidate(company):
    pass

def delete_candidate(company):
    pass

def save_DB(company):
    company.save_data()

def load_DB(company):
    company.load_data()

def exit(_):
    return True






def main():
    while True:
        command = input("Выберите действие (1-9): ")
        if command not in commands.keys():
            print(f"Действие \"{command}\" не найдено, введите \"help\" для справки")
        else:
            print('\n' * 5)
            if commands[command](company):
                break
            print('\n')





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

errors_path = f"{this_path()}errors.log"
db_path = f"{this_path()}DB.json"

company = HRDB.DataBase("hr company", db_path, errors_path)



commands["1"](company, "Свешникова Анна Александровна", 28, "anna@mail.com", "rejected")
commands["2"](company)



main()