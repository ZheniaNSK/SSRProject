from .Candidate import *
from .LoggingErrors import *
from .SaveDB import *


class DataBase:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)

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

            return True
        except Exception as err:
            print(err)
            self.__errors.add_error(err)

            return False

    def del_candidate(self, id: int|str):
        if not self.check_id(id):
            return False

        id = int(id)

        del self.__candidates[id]
        return True

    def get_candidate(self, id: int)->Candidate|None:
        if isinstance(id, int):
            return self.__candidates.get(id, None)
        else:
            err = "id must be int in get_candidate"
            print(err)
            self.__errors.add_error(err)

    def edit_candidate(self, id: int|str, field: str, value):
        if not self.check_id(id):
            return False

        id = int(id)

        if field not in Candidate.fields(None):
            err = f"field not in {Candidate.fields(None)}"
            print(err)
            self.__errors.add_error(err)
            return False

        try:
            Candidate.fields(self.__candidates[id])[field](value)

            return True
        except Exception as err:
            print(err)
            self.__errors.add_error(err)

            return False



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

    def check_id(self, id: int)->bool:
        if not (isinstance(id, int) or (isinstance(id, str) and id.isdigit())):
            err = "id must be int or digit str for delete"
            print(err)
            self.__errors.add_error(err)
            return False

        if int(id) not in self.__candidates.keys():
            err = "id not in candidates for delete"
            print(err)
            self.__errors.add_error(err)
            return False

        return True

    def check_validate(self, **kwargs):
        try:
            Candidate.check_validate(**kwargs)
            return True
        except Exception as err:
            print(err)
            self.__errors.add_error(err)
            return False

    def __repr__(self):
        return f"Все кандидаты:" + "".join((f"\n\t{i};" for i in self.__candidates.values()))
