import os
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import jobs
from util.util_functions import watch_job_id

w = WorkspaceClient()

# Copy job id: CreateResponse(job_id=408833111205762)
# Tpch job id: CreateResponse(job_id=562761924288400)

### datagen job
response = w.jobs.run_now(job_id=322338326675003 , 
                    job_parameters = {
                        "CATALOG": "workspace",
                        "SCHEMA": "tpch100_db",
                        "SCALE": 100,
                        "PROFILE": "datagen",
                        "PROFILE_DTL": "d4sv3_single_tot_4c_16g"
                    })
watch_job_id(w, response.run_id)

### Ingestion COPY job
# response = w.jobs.run_now(job_id=408833111205762 , 
#                     job_parameters = {
#                         "CATALOG": "workspace",
#                         "SCHEMA": "tpch100_db",
#                         "SCALE": 100,
#                         "PROFILE": "batch_ingest",
#                         "PROFILE_DTL": "d4sv3_single_tot_4c_16g"
#                     })
# watch_job_id(w, response.run_id)

### Iterate thru each tpch_query and submit as separate job.
# for i in range(1,23):
#     response = w.jobs.run_now(job_id=562761924288400 , 
#                         job_parameters = {"CATALOG": "workspace",
#                                             "SCHEMA": "tpch100_db",
#                                             "SCALE": 100,
#                                             "Q_NUM": f"{str(i)}",
#                                             "PROFILE": "batch_aggr",
#                                             "PROFILE_DTL": f"d4sv3_single_tot_4c_16g_qnum{str(i)}"
#                                             }              
#                         )
#     print(f"Job {i} submitted.")      
#     watch_job_id(w, response.run_id) 
    

#- end of script                    