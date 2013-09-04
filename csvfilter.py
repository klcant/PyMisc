#!/usr/bin/python

import csv, os

orig_file = csv.reader(open("/path/to/file/orig.csv", "rb"))
dest_file = csv.writer(open("/path/to/file/dest.csv", "wb"))
newrows = []
for row in orig_file:
    if row not in newrows:
        newrows.append(row)
dest_file.writerows(newrows)
