#  Leap year for Gregorian calendar 
def leap_yr(year):
  leap = False
  if year % 4 == 0 and year % 100 != 0:
    leap = True
  elif year % 400 == 0:
    leap = True
  return leap

year = int(input("Enter year between 1990 and 10^5: "))

print(leap_yr(year))