FROM python:3.6-buster

RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt update && apt install -y postgresql-13

USER postgres
RUN service postgresql start \
  && createdb -O postgres kw_db \
  && sed -i -r 's/(local\s*all\s*postgres\s*)peer/\1trust/' /etc/postgresql/13/main/pg_hba.conf \
  && echo "host all  all    0.0.0.0/0  trust" >> /etc/postgresql/13/main/pg_hba.conf \
  && echo "listen_addresses='*'" >> /etc/postgresql/13/main/postgresql.conf
USER root

WORKDIR /app
COPY ./app ./
RUN yes | pip install faker numpy pandas psycopg2 sqlalchemy
RUN service postgresql start \
  && python ./dummy_data/main.py

CMD ["sh", "./start.sh"]