# function for checking if it is a leap year
def check_year(year):
  flag = 0
  if year%4 == 0:
    flag = 1
    if year%100 == 0:
      flag = 0
      if year%400 == 0:
        flag = 1
  if flag == 1:
    return 1
  return 0

#input year from the user
year = int(input("Enter year: "))
if(check_year(year)):
  print("Leap year")
else:
  print("Not a leap year")
