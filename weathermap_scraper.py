#!/usr/bin/env python3
'''
Copyright (c) 2024, FUJIHARA Kazuhiro
This is a script to Scrape weather maps from jma.
Usage: python3 weathermap_scraper.py [option]
    -u: use utc

'''

from datetime import datetime
from optparse import OptionParser
import sys
import os
import urllib.request

tz = '0900JST'

wm_files = [
    ('www.data.jma.go.jp/fcd/yoho/data/wxchart/quick/', 'ASAS_MONO.pdf'),
    ('www.jma.go.jp/bosai/numericmap/data/nwpmap/', 'aupq35_00.pdf'),
    ('www.jma.go.jp/bosai/numericmap/data/nwpmap/', 'aupq78_00.pdf')
]


# parse options and args
usage = "usage: /path/to/%prog [options]"
parser = OptionParser(usage = usage)
parser.add_option("-u", "--utc", action="store_true", dest="utc", help="ファイル名，フォルダ名にUTCを使う")

(options, args) = parser.parse_args()

if len(args) != 0:
    parser.print_help()
    sys.exit()

# create and change dir
date_string = datetime.now().strftime('%Y%m%d')
if options.utc :
    tz = '0000UTC'

date_string = date_string + tz
dir_string = './' + date_string

if os.path.isdir(dir_string) is False:
    os.makedirs(dir_string)

os.chdir(dir_string)

# scraping
for i, j in wm_files:
    url = 'https://' + i + j
    save_file_name = j
    urllib.request.urlretrieve(url, save_file_name)
