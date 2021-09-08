FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update
RUN apt-get -y upgrade

RUN apt install -y python3-pip python3-dev postgresql postgresql-contrib libpq-dev jupyter-notebook vim openjdk-8-jdk
RUN pip3 install jupyter ipython-sql psycopg2

ADD Assignment-0/smallRelationsInsertFile.sql Assignment-0/largeRelationsInsertFile.sql Assignment-0/DDL.sql /datatemp/
ADD Assignment-1/populate-sn.sql /datatemp/

EXPOSE 8888
EXPOSE 5432

USER postgres

RUN /etc/init.d/postgresql start &&\
    createdb university &&\
    psql --command "\i /datatemp/DDL.sql;" university &&\
    psql --command "\i /datatemp/smallRelationsInsertFile.sql;" university &&\
    psql --command "alter user postgres with password 'postgres';" university &&\
    createdb socialnetwork &&\
    psql --command "\i /datatemp/populate-sn.sql;" socialnetwork 
