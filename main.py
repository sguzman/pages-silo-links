import brotli
import sys
import os

filename = sys.argv[1]
file = open(filename, 'rb').read()
links = brotli.decompress(file)
links_split = links.split(b'\n')[:-1]
for i in links_split:
    out_file = './%s.html.brotli' % i
    if os.path.exists(out_file) is False:
        print(i)
