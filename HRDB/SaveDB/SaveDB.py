import os
from json import loads, dumps

from ..Candidate import *

class DB:
    def __init__(self, db_path):
        self.__db_path = db_path

    def load_db(self):
        try:
            if os.access(self.__db_path, os.F_OK):
                file = open(self.__db_path, "r")
                company_name, last_id, candidates = loads(file.read()).values()
                file.close()

                candidates = { int(key): Candidate(
                    value["id"],
                    value["full_name"],
                    value["age"],
                    value["email"],
                    value["status"]
                )
                    for key, value in candidates.items() }

                return company_name, last_id, candidates
        except Exception as e:
            print(f"CRIT ERROR: failed to load data base {self.__db_path}\nMORE LOGS:\n{e}")

            return False


    def save_db(self, company_name, last_id, candidates):
        try:
            file = open(self.__db_path, "w+")

            file.write(dumps(
                {
                    "company_name": company_name,
                    "last_id": last_id,
                    "candidates": { key: value.__dict__() for key, value in candidates.items() }
                },
                indent=4
            ))

            file.close()

            return True
        except Exception as e:
            print(f"CRIT ERROR: failed to save data base {self.__db_path}\nMORE LOGS:\n{e}")

            return False
