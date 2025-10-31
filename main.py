import HRDB
import sys
import os









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
    errmsg = "Ошибка, попробуйте ещё"

    if len(args):
        company.add_candidate(*args)
    else:
        while True:
            full_name = input("Введите ФИО: ")
            if full_name == exit_command: return
            if company.check_validate(full_name=full_name): break
            print(errmsg)
        while True:
            age = input("Введите возраст: ")
            if age == exit_command: return
            if company.check_validate(age=age): break
            print(errmsg)
        while True:
            email = input("Введите почту: ")
            if email == exit_command: return
            if company.check_validate(email=email): break
            print(errmsg)
        while True:
            status = input(f"Введите статус ({", ".join(list(map(lambda x: x.name.lower(), HRDB.CandidateStatus)))}): ").strip()
            if status == exit_command: return

            if not status:
                status = HRDB.CandidateStatus.NEW

            if company.check_validate(status=status): break
            print(errmsg)

        if company.add_candidate(full_name, age, email, status):
            print("Данные успешно записаны")
        else:
            print("Произошла ошибка при записи данных")

def print_candidates(company):
    print(company)

def find_candidate(company):
    output_zero = "🔍 Найдено 0 кандидатов"
    output_above_zero = "🔍 Найдено {} кандидата:"

    find_value = input("Введите имя или ID: ")
    if find_value == exit_command: return

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
    if find_value == exit_command: return

    find = company.find_candidates_by_status(find_value.strip().lower())

    if find and len(find):
        print(output_above_zero.format(len(find)) + "".join((f"\n\t{i};" for i in find)))
    else:
        print(output_zero)

def edit_candidate(company):
    errmsg = "Ошибка, попробуйте ещё"

    while True:
        id = input("Введите id: ")
        if id == exit_command: return
        if company.check_id(id): break
        print(errmsg)
    while True:
        field = input(f"Введите поле для редактирования ({", ".join(HRDB.HRDB.Candidate.fields(None))}): ").strip().lower()
        if field == exit_command: return
        if field in HRDB.HRDB.Candidate.fields(None): break
        print(errmsg)
    while True:
        value = input(f"Введите новое значение: ")
        if value == exit_command: return
        if company.edit_candidate(id, field, value): break
        print(errmsg)

    print("Данные успешно изменены")

def delete_candidate(company, **kwargs):
    errmsg = "Ошибка, попробуйте ещё"

    while True:
        id = input("Введите id: ")
        if id == exit_command: return
        if company.check_id(id) and company.del_candidate(id): break
        print(errmsg)

    print("Данные успешно удалены")



def save_DB(company):
    if company.save_data():
        print("Данные успешно сохранены")
    else:
        print("Произошла ошибка при сохранении данных")


def load_DB(company):
    if company.load_data():
        print("Данные успешно загружены")
    else:
        print("Произошла ошибка при загрузке данных")

def exit(_):
    return True



def main(company):
    os.system("cls")

    while True:
        command = input(main_input_text)
        if command == exit_command: return

        if command not in commands.keys():
            print(f"Действие \"{command}\" не найдено, введите \"help\" для справки")
        else:
            os.system("cls")
            print(main_input_text + command + '\n')
            if commands[command](company):
                return
            print('\n')



exit_command = "exit"
main_input_text = "Выберите действие (1-9): "

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


# commands["1"](company, "Свешникова Анна Александровна", 28, "anna@mail.com", "rejected")
# commands["8"](company)



if __name__ == "__main__":
    main(company)