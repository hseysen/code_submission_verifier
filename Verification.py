import random
import string
import os


class CodeValidation:
    def __init__(self, idata, odata, func):
        self.idata = idata
        self.odata = odata
        self.func = func

    def validate(self):
        for i, o in zip(self.idata, self.odata):
            if self.func(*i) != o:
                return False
        return True


class CodeSaver:
    def __init__(self, user_code):
        self.user_code = user_code
        self.file_name = self.gen_rand_name()

    @staticmethod
    def gen_rand_name():
        letters = "".join([random.choice(string.ascii_letters) for i in range(5)] +
                          [random.choice(string.ascii_letters + string.digits) for i in range(15)])
        return letters

    def save_code(self):
        with open(f"{self.file_name}.py", "w") as wf:
            wf.write(self.user_code)

    def delete_file(self):
        os.remove(f"{self.file_name}.py")
