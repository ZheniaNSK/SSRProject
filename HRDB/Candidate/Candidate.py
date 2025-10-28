from .CandidateStatuses import CandidateStatus



class Candidate:
    def __init__(self, full_name: str, age: int, email: str, status: CandidateStatus):
        if not self.check_validate(full_name, age, email, status):
            raise TypeError("check_validate")

        self.full_name = full_name
        self.age = age
        self.email = email
        self.status = status
        self.__id = 1234567





    @staticmethod
    def check_validate(full_name: str, age: int, email: str, status: CandidateStatus.NEW):
        return (
            isinstance(full_name, str) and
            isinstance(age, int) and
            isinstance(email, str) and
            isinstance(status, CandidateStatus) and
            full_name.count(' ') == 2 and
            0 < age < 100
        )

    def __repr__(self):
        return f"ID: {self.__id} | ФИО: {self.full_name} | Возраст: {self.age} | E-mail: {self.email} | Статус: {self.status.value}"
