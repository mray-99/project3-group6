from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

FILE_NAME = 'local_copy.log'

fh = open(FILE_NAME)

for line in fh:
 print(line)

num_lines = sum(1 for line in open('local_copy.log'))
print('The total number of requests made is' , num_lines)
