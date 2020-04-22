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
writer.writerow(['community_area', 'ward', *tables])

c = Census(CENSUS_API_KEY)

for feature in json.load(sys.stdin):
    community_area = feature['properties']['community_area'].title()
    ward = feature['properties']['ward']

    table_values = []

    for table in tables:
        data_by_tract = c.acs5.geo_tract(('NAME', table), feature)
        count = sum(tract_data[table] for _, tract_data, _ in data_by_tract)

        table_values.append(count)

    writer.writerow([community_area, ward, *table_values])
