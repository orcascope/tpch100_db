-- ...existing code...
Use Catalog workspace;
USE SCHEMA tpch100_db;

COPY INTO nation
BY POSITION
FROM 's3://clickhouse-datasets/h/100/nation.tbl.gz'
FILEFORMAT = CSV
FORMAT_OPTIONS ('sep'='|');

COPY INTO region
BY POSITION
FROM 's3://clickhouse-datasets/h/100/region.tbl.gz'
FILEFORMAT = CSV
FORMAT_OPTIONS ('sep'='|');

COPY INTO part
BY POSITION
FROM 's3://clickhouse-datasets/h/100/part.tbl.gz'
FILEFORMAT = CSV
FORMAT_OPTIONS ('sep'='|');

COPY INTO supplier
BY POSITION
FROM 's3://clickhouse-datasets/h/100/supplier.tbl.gz'
FILEFORMAT = CSV
FORMAT_OPTIONS ('sep'='|');

COPY INTO partsupp
BY POSITION
FROM 's3://clickhouse-datasets/h/100/partsupp.tbl.gz'
FILEFORMAT = CSV
FORMAT_OPTIONS ('sep'='|');

COPY INTO customer
BY POSITION
FROM 's3://clickhouse-datasets/h/100/customer.tbl.gz'
FILEFORMAT = CSV
FORMAT_OPTIONS ('sep'='|');

COPY INTO orders
BY POSITION
FROM 's3://clickhouse-datasets/h/100/orders.tbl.gz'
FILEFORMAT = CSV
FORMAT_OPTIONS ('sep'='|');

COPY INTO lineitem
BY POSITION
FROM 's3://clickhouse-datasets/h/100/lineitem.tbl.gz'
FILEFORMAT = CSV
FORMAT_OPTIONS ('sep'='|');