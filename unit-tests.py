import main



def test__add_candidate(company, result, *args):
    try:
        return result == company.add_candidate(*args)
    except Exception as e:
        print(f"Возникло исключение в add_candidate:\n{e}")

def test__print_candidates(company, result):
    try:
        return result == str(company)
    except Exception as e:
        print(f"Возникло исключение в print_candidates:\n{e}")

def test__find_candidate(company, result, *args):
    try:
        return result == str(company.get_candidate(*args))
    except Exception as e:
        print(f"Возникло исключение в get_candidate:\n{e}")

def test__find_candidates_by_name(company, result, *args):
    try:
        return result == tuple(map(lambda x: str(x), company.find_candidates_by_name(*args)))
    except Exception as e:
        print(f"Возникло исключение в find_candidates_by_name:\n{e}")

def test__filter_status(company, result, *args):
    try:
        return result == tuple(map(lambda x: str(x), company.find_candidates_by_status(*args)))
    except Exception as e:
        print(f"Возникло исключение в filter_status:\n{e}")

def test__edit_candidate(company, result, *args):
    try:
        return result == company.edit_candidate(*args)
    except Exception as e:
        print(f"Возникло исключение в edit_candidate:\n{e}")

def test__delete_candidate(company, result, *args):
    try:
        return result == company.del_candidate(*args)
    except Exception as e:
        print(f"Возникло исключение в delete_candidate:\n{e}")

def test__save_DB(company, result, *args):
    try:
        return result == company.save_data(*args)
    except Exception as e:
        print(f"Возникло исключение в save_DB:\n{e}")

def test__load_DB(company, result, *args):
    try:
        return result == company.load_data(*args)
    except Exception as e:
        print(f"Возникло исключение в load_DB:\n{e}")


def main_tests():
    company = main.company

    t_c = 0
    t_i = 0

    print(f"test {(t_i:=t_i+1)} {"completed" if (
        test__save_DB(company, True)
    ) and (t_c:=t_c+1) else "failed"}")

    print(f"test {(t_i:=t_i+1)} {"completed" if (
        test__load_DB(company, True)
    ) and (t_c:=t_c+1) else "failed"}")

    print(f"test {(t_i:=t_i+1)} {"completed" if (
        test__print_candidates(company, "Все кандидаты:")
    ) and (t_c:=t_c+1) else "failed"}")

    print(f"test {(t_i:=t_i+1)} {"completed" if (
        test__add_candidate(company, False, "  Иванов иВАН иванович ", "35", "ivan@mail.ru", "funny")
    ) and (t_c:=t_c+1) else "failed"}")

    print(f"test {(t_i:=t_i+1)} {"completed" if (
        test__add_candidate(company, False, "  Иванов иВАН иванович ", 135, "ivan@mail.ru", "rejected")
    ) and (t_c:=t_c+1) else "failed"}")

    print(f"test {(t_i:=t_i+1)} {"completed" if (
        test__add_candidate(company, False, "  Иванов иВАН 3456/*-=; ", "35", "ivan@mail.ru", "rejected")
    ) and (t_c:=t_c+1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__add_candidate(company, True, "  Иванов иВАН иванович ", "25", "ivan@mail.ru", "rejected")
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__add_candidate(company, True, "Пушкин Александр Сергеевич", 20, "  pushkin@mail.com ", main.HRDB.CandidateStatus.NEW)
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__add_candidate(company, True, "Сатторов Евгений Евгеньевич", 16, "evgenijsattorov@gmail.com", "hired")
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__print_candidates(company, """Все кандидаты:
	ID: 1 | ФИО: Иванов Иван Иванович | Возраст: 25 | E-mail: ivan@mail.ru | Статус: rejected;
	ID: 2 | ФИО: Пушкин Александр Сергеевич | Возраст: 20 | E-mail: pushkin@mail.com | Статус: new;
	ID: 3 | ФИО: Сатторов Евгений Евгеньевич | Возраст: 16 | E-mail: evgenijsattorov@gmail.com | Статус: hired;""")
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__find_candidate(company, "ID: 2 | ФИО: Пушкин Александр Сергеевич | Возраст: 20 | E-mail: pushkin@mail.com | Статус: new", 2)
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__find_candidate(company, "None", 20)
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__find_candidates_by_name(company, tuple(['ID: 3 | ФИО: Сатторов Евгений Евгеньевич | Возраст: 16 | E-mail: evgenijsattorov@gmail.com | Статус: hired']), "тторов")
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__find_candidates_by_name(company, tuple(), "тторова")
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__filter_status(company, tuple(['ID: 3 | ФИО: Сатторов Евгений Евгеньевич | Возраст: 16 | E-mail: evgenijsattorov@gmail.com | Статус: hired']), "hired")
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__filter_status(company, tuple(), "interviewed")
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__edit_candidate(company, True, 1, "age", 26)
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__edit_candidate(company, False, 1, "happy", 26)
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__edit_candidate(company, False, 1, "age", "15g")
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__print_candidates(company, """Все кандидаты:
	ID: 1 | ФИО: Иванов Иван Иванович | Возраст: 26 | E-mail: ivan@mail.ru | Статус: rejected;
	ID: 2 | ФИО: Пушкин Александр Сергеевич | Возраст: 20 | E-mail: pushkin@mail.com | Статус: new;
	ID: 3 | ФИО: Сатторов Евгений Евгеньевич | Возраст: 16 | E-mail: evgenijsattorov@gmail.com | Статус: hired;""")
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__save_DB(company, True)
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__delete_candidate(company, True, 2)
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__delete_candidate(company, False, 2)
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__print_candidates(company, """Все кандидаты:
	ID: 1 | ФИО: Иванов Иван Иванович | Возраст: 26 | E-mail: ivan@mail.ru | Статус: rejected;
	ID: 3 | ФИО: Сатторов Евгений Евгеньевич | Возраст: 16 | E-mail: evgenijsattorov@gmail.com | Статус: hired;""")
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__load_DB(company, True)
    ) and (t_c := t_c + 1) else "failed"}")

    print(f"test {(t_i := t_i + 1)} {"completed" if (
        test__print_candidates(company, """Все кандидаты:
	ID: 1 | ФИО: Иванов Иван Иванович | Возраст: 26 | E-mail: ivan@mail.ru | Статус: rejected;
	ID: 2 | ФИО: Пушкин Александр Сергеевич | Возраст: 20 | E-mail: pushkin@mail.com | Статус: new;
	ID: 3 | ФИО: Сатторов Евгений Евгеньевич | Возраст: 16 | E-mail: evgenijsattorov@gmail.com | Статус: hired;""")
    ) and (t_c := t_c + 1) else "failed"}")



    print(f"Всего пройдено тестов {t_c} из {t_i} это {(t_c / t_i * 100):.2f}%")



main_tests()

