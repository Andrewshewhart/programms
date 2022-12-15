day=int(input("whaT IS THE DAY YOU WERE BORN?"))
month=int(input("in which month you were born?"))
year=int(input("in which year you were born?"))
modernday=int(input("what day is it today? "))
modernmonth=int(input('which month is right now?'))
modernyear=int(input("what is the year?"))
while month<=12:
  day=365*(modernyear-year)
  month=12*(modernyear-year)
  year=modernyear-year
  break
print("year:",year,"months:",month,"days has gone:",day)