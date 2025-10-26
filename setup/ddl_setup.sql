Use Catalog workspace;
CREATE SCHEMA IF NOT EXISTS tpch100_db;
USE SCHEMA tpch100_db;

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
  p_size INT,
  p_container STRING,
  p_retailprice DECIMAL(15,2),
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
  s_acctbal DECIMAL(15,2),
  s_comment STRING
)
USING DELTA;

-- partsupp
DROP TABLE IF EXISTS partsupp;
CREATE OR REPLACE TABLE partsupp (
  ps_partkey BIGINT,
  ps_suppkey BIGINT,
  ps_availqty INT,
  ps_supplycost DECIMAL(15,2),
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
  c_acctbal DECIMAL(15,2),
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
  o_totalprice DECIMAL(15,2),
  o_orderdate DATE,
  o_orderpriority STRING,
  o_clerk STRING,
  o_shippriority INT,
  o_comment STRING
)
USING DELTA;

-- lineitem (partition by ship date)
DROP TABLE IF EXISTS lineitem;
CREATE OR REPLACE TABLE lineitem (
  l_orderkey BIGINT,
  l_partkey BIGINT,
  l_suppkey BIGINT,
  l_linenumber INT,
  l_quantity DECIMAL(15,2),
  l_extendedprice DECIMAL(15,2),
  l_discount DECIMAL(15,2),
  l_tax DECIMAL(15,2),
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
