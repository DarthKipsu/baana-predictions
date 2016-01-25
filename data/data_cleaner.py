from bs4 import BeautifulSoup
from openpyxl import load_workbook

def read_xlsx_file(path, sheet):
    """
    Takes a path to xlsx (Excel) file and a sheet name within the file and returns an openpyxl
    Workbook sheet.
    """
    return load_workbook(path).get_sheet_by_name(sheet)

def read_xml_file(path):
    """
    Takes a path to xml file and returns BeautifulSoup object representing the document.
    """
    return BeautifulSoup(open(path), 'lxml-xml')

def print_content(path, sheet_name, cells):
    sheet = read_xlsx_file(path, sheet_name)
    for row in sheet.iter_rows(cells):
        # row[0] = datetime object for the count
        # row[1] = the day of week for the count
        # row[2] = the actual cyclist count
        print(row[0].value, row[1].value, row[2].value)

def print_xml(path):
    soup = read_xml_file(path)
    for feature in soup.find_all('MeasurementTimeseries'):
        # prints feature ids
        print(feature.get('gml:id'))

# currently the data is in rows B3:D850
print_content('original/Baanan_pyorailijamaarat.xlsx', 'Taul1', 'B3:D50')

print_xml('original/fmi-2013-2014.xml')
