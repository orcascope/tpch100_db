from databricks.sdk import WorkspaceClient
from databricks.sdk.service import jobs
from util.util_functions import watch_job_id

w = WorkspaceClient()

### datagen job
# response = w.jobs.run_now(job_id=322338326675003 , 
#                     job_parameters = {
#                         "CATALOG": "workspace",
#                         "SCHEMA": "tpch100_db",
#                         "SCALE": 100,
#                         "PROFILE": "datagen",
#                         "PROFILE_DTL": "d4sv3_single_tot_4c_16g"
#                     })
# watch_job_id(w, response.run_id)

# Copy job id: CreateResponse(job_id=735284953891071)
# Tpch job id: CreateResponse(job_id=29645532917253)
### Ingestion COPY job
# response = w.jobs.run_now(job_id=735284953891071 , 
#                     job_parameters = {
#                         "CATALOG": "workspace",
#                         "SCHEMA": "tpch100_db",
#                         "SCALE": 100,
#                         "PROFILE": "batch_ingest",
#                         "PROFILE_DTL": "d4sv3_1w_tot_8c_32g_ingest_copy_concurrent"
#                     })
# watch_job_id(w, response.run_id)

### Iterate thru each tpch_query and submit as separate job.
# for i in range(1, 23):
#     response = w.jobs.run_now(job_id=285229417579798 , 
#                         job_parameters = {"CATALOG": "workspace",
#                                             "SCHEMA": "tpch100_db",
#                                             "SCALE": 100,
#                                             "Q_NUM": f"{str(i)}",
#                                             "PROFILE": "batch_aggr",
#                                             "PROFILE_DTL": f"d4sv3_1w_tot_8c_32g_qnum{str(i)}_after_concurrent_copy"
#                                             }              
#                         )    
#     watch_job_id(w, response.run_id) 
    
#Run all queries concurrently in a single job run
#tpch_query_conc_2wrkr_job id: CreateResponse(job_id=64363532768096)
# tpch_query_duck id: CreateResponse(job_id=963764923699891)
# tpch_query_duck_16c_64g id: CreateResponse(job_id=345438643830368)
response = w.jobs.run_now(job_id=345438643830368 , 
                    job_parameters = {"CATALOG": "workspace",
                                        "SCHEMA": "greyhill",
                                        "MAX_WORKERS": "1",
                                        "PROFILE": "batch_aggr",
                                        "PROFILE_DTL": f"d16sv3_single_tot_16c_64g_duck",
                                        "DESC": """Running all queries concurrently with 1 worker. 
                                                Using d16sv3_single_16c_64g cluster.
                                                DuckDB with Delta Lake ATTACH for storage access.
                                                """
                                        }              
                    )    
watch_job_id(w, response.run_id) 

#- end of script                    