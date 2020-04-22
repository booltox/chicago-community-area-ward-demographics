# 👨‍👩‍👧‍👦 chicago-community-area-ward-demographics

Discover how demographics in your Chicago neighborhood break down by ward.

## What's this?

This repository contains configurable scripts to generate demographic data
from the intersection of Chicago community areas and overlapping wards.

These scripts were developed in support of the **Hermosa Neighborhood
Association**, so they default to calculating the total population of Hermosa
broken down by ward.

You can view the generated dataset [here](finished/population_by_ward.csv).

## Run the scripts yourself

### Requirements

- [Docker](https://www.docker.com/products/docker-desktop)

### Setup

Navigate in your terminal to the directory in which you'd like this code to
live, then clone and `cd` into this repository:

```bash
git clone && cd chicago-community-area-ward-demographics
```

### Usage

#### Get an API key

To retrieve data, first [get a Census API key](https://api.census.gov/data/key_signup.html).

When your key is activated, make a working copy of the secrets file:

```bash
cp scripts/secrets.py.example scripts/secrets.py
```

Replace 'YOUR API KEY' with, what else?, your API key.

#### ♻️ Make the default data afresh

**To remove and remake the default data**, run this in your terminal:

```bash
make clean && docker-compose run --rm data
```

#### 🔍 Customize the scripts

**To retrieve additional tables** from the American Community Survey, consult
the ACS variable definition [here](https://api.census.gov/data/2018/acs/acs5/variables.html).
Once you've identified which tables you'd like, update the value of `ACS_TABLES`
in [line 17 of `docker-compose.yml`](docker-compose.yml#L17). To retrieve
multiple tables, separate them with commas, e.g., `B01001B_005E,B01001B_006E`.

**To retrieve information for a different community area and wards**, update
the values of `COMMUNITY_AREA` and `WARDS` in [lines 15 and 16 of `docker-compose.yml`](docker-compose.yml#L15-16).
Be sure to enclose your community area in quotes if it contains a space, e.g.,
`"Humboldt Park"`.

Once you've made your changes, refresh the data by running the following
command in your terminal:

```bash
make clean && docker-compose run --rm data
```

## Loose ends

Right now, you need to know your community area and the wards it overlaps to use
these scripts. It'd be great if you could plug in a community area and these
scripts would discover the overlapping wards for you!

## Team

* Hannah Cushmand Garland, DataMade

## Errors and bugs

If something is not behaving intuitively, it is a bug and should be reported.
Report it here by creating an issue: https://github.com/datamade/chicago-community-area-ward-demographics/issues

Help us fix the problem as quickly as possible by following [Mozilla's guidelines for reporting bugs.](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines#General_Outline_of_a_Bug_Report)

## Patches and pull requests

Your patches are welcome. Here's our suggested workflow:

* Fork the project.
* Make your feature addition or bug fix.
* Send us a pull request with a description of your work.

## Copyright and attribution

Copyright (c) 2020 DataMade. Released under the [MIT License](https://github.com/datamade/chicago-community-area-ward-demographics/blob/master/LICENSE).
