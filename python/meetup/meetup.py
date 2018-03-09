import datetime
import calendar
def meetup_day(year, month, day_of_the_week, which):

    #finding first day
    day = 0
    for i in range(1, 8):
        if switch_day_of_week(day_of_the_week) == datetime.date(year, month, i).weekday():
            day = i
            break
    
    if which is 'teenth':
        while not 12 < day < 20:
            day += 7
        return datetime.date(year, month, day)
    elif which is 'last':
        #calender.monthrange(year, month) return value : (weekday, whole day)
        while  day <= calendar.monthrange(year, month)[1]:
            day += 7
        return datetime.date(year, month, day-7)
    else :
        day += 7*(int(which[0]) - 1)
        if day > calendar.monthrange(year, month)[1]:
            raise ValueError('error')
        else:
            return datetime.date(year, month, day)

def switch_day_of_week(day):
    return {'Monday': 0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4,
            'Saturday':5, 'Sunday':6}.get(day)
