import os
from src.utils.validations import Validations as Val


class ReadFiles:
    """
    ReadFiles class
    """

    def __init__(self, file_name):
        """
        Constructor
        """
        self.Validations = Val()
        self.file_name = file_name
        self.folder_path = os.path.dirname(
            os.path.abspath(__file__)) + "\\assets"
        # self.file_content = self.read_file()

    def read_file(self):
        """
        Reads the file
        """
        print("> Reading file: {}".format(self.file_name))
        path = os.path.join(self.folder_path, self.file_name)
        print("> File path: {}".format(path))

        try:
            if(self.Validations.is_empty(self.file_name)):
                raise Exception("File name is empty")

            elif(self.Validations.is_file(path)):
                with open(path, 'r') as file:
                    file_content = file.read()
                # print("> File content: {}".format(file_content))
                return file_content

            else:
                raise Exception("File does not exist")

        except Exception as e:
            return("* Error: {}".format(e))
