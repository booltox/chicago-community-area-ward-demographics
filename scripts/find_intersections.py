'''
Expected input: Name of Chicago community area and comma-separated list of
wards that intersect.

Expected output: Array of GeoJSON-like objects with "community_area" and "ward"
properties.
'''
import json
import os
import sys

from osgeo import ogr


# Default to Hermosa and its wards.
community_area = os.environ.get('COMMUNITY_AREA', 'Hermosa')
wards = os.environ.get('WARDS', '26,31,35,36')

pwd = os.path.abspath(os.path.dirname(__file__))

def feature_from_array(array, prop, value):
    '''
    Return feature with the given property value from an array of features.
    Raise an exception if a matching feature cannot be found, or if more than
    one feature matches the given property value
    '''
    try:
        feature, = [f for f in array if f['properties'][prop].lower() == value.lower()]

    except ValueError as e:
        if 'need more than 0 values' in str(e):
            raise ValueError('Could not find feature with {0} "{1}"'.format(prop, value))
        elif 'too many values' in str(e):
            raise ValueError('Found multiple features with {0} "{1}"'.format(prop, value))
        else:
            raise

    else:
        return feature

with open(os.path.join(pwd, '..', 'raw', 'chicago_community_areas.geojson'), 'r') as f:
    ca_geojson = json.load(f)

    ca_feature = feature_from_array(ca_geojson['features'], 'community', community_area)

    ca_geom = ogr.CreateGeometryFromJson(
        json.dumps(ca_feature['geometry'])
    )

intersections = []

with open(os.path.join(pwd, '..', 'raw', 'chicago_wards.geojson'), 'r') as f:
    ward_geojson = json.load(f)

    for ward in wards.split(','):
        ward_feature = feature_from_array(ward_geojson['features'], 'ward', ward)

        ward_geom = ogr.CreateGeometryFromJson(
            json.dumps(ward_feature['geometry'])
        )

        intersection = json.loads(ca_geom.Intersection(ward_geom).ExportToJson())

        intersection['properties'] = {
            'community_area': community_area,
            'ward': ward,
        }

        intersections.append(intersection)

sys.stdout.write(json.dumps(intersections, indent=2))
