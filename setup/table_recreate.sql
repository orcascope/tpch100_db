CREATE TABLE orders (
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
CLUSTER BY (o_orderdate, o_orderkey)
USING DELTA;


CREATE TABLE lineitem (
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
CLUSTER BY (l_shipdate, l_orderkey)
USING DELTA;

