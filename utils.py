import random
import string

def generate_random_name(file_name):
    file_name = file_name.split(".")
    file_extension = file_name[len(file_name) - 1]
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10)) + "." + file_extension
