
spark.sql("USE CATALOG workspace")
spark.sql("USE SCHEMA tpch100_db")

tables = [
    "nation", "region", "part", "supplier",
    "partsupp", "customer", "orders", "lineitem"
]
for table in tables:
    df = spark.read.format("delta").load(f"tpch100_db.{table}")
    df.write.insertInto(f"greyhill.{table}")
