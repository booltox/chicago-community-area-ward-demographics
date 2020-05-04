.INTERMEDIATE : intersections_ward.json

.INTERMEDIATE : intersections_zip.json


all : finished/population_by_ward.csv finished/population_by_zipcode.csv

clean :
	rm -f finished/* || echo 'Nothing to clean up!'

finished/population_by_ward.csv : intersections_ward.json
	python scripts/calculate_demographics.py < $^ > $@

finished/population_by_zipcode.csv : intersections_zip.json
	python scripts/calculate_demographics_zipcode.py < $^ > $@

intersections_ward.json : raw/chicago_wards.geojson raw/chicago_community_areas.geojson
	python scripts/find_intersections.py > $@

intersections_zip.json : raw/chicago_community_areas.geojson raw/chicago_zipcodes.geojson
	python scripts/find_intersections_zip.py > $@

raw/chicago_wards.geojson :
	wget -O $@ --no-use-server-timestamps \
		https://data.cityofchicago.org/api/geospatial/sp34-6z76?method=export\&format=GeoJSON

raw/chicago_community_areas.geojson :
	wget -O $@ --no-use-server-timestamps \
		https://data.cityofchicago.org/api/geospatial/cauq-8yn6?method=export\&format=GeoJSON

raw/chicago_zipcodes.geojson :
	wget -O $@ --no-use-server-timestamps \
		https://data.cityofchicago.org/api/geospatial/gdcf-axmw?method=export\&format=GeoJSON
