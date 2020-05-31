import calendar
def is_leap(year):
    return calendar.isleap(year)
    # 2nd way or naive approach
    # leap = False
    # if year%4==0 and year%100!=0 or year%400==0:
    #     return True
    # return False
    # # Write your logic here
    
    # return leap

year = int(input())
print(is_leap(year))
