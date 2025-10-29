from .CandidateStatuses import CandidateStatus



class Candidate:
    def __init__(self, id: int, full_name: str, age: int|str, email: str, status: str|CandidateStatus):
        self.__set_id(id)

        self.set_full_name(full_name)
        self.set_age(age)
        self.set_email(email)
        self.set_status(status)

    def __set_id(self, id: int):
        if not isinstance(id, int):
            raise TypeError("id must be int")

        self.__id = id

    def set_full_name(self, full_name: str):
        if not isinstance(full_name, str):
            raise TypeError("full_name must be str")

        full_name = full_name.strip().replace("  ", " ").title()

        if full_name.count(' ') != 2:
            raise ValueError("full_name must contain 3 words")

        self.full_name = full_name

    def set_age(self, age: int|str):
        if not isinstance(age, int|str) or (isinstance(age, str) and not age.isdigit()):
            raise TypeError("age must be int or digits str")

        age = int(age)

        if not (0 < age < 100):
            raise ValueError("age must be in interval 0 < age < 100")

        self.age = age

    def set_email(self, email: str):
        if not isinstance(email, str):
            raise TypeError("email must be str")

        email = email.strip().lower()

        self.email = email

    def set_status(self, status: str|CandidateStatus):
        if not isinstance(status, str|CandidateStatus):
            raise TypeError("status must be str or CandidateStatus")

        if isinstance(status, str):
            status = status.strip().upper()

            if status not in map(lambda x: x.name, CandidateStatus):
                raise ValueError("status not in CandidateStatus")

            status = CandidateStatus[status]

        self.status = status

    def __dict__(self):
        return {
            "id": self.__id,
            "full_name": self.full_name,
            "age": self.age,
            "email": self.email,
            "status": self.status.value
        }

    def __repr__(self):
        return f"ID: {self.__id} | ФИО: {self.full_name} | Возраст: {self.age} | E-mail: {self.email} | Статус: {self.status.value}"
