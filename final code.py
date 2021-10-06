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

#pull request test
#pull request test 2
