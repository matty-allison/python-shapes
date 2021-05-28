from datetime import datetime, timedelta
dt = datetime.today()
print(dt.strftime("%y-%m-%d"))
for x in range(9):
    week = dt + timedelta(days=14)
    dt = week
    print(dt.strftime("%y-%m-%d"))
