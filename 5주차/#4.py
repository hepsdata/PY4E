#month calculation function
def month_calculation(f_month):
    
    if f_month in [4,6,9,11] :
        end_of_day = 30
    elif f_month == 2 :
        end_of_day = 28
    else :
        end_of_day = 31
        
    return(end_of_day)


#days_of_week calculation function
def days_of_week_calculation(days_of_week,n):

    weekdays = ['일','월','화','수','목','금','토']

    start = weekdays.index(days_of_week)
    
    #-1 : 오늘포함
    num = ( start + n ) % 7 - 1

    f_days_of_week = weekdays[num]

    return(f_days_of_week)


def after_100(month:int, day:int, days_of_week:str) :
    
    # n = After n days
    n = 100

    f_month = month
    f_day = day

    f_days_of_week = days_of_week_calculation(days_of_week,n)

    #n-1 : 오늘 포함
    for i in range(n-1):
        
        f_day += 1
        
        end_of_day = month_calculation(f_month)
        
        if end_of_day < f_day :
            f_day = 1
            f_month += 1


    print(f"{month}월",f"{day}일",f"{days_of_week}부터",f"{n}일 뒤는",f"{f_month}월",f"{f_day}일",f"{f_days_of_week}요일")
    
    
after_100(6,21,"월")
