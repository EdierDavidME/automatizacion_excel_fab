import os
import re


class Validations:
    def __init__(self):
        pass

    def is_empty(self, value):
        if value == "None" or value == None or value == "" or value == " " or len(re.sub(r"\s+", "", str(value))) == 0:
            return True
        else:
            return False

    def is_file(self, file_path):
        if os.path.isfile(file_path):
            return True
        else:
            return False

    def is_dir(self, file_path):
        if os.path.isdir(file_path):
            return True
        else:
            return False

    def is_number(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def is_integer(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def is_boolean(self, value):
        if value == True or value == False:
            return True
        else:
            return False

    def is_list(self, value):
        if type(value) == list:
            return True
        else:
            return False

    def is_dict(self, value):
        if type(value) == dict:
            return True
        else:
            return False

    def is_string(self, value):
        if type(value) == str:
            return True
        else:
            return False

    def is_tuple(self, value):
        if type(value) == tuple:
            return True
        else:
            return False

    def is_set(self, value):
        if type(value) == set:
            return True
        else:
            return False

    def is_none(self, value):
        if value == None:
            return True
        else:
            return False
