from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# Alt.: supply an anonmymous callback function to print a simple progress bar to screen
#local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True))

# Alt. 2: a progress bar with reduced output (every 1000 blocks)
#local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

FILE_NAME = 'local_copy.log'

fh = open(FILE_NAME)
counter = 0
counter2 = 0

for line in fh:
  counter += 1
  if "Apr" in line and "1995" in line:
    counter2 += 1
  elif "May" in line and "1995" in line:
    counter2 += 1
  elif "Jun" in line and "1995" in line:
    counter2 += 1
  elif "Jul" in line and "1995" in line:
    counter2 += 1
  elif "Aug" in line and "1995" in line:
    counter2 += 1
  elif "Sep" in line and "1995" in line:
    counter2 += 1
  elif "Oct" in line and "1995" in line:
    counter2 += 1
  else:
    counter2 += 0

print("There have been", counter, "total requests!")
print ("There have been", counter2, "requests in the last 6 months!")


# \[(\d{2})/([A-Za-z]{3,4})/(\d{4}):(\d{2}:\d{2}:\d{2}).+\] \"([A-Z]{3,6}) (.+) HTTP/1.0\" (\d{3}) .*

fh2 = open(FILE_NAME)


import calendar
import datetime
from datetime import datetime
from datetime import date
import re
regex = re.compile('\[(\d{2})/([A-Za-z]{3,4})/(\d{4}):(\d{2}:\d{2}:\d{2}).+\] \"([A-Z]{3,6}) (.+) HTTP/1.0\" (\d{3}) .*')

monday_counter= 0
tuesday_counter = 0
wednesday_counter = 0
thursday_counter = 0
friday_counter = 0
saturday_counter = 0
sunday_counter = 0
sunday_counter = 0

for line in fh2:
  parts = regex.split(line)
  try:
    month_name = parts[2]
    month_num = datetime.strptime(month_name, '%b').month
    log_date = date(year=int(parts[3]), month=month_num, day=int(parts[1]))

#Question 4

fh4 = open(FILE_NAME)

for line in fh4:
  total1 = re.findall(r"\b(3\d\d)\b",fh4.read())
RequestTotal2 = (len(total1) / 726736) * 100
print ( "{}% were redirected.".format(round(RequestTotal2)))
