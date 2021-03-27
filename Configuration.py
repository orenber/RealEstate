from configparser import ConfigParser

config = ConfigParser()

config['files'] = {'crome_driver_path': "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"}

config['sql'] = {'Driver':"{SQL Server}",
                 'Server':'ORENBER-PC\MSSQLSERVER2008',
                 'Database':'RealEstate',
                 'Trusted_Connection':'yes',
                 'conection_string':'Driver={SQL Server};Server=ORENBER-PC\\MSSQLSERVER2008;Database=RealEstate;Trusted_Connection=yes;'}


config['url']  = {'site': 'https://www.nadlan.gov.il/'}


with open('./setup.ini','w') as f:
    config.write(f)