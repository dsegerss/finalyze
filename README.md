# finalyze
An experimental stock market analysis and prediction sandbox



Database
--------

Create a postgresql database and add timescaledb extension:

psql -d postgres
postgres=# create database finalyze;
postgres=# CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;
