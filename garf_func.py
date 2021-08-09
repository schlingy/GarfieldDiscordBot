
from faker import Faker
from random import randrange
from datetime import datetime 

def random_comic(first_year, first_month, first_day, sunday_only=False):
    fakey = Faker()
    seed = randrange(100000000)
    Faker.seed(seed)

    while(True):
        chosen_date = fakey.date()
        year, month, day = chosen_date.split()
        if int(month[0]) == 0:
            month = month[1]
        if int(day[0]) == 0:
            day = day[1]
        if int(year) < int(first_year):
            if int(year) == int(first_year) and int(month) < int(first_month) and int(day) < int(first_day):
                continue
        else:
            break
    
    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day

    url = "http://images.ucomics.com/comics/ga/" + year + "/ga" + year[2:] + month + day + ".gif"
    return url, year, month, day


def random_sunday_comic():
    # do the import fake from faker thing
    fakey = Faker()
    seed = randrange(100000000)
    Faker.seed(seed)

    while(True):
        chosen_date = fakey.date()
        year, month, day = chosen_date.split('-')
        # turn the day into a datetime object 
        day_object = datetime.strptime(chosen_date, "%Y-%m-%d")
        if int(month[0]) == 0:
            month = month[1]
            print(month)
        if int(day[0]) == 0:
            day = day[1]
            print(day)
        if int(year) < 1978:
            if int(year) == 1978 and int(month) < 6 and int(day) < 19:
                continue
        if day_object.weekday() != 6:
            continue
        else:
            break
    
    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day

    print("year: " + year)
    print("month: " + month)
    print("day: " + day)
    url = "http://images.ucomics.com/comics/ga/" + year + "/ga" + year[2:] + month + day + ".gif"
    return url

def comic_by_date(date):
    split_date = date.split("-")
    year = split_date[0]
    month = split_date[1]
    day = split_date[2]

    url = "http://images.ucomics.com/comics/ga/" + year + "/ga" + year[2:] + month + day + ".gif"
    return url