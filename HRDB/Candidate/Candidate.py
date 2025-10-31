from .CandidateStatuses import CandidateStatus



class Candidate:
    def __init__(self, id: int|str, full_name: str, age: int|str, email: str, status: str|CandidateStatus):
        self.__set_id(id)

        self.set_full_name(full_name)
        self.set_age(age)
        self.set_email(email)
        self.set_status(status)


    def fields(self):
        if not self:
            return ("name", "age", "email", "status")
        return { "name": self.set_full_name, "age": self.set_age, "email": self.set_email, "status": self.set_status }

    def __set_id(self, id: int|str):
        self.__id = self.check_validate(id=id)

    def set_full_name(self, full_name: str):
        self.full_name = self.check_validate(full_name=full_name)

    def set_age(self, age: int|str):
        self.age = self.check_validate(age=age)

    def set_email(self, email: str):
        self.email = self.check_validate(email=email)

    def set_status(self, status: str|CandidateStatus):
        self.status = self.check_validate(status=status)



    @staticmethod
    def check_validate(**kwargs):
        if kwargs.get("id", None) != None:
            if not (isinstance(kwargs["id"], int) or (isinstance(kwargs["id"], str) and kwargs["id"].isdigit())):
                raise TypeError("id must be int or digit str")
            return kwargs["id"]

        elif kwargs.get("full_name", None) != None:
            if not isinstance(kwargs["full_name"], str):
                raise TypeError("full_name must be str")

            kwargs["full_name"] = kwargs["full_name"].strip().title()

            if not kwargs["full_name"].replace('-', '').replace(' ', '').isalpha():
                raise ValueError("full_name must contain only letters or hyphens")

            if kwargs["full_name"].count(' ') != 2:
                raise ValueError("full_name must contain 3 words")

            return kwargs["full_name"]

        elif kwargs.get("age", None) != None:
            if not (isinstance(kwargs["age"], int) or (isinstance(kwargs["age"], str) and kwargs["age"].isdigit() and len(kwargs["age"]))):
                raise TypeError("age must be int or digits str")

            kwargs["age"] = int(kwargs["age"])

            if not (0 < kwargs["age"] < 100):
                raise ValueError("age must be in interval 0 < age < 100")

            return kwargs["age"]

        elif kwargs.get("email", None) != None:
            if not isinstance(kwargs["email"], str) or not len(kwargs["email"]):
                raise TypeError("email must be str")

            return kwargs["email"].strip().lower()

        elif kwargs.get("status", None):
            if not isinstance(kwargs["status"], str|CandidateStatus):
                raise TypeError("status must be str or CandidateStatus")

            if isinstance(kwargs["status"], str):
                kwargs["status"] = kwargs["status"].strip().upper()

                if kwargs["status"] not in map(lambda x: x.name, CandidateStatus):
                    raise ValueError("status not in CandidateStatus")

                kwargs["status"] = CandidateStatus[kwargs["status"]]
            return kwargs["status"]

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
