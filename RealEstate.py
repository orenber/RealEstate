
# !pip install selenium
# WebDriver installation required
import pyodbc 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException
import csv
import datetime 
import time

def is_empty(string):
    return len(string.strip())==0


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ORENBER-PC\MSSQLSERVER2008;'
                      'Database=RealEstate;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM purchase')

for row in cursor:
    print(row)

start_time = time.time() # to measure running time
path = "C:\Program Files (x86)\Google\Chrome\Application\87.0.4280.88\chromedriver.exe"

def validate(date_text):
    '''This function helps us check wheater the string contain date'''
    try:
        datetime.datetime.strptime(date_text, '%d.%m.%Y')
        return True
    except ValueError:
        return False


the_list= []  # This list is going to contain the final data, which will be converted to dictionary
cities = ["פתח תקווה"]
street = ' רמב"ם 38 ' 
room = ["4"]

 
for city in cities:
    driver = webdriver.Chrome(path)
    main_url = 'https://www.nadlan.gov.il/' # That is the site
    url = main_url + '/?search=' + city + street # This way we search every city
    driver.get(url)
    time.sleep(5) # Change is possible


    waiting_time = 0.5 # Change is possible, addapt to your needs
    max_count = 1 # same
    count = max_count
    height_dict = {}
    row = driver.find_elements_by_class_name('tableCol')
    while count>1:
        '''This loop made to catch and scroll all data'''
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        count-=1
        print(f"{city}, count: {count}, waiting time:{waiting_time}")
        time.sleep(waiting_time)
        row = driver.find_elements_by_class_name('tableCol')
        height_dict = {**height_dict, **{count: len(row)}}
        print(height_dict)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        count-=1
        print(f"{city}, count: {count}, waiting time:{waiting_time}")
        time.sleep(waiting_time)
        row = driver.find_elements_by_class_name('tableCol')
        height_dict = {**height_dict, **{count: len(row)}}
        print(height_dict)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        count-=1
        print(f"{city}, count: {count}, waiting time:{waiting_time}")
        if len(height_dict) > 5:
            height_dict = dict(list(height_dict.items())[-9:]) # Making the dict shorter
        time.sleep(waiting_time)
        row = driver.find_elements_by_class_name('tableCol')
        height_dict = {**height_dict, **{count: len(row)}}
        print(height_dict)
        if height_dict[count] <= height_dict[count+2]: #  This way running time is shorter
            waiting_time = waiting_time*2 # Adaptiv time.sleep
            if waiting_time > 10:
                count = 1
            elif height_dict[count] > height_dict[count+1] and height_dict[count] > height_dict[count+2]:
                waiting_time = 0.5 # If there is data - run FASTER



    row = driver.find_elements_by_class_name('tableCol')
    if len(row) == 0:
        print(city, "Nothing found")
    else:
        print(f"{len(row)} records found in {city}")
        lst = []
        for r in row:
            new_row = r.text #  Convert to text
            lst.append(new_row)


        data = []
        new_row = []
        for i in range(0, len(lst)):
            '''split the data to rows'''
            new_row.append(lst[i])
            if validate(lst[i]):
                new_row.remove(lst[i])
                data.append(new_row)
                new_row = [lst[i]]


        temp_dict = {}
        for i in data:
            '''Each element to key'''
            temp_list = []
            if len(i) > 0:
                if "\u0590" <= i[0] <= "\u05EA": # If hebrew inside
                    temp_dict = {**temp_dict, **{"Adresss": i[0]}}
                elif validate(i[0]): # if date
                    cr_date = datetime.datetime.strptime(i[0], '%d.%m.%Y')
                    cr_date = cr_date.strftime("%d/%m/%Y")
                    temp_dict = {**temp_dict, **{"Selling Date": cr_date}}

                if "\u0590" <= i[1] <= "\u05EA":
                    temp_dict = {**temp_dict, **{"Adresss": i[1]}}

                else: # גוש חלקה (block in hebrew)
                    temp_dict = {**temp_dict, **{"Block": i[1]}}

                if "\u0590" <= i[2] <= "\u05EA":
                    temp_dict = {**temp_dict, **{"App. Type": i[2]}}

                else:
                    temp_dict = {**temp_dict, **{"Block": i[2]}}


                if "\u0590" <= i[3] <= "\u05EA":
                    temp_dict = {**temp_dict, **{"App. Type": i[3]}}

                else:
                    if is_empty(i[3]):
                        i[3]=float(0)
                    temp_dict = {**temp_dict, **{"Num. of rooms": i[3]}}

                if "\u0590" <= i[4] <= "\u05EA":
                    temp_dict = {**temp_dict, **{"Floor": i[4]}}

                else:
                    temp_dict = {**temp_dict, **{"Num. of rooms": float(i[4])}} 


                if "\u0590" <= i[5] <= "\u05EA":
                    temp_dict = {**temp_dict, **{"Floor": i[5]}}

                else:
                    temp_dict = {**temp_dict, **{"Surface": float(i[5])}}

                if '.' in i[6] or len(i[6]) < 4:
                    temp_dict = {**temp_dict, **{"Surface": float(i[6])}}

                else:
                    temp_dict = {**temp_dict, **{"Selling Price": float(i[6].replace(",",""))}}

                if "%" in i[7]:
                    temp_dict = {**temp_dict, **{"Change in return": i[7]}}

                else:
                    if is_empty(i[7]):
                        i[7]=float(0)
                    else:
                        i[7] = float(i[7].replace(",",""))
                    temp_dict = {**temp_dict, **{"Selling Price": i[7] }}


                if "%" in i[8]:
                    temp_dict = {**temp_dict, **{"Change in return": i[8]}}

                temp_dict = {**temp_dict, **{"City": city}}

                the_list.append(temp_dict)

    driver.close()


now = datetime.datetime.now()
current_time = now.strftime("%d.%m.%Y %H.%M.%S")
name = 'Real_Estate' +" " + str(current_time)
filename= "%s.csv" % name
with open(filename, 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file,["Selling Date", "Adresss", "Block", "App. Type", "Num. of rooms",
                                               "Floor", "Surface", "Selling Price", "Change in return", "City"])
    dict_writer.writeheader()
    dict_writer.writerows(the_list)

    
end_time = time.time()

running_time = (end_time - start_time)/60
for n in range(0,len(the_list)):
    cursor.execute('spInsertDeal '+
                   the_list[n]['Block']+","+
                   the_list[n]['Selling Date']+","+
                   the_list[n]['City']+","+
                   the_list[n]['Adresss']+","+
                   the_list[n]['App. Type']+","+
                   the_list[n]['Num. of rooms']+","+
                   the_list[n]['Floor']+","+
                   the_list[n]['Surface']+","+
                   the_list[n]['Selling Price']+","+
                   the_list[n]['Change in return']
                         )
print(f"FINISH! running time is {running_time} minutes")

 
