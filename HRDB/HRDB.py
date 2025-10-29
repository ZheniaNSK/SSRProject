from .Candidate import *
from .LoggingErrors import *
from .SaveDB import *


class DataBase:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(DataBase, cls).__new__(cls)

        return cls.instance

    def __init__(self, company_name: str, db_path: str, errors_path: str):
        self.company_name = company_name

        self.__db = DB(db_path)
        self.__errors = Errors(errors_path)

        self.__candidates = dict()
        self.__last_id = 1


    def add_candidate(self, full_name: str, age: int|str, email: str, status: CandidateStatus|str):
        try:
            self.__candidates[self.__last_id] = Candidate(self.__last_id, full_name, age, email, status)
            self.__last_id += 1
        except Exception as e:
            print(e)
            self.__errors.add_error(e)

    def get_candidate(self, id: int)->Candidate|None:
        if isinstance(id, int):
            return self.__candidates.get(id, None)
        else:
            err = "id must be int in get_candidate"
            print(err)
            self.__errors.add_error(err)

    def find_candidates_by_name(self, name: str):
        if isinstance(name, str):
            return tuple(i for i in self.__candidates.values() if name in i.full_name.lower())
        else:
            err = "name must be str in find_candidates"
            print(err)
            self.__errors.add_error(err)

    def find_candidates_by_status(self, status: CandidateStatus|str):
        if isinstance(status, CandidateStatus|str):
            if isinstance(status, str):
                status = status.strip().upper()

                if status not in map(lambda x: x.name, CandidateStatus):
                    err = "status not in CandidateStatus"
                    print(err)
                    self.__errors.add_error(err)
                else:
                    status = CandidateStatus[status]

                    return tuple(i for i in self.__candidates.values() if status == i.status)
        else:
            err = "name must be str in find_candidates"
            print(err)
            self.__errors.add_error(err)

    def save_data(self):
        self.__db.save_db(self.company_name, self.__last_id, self.__candidates)

        self.__errors.save_errors()

    def load_data(self):
        data = self.__db.load_db()

        if data:
            self.company_name, self.__last_id, self.__candidates = data
            self.__errors.clear()
            return True

        return False


    def __repr__(self):
        return f"Все кандидаты:" + "".join((f"\n\t{i};" for i in self.__candidates.values()))
