.INTERMEDIATE : intersections.json

all : finished/population_by_ward.csv

clean :
	rm -f finished/* || echo 'Nothing to clean up!'

finished/population_by_ward.csv : intersections.json
	python scripts/calculate_demographics.py < $^ > $@

intersections.json : raw/chicago_wards.geojson raw/chicago_community_areas.geojson
	python scripts/find_intersections.py > $@

raw/chicago_wards.geojson :
	wget -O $@ --no-use-server-timestamps \
		https://data.cityofchicago.org/api/geospatial/sp34-6z76?method=export\&format=GeoJSON

raw/chicago_community_areas.geojson :
	wget -O $@ --no-use-server-timestamps \
		https://data.cityofchicago.org/api/geospatial/cauq-8yn6?method=export\&format=GeoJSON
