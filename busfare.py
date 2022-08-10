import datetime as dt

current_date = dt.date.today()
Final_date = current_date.strftime("%A")
day = current_date.strftime("%a")
weekday = dt.date.today().weekday()

print("Date:",current_date)
print("Day:", day)

if weekday <5:
    print("Fare:100")
elif weekday == 5:
    print("Fare:60")
elif weekday == 6:
    print("Fare:80")
else:
    pass
