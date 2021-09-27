# How many total requests have been made in the last 6 months?
    #Oct 24-Apr 24
# How many total requests were made in the time period represented by the log?

from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# Alt.: supply an anonmymous callback function to print a simple progress bar to screen
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True))

# Alt. 2: a progress bar with reduced output (every 1000 blocks)
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

FILE_NAME = 'local_copy.log'

# Use open() to get a filehandle that can access the file
fp = open(FILE_NAME)

# #loop through the file
# for line in fp:
#     print(line)

# # The filehandle object provides many basic file operations:
# # fp.read(32)     # read the specified bytes from the file (if no byte size is specified, then the entire file is read)
# # fp.readline()   # read a single line from the file (up to a newline character - \n)
# # # fh.write('some data here')  # write a string to the file (make sure the file was open()'ed for writing!)
# # fp.close()      # close the file when you're finished with it
# try:
#     # fp = open('local_copy.log')
#     # #do studd with fp
#     # fp.readline()

#     with open('local_copy.log') as f:
#         for index, line in enumerate(f):
#             print("Line {}: {}".format(index, line.strip()))
# finally:
#     fp.close()



