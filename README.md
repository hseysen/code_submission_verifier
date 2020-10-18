# Code Submission Verifier

The main module is `Verification.py`, and the other two python scripts are just for testing whether or not the module works. You don't need any special packages/modules for this to work, only requires built-in features of Python.

## How to use Verification.py

1. Write this line in your imports:
```python
from Verification import CodeSaver, CodeValidation
```
2. Have your code to be tested ready in a string variable.
3. Make a `CodeSaver` object to hold your code.
4. Use the `.save_code()` method to save the code in a new Python file.
5. Now you need to import the file created with the following line:
```python
user_defined_func = __import__(f"{code_saver.file_name}").__getattribute__("f")
```
Here, `"f"` is the name of the function you want to validate against input and output data. This line imports that function to the variable `user_defined_func`
6. You can delete the file to free up storage space if you wish:
```python
code_saver.delete_file()
```
7. Next, create a `CodeValidation` object, and feed it input and output data in a form of list of tuples. (Can be seen on `correct_submission.py` or `incorrect_submission.py`), and your function to be validated.
8. Now running the `.validate()` method will return `True` or `False` depending on the submission correctness against the input-output data.

## TODO
* Abstract the above process to make the module more user-friendly.
* Check the code in order to avoid risk of attacks to the system from code submissions. In simple words, if the code submission is ***something like*** the following, it may cause problems in an online system:
```python
import os
os.rmdir(r"C:\Windows")
```
* Add a timeout feature to validation process (preferably ~5 seconds max)
* Rather than a dry `True`/`False` response, make the judge actually check how many of the tests did the code pass, and how well it did in terms of time management.
