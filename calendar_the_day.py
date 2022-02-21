
print("Feel free to see name day of any day any year :-).")
year = input("Introduce the year: ")
month = input("Introduce the month: ")
day = input("Introduce the day: ")

year = int(year)
month = int(month)
day = int(day)
import calendar
desired_date = calendar.weekday(year, month, day)
name = calendar.day_name[desired_date]

print(str(day) + "-" + str(month) + "-" + str(year) + " was " + name + ".")
