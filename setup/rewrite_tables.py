spark.sql("ALTER TABLE lineitem SET TBLPROPERTIES ('delta.targetFileSize' = '256MB')") 

df = (spark.sql("""
        select * from lineitem_stage 
        order by l_shipdate, l_orderkey
                """))

df.write.insertInto("lineitem") 

spark.sql("ALTER TABLE orders SET TBLPROPERTIES ('delta.targetFileSize' = '256MB')") 

df = (spark.sql("""
        select * from orders_stage 
        order by o_orderdate, o_orderkey
                """))

df.write.insertInto("orders") 