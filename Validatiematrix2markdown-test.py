
def test_file_exists():
  import os.path
  assert os.path.isfile('Validatiematrix.xlsx')

def test_open_xslx_openpyxl():
  import openpyxl
  wb = openpyxl.load_workbook('Validatiematrix.xlsx')
  assert wb is not None
