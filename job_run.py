import os
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import jobs

w = WorkspaceClient()

# Copy job id: CreateResponse(job_id=328286763733530)
# Tpch job id: CreateResponse(job_id=440635001741416)

# copy_response = w.jobs.run_now(job_id=328286763733530 , 
#                     job_parameters = {
#                         "CATALOG": "workspace",
#                         "SCHEMA": "tpch100_db",
#                         "SCALE": 1,
#                         "PROFILE": "batch_ingest",
#                         "PROFILE_DTL": "d4sv3_single_tot_4c_16g"
#                     })

# run_id = copy_response.run_id 
# job_run_resp = w.jobs.get_run(run_id=run_id)
# print(job_run_resp.state.life_cycle_state.value)
# while True:
#     job_run_resp = w.jobs.get_run(run_id=run_id)
#     if job_run_resp.state.life_cycle_state.value in ["INTERNAL_ERROR", "TERMINATED", "SKIPPED", "TERMINATING"]:
#         break
#     time.sleep(10)
# print(job_run_resp.state.life_cycle_state.value)


for i in range(1,5):
    response = w.jobs.run_now(job_id=171430988934981 , 
                        job_parameters = {"CATALOG": "workspace",
                                            "SCHEMA": "tpch100_db",
                                            "SCALE": 1,
                                            "Q_NUM": f"{str(i)}",
                                            "PROFILE": "batch_aggr",
                                            "PROFILE_DTL": f"d4sv3_single_tot_4c_16g_qnum{str(i)}"
                                            }              
                        )
    run_id = response.run_id 
    job_run_resp = w.jobs.get_run(run_id=run_id)
    print(f"Query_{str(i)} Job Status ",job_run_resp.state.life_cycle_state.value)
    while True:
        job_run_resp = w.jobs.get_run(run_id=run_id)
        if job_run_resp.state.life_cycle_state.value in ["INTERNAL_ERROR", "TERMINATED", "SKIPPED", "TERMINATING"]:
            break
        time.sleep(10)
    print(f"Query_{str(i)} Job Status ",job_run_resp.state.life_cycle_state.value)

#- end of script                    