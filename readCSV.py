#!/usr/bin/python
#  Author:  Carole Verbick

#  The purpose of this program is to read relevant columns from this link:
#  https://data.sfgov.org/Culture-and-Recreation/SF-Civic-Art-Collection/zfw6-95su
#  by clicking on "manage" and exporting data as a CSV format.  The output is written
#  into a JSON format to be used within my Javascript script.  

import csv
import json

fname = "SF_Civic_Art_Collection.csv"
art = {}

with open( fname, 'r') as fh, open( "data.json", 'w') as fh2:

     c = csv.reader( fh, delimiter=',', quotechar='"')

     # skip the first 2 lines ( header)
     c.__next__()
     c.__next__()

     art_items = []

     for line in c:
          v_json_data = json.loads( line[ 1])

          art[ 'artist'] = line[ 0]
          art[ 'title'] = line[ 2]
          art[ 'lat'] = v_json_data[ 'coordinates'][ 1]
          art[ 'long'] = v_json_data[ 'coordinates'][ 0]
           
          art_items.append( dict( art))


     json.dump( art_items, fh2)

    
