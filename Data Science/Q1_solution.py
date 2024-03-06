#defining function to check in which range does the given number lie
def check_num(num):
  if num % 2 != 0:
    return 1
  else:
    if( 2 <= num <= 5):
      return 0
    elif (6 <= num <= 20):
      return 1
    else:
      return 0
#taking unput from the user
num = int(input("Enter the number: "))
#checking the constraints
if num < 1 or num > 100:
  print("Number should be in the range 1 to 100")
  num = int(input("Enter again"))

if(check_num(num)):
  print("Weird")
else:
  print("Not weird")
