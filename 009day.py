# myScore = int(input("Your score: "))
# if myScore > 100000:
#  print("Winner!")
# else:
#  print("Try again 😭")

print("--- generation identifier ---")
myYear = int(input("which year were you born? "))
if myYear >= 1883 and myYear <= 1900:
  print("lost generation")
elif myYear >= 1901 and myYear <= 1927:
  print("greatest generation")
elif myYear >= 1928 and myYear <= 1945:
  print("silent generation")
elif myYear >= 1946 and myYear <= 1964:
  print("baby boomers")
elif myYear >= 1965 and myYear <= 1980:
  print("generation x")
elif myYear >= 1981 and myYear <= 1996:
  print("millennials")
elif myYear >= 1997 and myYear <= 2012:
  print("generation z")
elif myYear >= 2012 and myYear <= 2023:
  print("generation alpha")
else:
  print("you are not born yet")