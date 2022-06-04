from openpyxl import Workbook
from src.utils.validations import Validations as vld

class ExcelFiles:
    def __init__(self, file, dir):
        self.wb = Workbook()
        self.file = file
        self.dir = dir
        self.ws = None

    def write(self):
        self.ws = self.wb.active
        self.ws.title = "Excel Files"
        self.ws.append(["File Name", "File Type"])
        self.ws.append(["test.xlsx", "Excel"])
        self.ws.append(["test.xls", "Excel"])
        self.ws.append(["test.xlsm", "Excel"])
        self.ws.append(["test.xlsb", "Excel"])

        self.wb.save(self.dir + "\\excelTypeFiles.xlsx")
