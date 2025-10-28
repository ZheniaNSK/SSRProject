from .Candidate import *


# def add_candidate(f):
#     def decorator(*args, **kwargs):
#         print(args, kwargs)
#         f(*args, **kwargs)
#
#     return decorator


class DataBase:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(DataBase, cls).__new__(cls)
        return cls.instance

    def __init__(self, company_name: str):
        self.company_name = company_name
        self.__candidates = list()


    def add_candidate(self, full_name: str, age: int, email: str, status: CandidateStatus = CandidateStatus.NEW):
        self.__candidates.append(Candidate(full_name, age, email, status))




    def __repr__(self):
        return f"Все кандидаты:\n" + "\n".join((f"\t{i};" for i in self.__candidates))
