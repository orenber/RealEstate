from datetime import datetime
from selenium import webdriver
import pyodbc
import copy
from configparser import ConfigParser

parser = ConfigParser()
parser.read('setup.ini')


def export_sql(estat_deal: dict) -> None:
    for n in range( 0, len( estat_deal ) ):
        values = (estat_deal[n]["Block"],
                  estat_deal[n]["Selling_Date"],
                  estat_deal[n]["Address"],
                  estat_deal[n]["City"],
                  estat_deal[n]["Type"],
                  estat_deal[n]["Rooms"],
                  estat_deal[n]["Floor"],
                  estat_deal[n]["Surface"],
                  estat_deal[n]["Price"],
                  estat_deal[n]["Change"]);

        store_procedure = """
        exec [RealEstate].[dbo].spInsertDeal
        @Block = ?,
        @Selling_Date = ?, 
        @Adresss = ?,
        @City = ?, 
        @Type_estate = ?, 
        @Rooms = ?,
        @Floor_num = ?,
        @Surface = ?,
        @Price = ?,
        @Price_change =  ? 
        """

        cursor.execute( store_procedure, values[:] )
        cursor.commit()

        pass


def deals_property(deals: list) -> list:
    value_count = int( len( deals ) )
    col_num = int( 11 )
    row_num = int( value_count / col_num )
    estat_deal = [{}] * row_num
    estete_row = {
        "Block": None, "Selling_Date": None,
        "Address": None, "City": None,
        "Type": None, "Rooms": None,
        "Floor": None, "Surface": None,
        "Price": None, "Change": None
    }
    row = 0;
    for n in range( 0, value_count, col_num ):
        estete_row["Selling_Date"] = datetime.strptime( deals[n], '%d.%m.%Y' ).strftime( "%Y-%m-%d" )
        estete_row["Address"] = deals[n + 1]
        estete_row["Block"] = deals[n + 2]
        estete_row["Type"] = deals[n + 3]
        estete_row["Rooms"] = float( deals[n + 4] )
        estete_row["Floor"] = deals[n + 5]
        estete_row["Surface"] = float( deals[n + 6] )
        estete_row["Price"] = deals[n + 7]
        estete_row["Change"] = deals[n + 8]
        estete_row["City"] = deals[n + 9]

        estat_deal[row] = copy.deepcopy( estete_row )
        row = row + 1

    return estat_deal

def import_nadlan_deals(cities: list, street: str) -> dict:
    # That is the site
    main_url = parser['url']['site']
    path = parser['files']['crome_driver_path']

    for city in cities:
        url = main_url + '/?search=' + city + street  # This way we search every city
        url = url.replace( " ", "%20" )
        driver = webdriver.Chrome( path )
        driver.get( url )
        column_elements = driver.find_elements_by_class_name( 'tableCol' )

        columns = [s.text for s in column_elements]

        deals = deals_property( columns )
    return deals

# connect to sql
conn = pyodbc.connect( parser['sql']['conection_string'] )

cursor = conn.cursor()
cursor.execute( 'SELECT * FROM Property' )

# connect to the web site

cities = ["פתח תקווה"]
street = ' רמב"ם 38'





# import web table


# exsport table data to sql
exsport_sql( deals )