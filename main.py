def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  """ This function will take 2 arguments, year and month in int format """
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year):
    month_days[1] = 29
    day = month_days[month-1]
    return f"{year} is a leap year and month {month} has {day} days "
  else:
    day = month_days[month-1]
    return f"{year} is not a leap year and month {month} has {day} days "
  

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












