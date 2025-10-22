-- ...existing code...

/* Create database (local filesystem paths). Adjust locations if you use a different root (e.g. cloud storage). */
Use Catalog workspace;
CREATE SCHEMA IF NOT EXISTS tpch100_db

-- nation
CREATE TABLE IF NOT EXISTS tpch100_db.nation (
  n_nationkey INT,
  n_name STRING,
  n_regionkey INT,
  n_comment STRING
)
USING DELTA;

-- region
CREATE TABLE IF NOT EXISTS tpch100_db.region (
  r_regionkey INT,
  r_name STRING,
  r_comment STRING
)
USING DELTA;

-- part
CREATE TABLE IF NOT EXISTS tpch100_db.part (
  p_partkey INT,
  p_name STRING,
  p_mfgr STRING,
  p_brand STRING,
  p_type STRING,
  p_size INT,
  p_container STRING,
  p_retailprice DOUBLE,
  p_comment STRING
)
USING DELTA;

-- supplier
CREATE TABLE IF NOT EXISTS tpch100_db.supplier (
  s_suppkey INT,
  s_name STRING,
  s_address STRING,
  s_nationkey INT,
  s_phone STRING,
  s_acctbal DOUBLE,
  s_comment STRING
)
USING DELTA;

-- partsupp
CREATE TABLE IF NOT EXISTS tpch100_db.partsupp (
  ps_partkey INT,
  ps_suppkey INT,
  ps_availqty INT,
  ps_supplycost DOUBLE,
  ps_comment STRING
)
USING DELTA;

-- customer
CREATE TABLE IF NOT EXISTS tpch100_db.customer (
  c_custkey INT,
  c_name STRING,
  c_address STRING,
  c_nationkey INT,
  c_phone STRING,
  c_acctbal DOUBLE,
  c_mktsegment STRING,
  c_comment STRING
)
USING DELTA;

-- orders (partitioning by order date for better date-range query performance)
CREATE TABLE IF NOT EXISTS tpch100_db.orders (
  o_orderkey INT,
  o_custkey INT,
  o_orderstatus STRING,
  o_totalprice DOUBLE,
  o_orderdate DATE,
  o_orderpriority STRING,
  o_clerk STRING,
  o_shippriority INT,
  o_comment STRING
)
USING DELTA;

-- lineitem (partition by ship date)
CREATE TABLE IF NOT EXISTS tpch100_db.lineitem (
  l_orderkey INT,
  l_partkey INT,
  l_suppkey INT,
  l_linenumber INT,
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


