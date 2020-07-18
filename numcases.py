import requests
import urllib.request
import datetime
from bs4 import BeautifulSoup

def digits_only(string):
        new_string = ""
        for char in string:
            if char.isdigit():
                new_string+=char
            else:
                pass
        return new_string

def get_info(country):
    url = "https://www.worldometers.info/coronavirus/country/"+country+"/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    covid_cases = soup.findAll('span')[4]
    recovered = soup.findAll('span')[6]
    str_covid_cases = digits_only(str(covid_cases))
    str_recovered_people = digits_only(str(recovered))
    return str_covid_cases, str_recovered_people

def get_date():
    d1 = datetime.date.today()
    today = d1.strftime('%m/%d/%Y')
    return today
    
while True:
    countr = input("What country would you like to know about?")
    country = countr.lower()
    today = get_date()
    try:
        total_cases, recovered_people = get_info(country)
    except:
        print("Invalid country!")
    else:
        print("The number of coronavirus cases in", countr, "as of", today, "is", total_cases+".")
        print("The number of recovered people in", countr, "as of", today, "is", recovered_people+".")
        print("Information retrieved from worldometers.info")
    again = input("Again?")
    if again[0]=='y':
        pass
    else:
        break
    
