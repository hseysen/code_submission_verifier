import Verification


def main():
    submission = """
def add_and_subtract(x, y):
    return x + y, x - y
    """

    code_saver = Verification.CodeSaver(submission)
    code_saver.save_code()

    user_defined_func = __import__(f"{code_saver.file_name}").__getattribute__("add_and_subtract")
    test_case_idata = [(5, 4), (6, 9), (3, 10), (7, 8), (22, 1)]
    test_case_odata = [(9, 1), (15, -3), (13, -7), (15, -1), (23, 21)]

    code_saver.delete_file()

    code_validator = Verification.CodeValidation(test_case_idata, test_case_odata, user_defined_func)
    print(code_validator.validate())


if __name__ == "__main__":
    main()
