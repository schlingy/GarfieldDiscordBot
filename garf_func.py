
from faker import Faker
from random import randrange, choice
from datetime import datetime, timedelta

# GET ALL DAYS IN A RANGE FROM START TO END
def date_range(start, end):
    delta = end - start
    days = [start + timedelta(days=i) for i in range(delta.days + 1)]
    return days

def format_date(month, day):
    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day
    return month, day

# GLOBAL 
# turn the date of comic's first appearance into datetime object
# find today's day, and create the list of days
first_comic_date = datetime.strptime("1978-06-19", "%Y-%m-%d")
today = datetime.now()
all_dates = date_range(first_comic_date, today)

def comic_by_number(number):

    index = int(number) - 1
    comic_date = all_dates[index]
    year = comic_date.strftime("%Y")
    month =  comic_date.strftime("%m")
    day = comic_date.strftime("%d")
    month, day = format_date(month, day)
    total = len(all_dates)

    url = "http://images.ucomics.com/comics/ga/" + year + "/ga" + year[2:] + month + day + ".gif"
    return url, year, month, day, number, total
    
def random_comic(first_year, first_month, first_day):
    fakey = Faker()
    seed = randrange(100000000)
    Faker.seed(seed)

    while(True):
        chosen_date = fakey.date()
        year, month, day = chosen_date.split("-")
        if int(month[0]) == 0:
            month = month[1]
        if int(day[0]) == 0:
            day = day[1]
        if int(year) < int(first_year):
            if int(year) == int(first_year) and int(month) < int(first_month) and int(day) < int(first_day):
                continue
        else:
            break
    
    month, day = format_date(month, day)

    # turn the day into a datetime object 
    day_object = datetime.strptime(chosen_date, "%Y-%m-%d")
    number = all_dates.index(day_object) + 1
    total = len(all_dates)
   
    url = "http://images.ucomics.com/comics/ga/" + year + "/ga" + year[2:] + month + day + ".gif"
    return url, year, month, day, number, total

def random_comic_by_year(chosen_year, first_year):
    fakey = Faker()
    seed = randrange(100000000)
    Faker.seed(seed)

    while(True):
        chosen_date = fakey.date()
        year, month, day = chosen_date.split('-')
        day_object = datetime.strptime(chosen_date, "%Y-%m-%d")

        if int(month[0]) == 0:
            month = month[1]
        if int(day[0]) == 0:
            day = day[1]
        if int(year) == int(chosen_year):
            if int(chosen_year) >= int(first_year):
                if int(chosen_year) == int(first_year) and int(month) < 6 and int(day) < 19:
                    continue
                else:
                    break
    
    number = all_dates.index(day_object) + 1
    total = len(all_dates)
    
    month, day = format_date(month, day)

    url = "http://images.ucomics.com/comics/ga/" + year + "/ga" + year[2:] + month + day + ".gif"
    return url, year, month, day, number, total


def random_comic_by_decade(decade):
    if decade == "70s":
        seventies = []
        for i in range(0, 561):
            seventies.append(i)
        comic_index = choice(seventies)

    if decade == "80s":
        eighties = []
        for i in range(561, 4214):
            eighties.append(i)
        comic_index = choice(eighties)
    
    if decade == "90s":
        nineties = []
        for i in range(4214, 7866):
            nineties.append(i)
        comic_index = choice(nineties)
    
    if decade == "00s":
        zeros = []
        for i in range(7866, 11519):
            zeros.append(i)
        comic_index = choice(zeros)
    
    if decade == "10s":
        tens = []
        for i in range(11519, 15171):
            tens.append(i)
        comic_index = choice(tens)
    
    if decade == "20s":
        twenties = []
        total = len(all_dates)
        for i in range(15171, total):
            twenties.append(i)
        comic_index = choice(twenties)

    comic_date = all_dates[comic_index]
    year = comic_date.strftime("%Y")
    month =  comic_date.strftime("%m")
    day = comic_date.strftime("%d")
    month, day = format_date(month, day)
    total = len(all_dates)

    url = "http://images.ucomics.com/comics/ga/" + year + "/ga" + year[2:] + month + day + ".gif"
    return url, year, month, day, total


def random_sunday_comic():
    while(True):

        url, year, month, day, number, total = random_comic(1978, 6, 19)
        date = year + "-" + month + "-" + day
        day_object = datetime.strptime(date, "%Y-%m-%d")
        if day_object.weekday() !=6:
            continue
        else:
            break

    number = all_dates.index(day_object) + 1
    total = len(all_dates)
   
    url = "http://images.ucomics.com/comics/ga/" + year + "/ga" + year[2:] + month + day + ".gif"
    return url, year, month, day, number, total
    
def comic_by_date(date):
    split_date = date.split("-")
    year = split_date[0]
    month = split_date[1]
    day = split_date[2]

 # turn the day into a datetime object 
    day_object = datetime.strptime(date, "%Y-%m-%d")
    number = all_dates.index(day_object) + 1
    total = len(all_dates)
   
    url = "http://images.ucomics.com/comics/ga/" + year + "/ga" + year[2:] + month + day + ".gif"
    return url, year, month, day, number, total
    
# def find_word_in_comic(word):
    # f = open("garf_transcripts.txt", "r")
    # comic_file = f.read()
    # individual_comics = comic_file.split("+++++START OF ENTRY+++++")

    # matches = []
    # for comic in individual_comics:
    #     comic_lines = comic.split("\n")
    #     for line in comic_lines:
    #         if line.startswith("DATE"): 
    #             date = line
    #         if word in line:
    #             matches.append({"match": line, "date": date})
    # return matches