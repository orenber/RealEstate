from configparser import ConfigParser

config = ConfigParser()

config['files'] = {'chrome_driver_path': "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"}

config['sql'] = {'Driver': "{SQL Server}",
                 'Server': 'ORENBER-PC\MSSQLSERVER2008',
                 'Database': 'RealEstate',
                 'Trusted_Connection': 'yes',
                 'connection_string': 'Driver={SQL Server};Server=ORENBER-PC\\MSSQLSERVER2008;Database=RealEstate;Trusted_Connection=yes;'}


config['url'] = {'site': 'https://www.nadlan.gov.il/'}

config['Estate'] = {'cities': "פתח תקווה",
                    'street': 'רמב"ם 38'}


with open('./setup.ini','w') as f:
    config.write(f)