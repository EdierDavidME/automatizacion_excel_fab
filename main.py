# PRINCIPAL CLASS: Main
# PURPOSE: Main class for the program.
import argparse as ap
from src.readFiles import ReadFiles

LINES = 25

parser = ap.ArgumentParser()
parser.add_argument("-f", "--file", help="File to be read", required=True)
parser.add_argument("-s", "--sheet", help="Sheet from excel", required=False)
parser.add_argument("-o", "--ouput", help="Dir to save", required=False)
args = parser.parse_args()


# def main():
#     if __name__ == "main":
print("#\tExcel\t\t#")
print("-"*LINES)
read_file = ReadFiles(args.file, str(args.ouput), str(args.sheet))
print(read_file.read_file())


# main()
