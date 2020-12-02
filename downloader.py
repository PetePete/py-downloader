import os
import urllib.request

DOWNLOADS_DIR = '/Users/jan.nyfeler/Desktop/mark/download/'

# For every line in the file
for url in open('/Users/jan.nyfeler/Desktop/mark/list.txt'):
    # Split on the rightmost / and take everything on the right side of that
    name = url.rsplit('/', 1)[-1]

    # Combine the name and the downloads directory to get the local filename
    filename = os.path.join(DOWNLOADS_DIR, name)
    filename = filename.strip()

    # Download the file if it does not exist
    try:
        if not os.path.isfile(filename):
            urllib.request.urlretrieve(url, filename)
    except: 
        pass