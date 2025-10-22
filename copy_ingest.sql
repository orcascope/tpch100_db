Use Catalog workspace;
USE SCHEMA tpch100_db;

COPY INTO region;
FROM 's3://clickhouse-datasets/h/100/region.tbl.gz'
FILEFORMAT = <format>
FORMAT_OPTIONS ('mergeSchema' = 'true')
COPY_OPTIONS ('mergeSchema' = 'true');