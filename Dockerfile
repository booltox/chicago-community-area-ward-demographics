FROM andrejreznik/python-gdal:py3.7.3-gdal3.0.0
LABEL maintainer "DataMade <info@datamade.us>"

RUN apt-get update && \
    apt-get install -y wget make

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app