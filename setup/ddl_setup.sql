Use Catalog workspace;
CREATE SCHEMA IF NOT EXISTS tpch100_db;
USE SCHEMA tpch100_db

-- nation
DROP TABLE IF EXISTS nation;
CREATE OR REPLACE TABLE nation (
  n_nationkey BIGINT,
  n_name STRING,
  n_regionkey BIGINT,
  n_comment STRING
)
USING DELTA;

-- region
DROP TABLE IF EXISTS region;
CREATE OR REPLACE TABLE region (
  r_regionkey BIGINT,
  r_name STRING,
  r_comment STRING
)
USING DELTA;

-- part
DROP TABLE IF EXISTS part;
CREATE OR REPLACE TABLE part (
  p_partkey BIGINT,
  p_name STRING,
  p_mfgr STRING,
  p_brand STRING,
  p_type STRING,
  p_size BIGINT,
  p_container STRING,
  p_retailprice DOUBLE,
  p_comment STRING
)
USING DELTA;

-- supplier
DROP TABLE IF EXISTS supplier;
CREATE OR REPLACE TABLE supplier (
  s_suppkey BIGINT,
  s_name STRING,
  s_address STRING,
  s_nationkey BIGINT,
  s_phone STRING,
  s_acctbal DOUBLE,
  s_comment STRING
)
USING DELTA;

-- partsupp
DROP TABLE IF EXISTS partsupp;
CREATE OR REPLACE TABLE partsupp (
  ps_partkey BIGINT,
  ps_suppkey BIGINT,
  ps_availqty BIGINT,
  ps_supplycost DOUBLE,
  ps_comment STRING
)
USING DELTA;

-- customer
DROP TABLE IF EXISTS customer;
CREATE OR REPLACE TABLE customer (
  c_custkey BIGINT,
  c_name STRING,
  c_address STRING,
  c_nationkey BIGINT,
  c_phone STRING,
  c_acctbal DOUBLE,
  c_mktsegment STRING,
  c_comment STRING
)
USING DELTA;

-- orders (partitioning by order date for better date-range query performance)
DROP TABLE IF EXISTS orders;
CREATE OR REPLACE TABLE orders (
  o_orderkey BIGINT,
  o_custkey BIGINT,
  o_orderstatus STRING,
  o_totalprice DOUBLE,
  o_orderdate DATE,
  o_orderpriority STRING,
  o_clerk STRING,
  o_shippriority BIGINT,
  o_comment STRING
)
USING DELTA;

-- lineitem (partition by ship date)
DROP TABLE IF EXISTS lineitem;
CREATE OR REPLACE TABLE lineitem (
  l_orderkey BIGINT,
  l_partkey BIGINT,
  l_suppkey BIGINT,
  l_linenumber BIGINT,
  l_quantity DOUBLE,
  l_extendedprice DOUBLE,
  l_discount DOUBLE,
  l_tax DOUBLE,
  l_returnflag STRING,
  l_linestatus STRING,
  l_shipdate DATE,
  l_commitdate DATE,
  l_receiptdate DATE,
  l_shipinstruct STRING,
  l_shipmode STRING,
  l_comment STRING
)
USING DELTA;

-- end of line
