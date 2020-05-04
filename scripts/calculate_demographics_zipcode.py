'''
Expected input: Accept an array of GeoJSON-like features with "community_area"
and "ward" properties from STDIN.

Expected output: CSV containing community area, ward, and population columns.
'''
import csv
import json
import sys
import os

from census_area import Census

from secrets import CENSUS_API_KEY


# Default to total population if no environment variable set.
# See https://api.census.gov/data/2018/acs/acs5/variables.html for variable definitions.
tables = os.environ.get('ACS_TABLES', 'B01003_001E').split(',')

writer = csv.writer(sys.stdout)
writer.writerow(['community_area', 'zip', *tables])

c = Census(CENSUS_API_KEY, year=2017)

for feature in json.load(sys.stdin):
    community_area = feature['properties']['community_area'].title()
    zipcode = feature['properties']['zipcode']

    table_values = []

    for table in tables:
        data_by_tract = c.acs5.geo_tract(('NAME', table), feature)

        # data_by_tract contains a three-tuple of the tract feature, properties
        # of the tract, and the proportion of the tract that overlaps with the
        # ward. Multiply the tract figure by the overlap in order to estimate
        # the portion of the value that belongs to the ward.
        count = sum(tract_data[table] * percent_overlap for _, tract_data, percent_overlap in data_by_tract)

        table_values.append(round(count, 0))

        writer.writerow([community_area, zipcode, *table_values])
