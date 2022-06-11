import pytz
from datetime import datetime, date, timedelta, timezone, time

# Display date
print("Current datetime", datetime.now())
curr_date = date.today()
print(f"Current date is {curr_date}: day {curr_date.day} month {curr_date.month} and year {curr_date.year}")

# create date
a_date = date(2021, 10, 1)
print("A Date", a_date)
print("Date from Timestamp", date.fromtimestamp(1326244364))

# Create DateTime from string. Using strptime()
date_string = "21 January 2021, 10:00:10"
date_object = datetime.strptime(date_string, "%d %B %Y, %H:%M:%S")
print(f"Date string [{date_string}] converted to date [{date_object}]")

# create timestamp
# python already have function timestamp() to get the timestamp of datetime since epoch.
print(f"Timestamp since epoc to current date tims is {datetime.now().timestamp()}")

# epoch = miliseconds since unix epoch time 1970-01-01
# to manually calculate: epcoch and datetime should have same timezone
# so it can be substracted

epoch = datetime(1970, 1, 1, 0, 0, 0, 0, timezone.utc)
curr_datetime = datetime.now(timezone.utc)
timestamp = (curr_datetime - epoch) / timedelta(seconds=1)  # float
int_timestamp = (curr_datetime - epoch) // timedelta(seconds=1)  # int
print(f"Timestamp of current date is {timestamp} == {int_timestamp}")

# time delta is object represents the difference between two dates or times
# when substracting 2 datetimes the result type is <class 'datetime.timedelta'>
t1 = timedelta(days=1, seconds=20)  # not only seconds can be mix days, hours etc
t2 = timedelta(days=1, seconds=50)
delta = t1 - t2
# negative delta will give unexpected. Must abs() first.
print(f"Delta t1 - t2 is {delta}")  # -1 day, 23:59:30
print(f"Delta abs t1 - t2 is {abs(delta)}")  # 30 secs
print(f"Delta in seconds {delta.total_seconds()}")  # 30 secs

# time
curr_time = time(10, 1, 1, 1000)
print(f"Current time {curr_time}: Hour {curr_time.hour} Minute {curr_time.minute} and Seconds {curr_time.second}.{curr_time.microsecond}")
print(datetime.now().timetz(), date.day, timezone.utc)

# Format time. User strftime()
print("Indonesia Format", curr_datetime.strftime("%d/%m/%Y %H:%M%:%S"))

# Handling Timezone
# To make it easier, there's module called pytZ
tz_ID = pytz.timezone("Asia/Jakarta")  # UTC
datetime_ID = datetime.now(tz_ID)  # +7
print("TZ ID:", datetime_ID.strftime("%m/%d/%Y, %H:%M:%S"))
