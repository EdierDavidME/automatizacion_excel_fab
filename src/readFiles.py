import os
from src.utils.validations import Validations as Val
from src.excelTypeFiles import ExcelFiles as Excel


class ReadFiles:
    """
    ReadFiles class
    """

    def __init__(self, file_name, folder_ouput, sheet):
        """
        Constructor
        """
        self.sheet = sheet
        self.temp_path = folder_ouput
        self.Validations = Val()
        self.file_extension = file_name.split(".")[1]
        self.file_name = file_name
        self.folder_path = os.path.dirname(
            os.path.abspath(__file__)) + "//assets"
        self.folder_ouput_save = folder_ouput if self.Validations.is_dir(self.temp_path) else os.path.dirname(
            os.path.abspath(__file__)) + "//assets//prueba2.xlsx"
        self.path_file = os.path.join(self.folder_path, self.file_name)
        # self.file_content = self.read_file()

    def read_file(self):
        """
        Reads the file
        """

        try:
            print("> Reading file: {}".format(self.file_name.split(".")[0]))
            print("> File path: {}".format(self.path_file))

            if(self.Validations.is_empty(self.file_name)):
                raise Exception("File name is empty")

            elif(self.Validations.is_file(self.path_file)):
                if self.file_extension == "txt":
                    return self.read_txt_file()
                elif self.file_extension in ["xls", "xlsx", "xlsm", "xlsb", "csv"]:
                    return self.read_excel_file()
            else:
                raise Exception("File does not exist")

        except Exception as e:
            return("* Error: {}".format(e))

    def read_txt_file(self):
        """
        Reads a txt file
        """
        try:
            with open(self.path_file, 'r') as file:
                file_content = file.read()
            # print("> File content: {}".format(file_content))
            return file_content

        except Exception as e:
            return("* Error: {}".format(e))

    def read_excel_file(self):
        """
        Reads an excel file
        """
        try:
            excel = Excel(self.path_file, self.folder_ouput_save, self.sheet)
            return excel.read()

        except Exception as e:
            return("* Error: {}".format(e))
