
import datetime
spark.sql("USE CATALOG workspace")
spark.sql("USE SCHEMA tpch100_db")

tables = [
    "nation", "region", "part", "supplier",
    "partsupp", "customer", "orders", "lineitem"
]
for table in tables:
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') } starting {table}")
    if table in ["lineitem, orders"]:
        df = spark.read.table(f"tpch100_db.{table}").repartition(200)
    else:
        df = spark.read.table(f"tpch100_db.{table}")
    df.write.insertInto(f"greyhill.{table}")
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') } loaded {table}")