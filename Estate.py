from datetime import datetime
from selenium import webdriver
import pyodbc
import copy
from configparser import ConfigParser

parser = ConfigParser()
parser.read('setup.ini')

# connect to sql
conn = pyodbc.connect(parser['sql']['connection_string'])

cursor = conn.cursor()
cursor.execute('SELECT * FROM Property')


def export_sql(estate_deal: list) -> None:
    for n in range(0, len(estate_deal)):
        values = (estate_deal[n]["Block"],
                  estate_deal[n]["Selling_Date"],
                  estate_deal[n]["Address"],
                  estate_deal[n]["City"],
                  estate_deal[n]["Type"],
                  estate_deal[n]["Rooms"],
                  estate_deal[n]["Floor"],
                  estate_deal[n]["Surface"],
                  estate_deal[n]["Price"],
                  estate_deal[n]["Change"])

        store_procedure = """
        exec [RealEstate].[dbo].spInsertDeal 
        @Block = ?,
        @Selling_Date = ?, 
        @Address = ?,
        @City = ?, 
        @Type_estate = ?, 
        @Rooms = ?,
        @Floor_num = ?,
        @Surface = ?,
        @Price = ?,
        @Price_Change =  ? 
        """

        cursor.execute(store_procedure, values[:])
        cursor.commit()

        pass


def deals_property(deals: list) -> list:
    value_count = int(len(deals))
    col_num = int(11)
    row_num = int(value_count / col_num)
    estate_deal = [{}] * row_num
    estate_row = {
        "Block": None, "Selling_Date": None,
        "Address": None, "City": None,
        "Type": None, "Rooms": None,
        "Floor": None, "Surface": None,
        "Price": None, "Change": None
    }
    row = 0
    for n in range(0, value_count, col_num):
        estate_row["Selling_Date"] = datetime.strptime(deals[n], '%d.%m.%Y').strftime("%Y-%m-%d")
        estate_row["Address"] = deals[n + 1]
        estate_row["Block"] = deals[n + 2]
        estate_row["Type"] = deals[n + 3]
        estate_row["Rooms"] = float(deals[n + 4])
        estate_row["Floor"] = deals[n + 5]
        estate_row["Surface"] = float(deals[n + 6])
        estate_row["Price"] = deals[n + 7]
        estate_row["Change"] = deals[n + 8]
        estate_row["City"] = deals[n + 9]

        estate_deal[row] = copy.deepcopy(estate_row)
        row = row + 1

    return estate_deal


def import_real_estate_deals(city: str, street: str) -> list:
    # That is the site
    main_url = parser['url']['site']
    path = parser['files']['chrome_driver_path']

    url = main_url + '/?search=' + city + " " + street  # This way we search every city
    url = url.replace(" ", "%20")
    # connect to the web site

    driver = webdriver.Chrome(path)
    driver.get(url)
    column_elements = driver.find_elements_by_class_name('tableCol')

    columns = [s.text for s in column_elements]

    deals = deals_property(columns)
    return deals


def main():

    es = parser['Estate']

    # import web table
    deals = import_real_estate_deals(es['cities'], es['street'])

    # export table data to sql
    export_sql(deals)


if __name__ == '__main__':
    main()
