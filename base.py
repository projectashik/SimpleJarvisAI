import datetime


def introduction():
    return "Hey, It's me Jarvis. I am being developed by Ashik Chapagai since March 3 2021."


def current_time():
    return datetime.datetime.now().strftime('%I:M% %p')


def greet(name):
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        return "Good Morning, " + name
    elif 12 <= hour <= 18:
        return "Good Afternoon, " + name
    else:
        return "Good Evening, " + name
