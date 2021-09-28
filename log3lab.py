from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrive() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# FILE_NAME = 'local_copy.log'
#
# fh = open(FILE_NAME)
#
# for line in fh:
#     print(line)
#
# num_lines = sum(1 for line in open('local_copy.log'))
# print(num_lines)
#
# from urllib.request import urlretrieve



URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrive() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

FILE_NAME = 'local_copy.log'

fh = open(FILE_NAME)

for line in fh:
  items = line.split()
  try:
    print(items[3])
  except IndexError:
    pass

from datetime import datetime

try:
  datetime_object = datetime.strptime(items[3], '%d/%m/%y:%H:%M:%S')
except IndexError:
  pass
print(type(datetime_object))

st="[11/Apr/1995:00:00:16"
ed="[11/Oct/1995:14:14:17"
start_date = datetime.datetime.strptime(st.strip(), '%d-%m-%y')
end_date = datetime.datetime.strptime(ed.strip(), '%d-%m-%y')
