# base image
FROM python:3.7

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONBUFFERED 1

#directory to store app source code
RUN mkdir /Cerrera

#switch to /app directory so that everything runs from here
WORKDIR /Cerrera


#copy the app code to image working directory
COPY ./Cerrera /Cerrera

RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  nano\
  build-essential \
  gdal-bin \
  libgdal-dev \
  redis-server \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*


#let pip install required packages
RUN pip install -r requirements.txt

COPY Cerrera/runserv.sh ./runserv.sh
RUN chmod +x ./runserv.sh
