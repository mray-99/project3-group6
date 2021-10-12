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
import calendar
import datetime
from datetime import datetime
from datetime import date

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
    #dt = datetime.strptime(log_date,"%d/%b/%Y")
    #print(findDay(date))
    #week_num=datetime.log_date.weekday()
    #print(log_date.strftime("%w"))
    day_num = int(log_date.strftime("%w"))
    if day_num == 0:
      monday_counter += 1
    elif day_num == 1:
      tuesday_counter += 1
    elif day_num == 2:
      wednesday_counter += 1
    elif day_num == 3:
      thursday_counter += 1
    elif day_num == 4:
      friday_counter += 1
    elif day_num == 5:
      saturday_counter += 1
    else:
      sunday_counter += 1 
  except:
    pass
print("")
print("There were",monday_counter,"requests made on Mondays.")
print("There were",tuesday_counter,"requests made on Tuesdays.")
print("There were",wednesday_counter,"requests made on Wednesdays.")  
print("There were",thursday_counter,"requests made on Thursdays.")
print("There were",friday_counter, "requests made on Fridays.")
print("There were", saturday_counter, "requests made on Saturdays.")
print("There were", sunday_counter, "requests made on Sundays.")
print("")

#question 2

from statistics import mean

number_list = [monday_counter, tuesday_counter, wednesday_counter, thursday_counter, friday_counter, saturday_counter, sunday_counter]
avg = mean(number_list)
avg2 = mean(number_list)*4 
print("the average is " , round(avg))
print("the monthly average is " , round(avg2)) 

# Driver program

     
#questions 3 

#Pattern1 = r"\b(4\d\d)\b"

fh3 = open(FILE_NAME)




for line in fh3:
  total = re.findall(r"\b(4\d\d)\b",fh3.read())
RequestTotal = (len(total) / 726736) * 100
print ( "{}% were not successful.".format(round(RequestTotal)))
print("")
    
    
    
    
#Question 4

fh4 = open(FILE_NAME)

for line in fh4:
  total1 = re.findall(r"\b(3\d\d)\b",fh4.read())
RequestTotal2 = (len(total1) / 726736) * 100
print ( "{}% were redirected.".format(round(RequestTotal2)))
