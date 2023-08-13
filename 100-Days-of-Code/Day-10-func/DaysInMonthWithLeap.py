def is_leap(year):
  """"Take a year and return True if it is a leap year, otherwise return False"""
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
#print (is_leap)

def days_in_month(year, month):
  """Take a year and a month and return the number of days in the month"""
  if month > 12 or month < 1:
    return "Invalid month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(year) and month == "february":
      return  29
  months = {
      "january" : 31,
      "february" : 28,
      "march" : 31,
      "april" : 30,
      "may" : 31,
      "june" : 30,
      "july" : 31,
      "august" : 31,
      "september" : 30,
      "october" : 31,
      "november" : 30,
      "december" : 31,
  }
  return int(months[month])
  
  #print (months[month])
  #return months[month]

  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = str(input("Enter a month: ")).lower()
days = days_in_month(year, month)
print(days)
