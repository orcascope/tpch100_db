# tpch100_db
#### Data generation: 
With tpchgen-cli utility. Data was first generated as partitioned parquet file and stored in ADLS storage. https://github.com/orcascope/tpch100_db/blob/main/setup/tpchgen.ipynb

#### Ingestion:
Generated data was ingested into Delta tables using COPY statements - https://github.com/orcascope/tpch100_db/blob/main/transform/copy_ingest_concurrent.ipynb

#### Queries:
Queries were copied from clickhouse page and minor changes made - https://github.com/orcascope/tpch100_db/blob/main/transform/queries.py

#### Running Queries:
Test was performed to run queries over multiThreading workers - https://github.com/orcascope/tpch100_db/blob/main/transform/run_tpch_queries_concurrent.ipynb & https://github.com/orcascope/tpch100_db/blob/main/transform/duck_run_tpch_concur.ipynb 

#### Cluster & JobSetup:
Job Clusters were setup and jobs were executed with databricks python sdk -  https://github.com/orcascope/tpch100_db/blob/main/job_setup.py & https://github.com/orcascope/tpch100_db/blob/main/job_run.py