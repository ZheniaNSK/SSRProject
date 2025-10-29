from datetime import datetime
import os



class Errors:
    def __init__(self, errors_path):
        self.__errors_path = errors_path
        self.__errors = list()

    def add_error(self, err: str|Exception):
        self.__errors.append(f"{datetime.now()} : {err}")

    def save_errors(self):
        try:
            prev_text = ""

            if os.access(self.__errors_path, os.F_OK):
                file = open(self.__errors_path, "r")
                prev_text = file.read()
                file.close()

            file = open(self.__errors_path, "w+")
            file.write(prev_text + "\n".join(self.__errors) + '\n')
            file.close()

            self.clear()
        except Exception as e:
            print(f"CRIT ERROR: no access to the file {self.__errors_path}\nMORE LOGS:\n{e}")

    def clear(self):
        self.__errors.clear()