%pip install databricks-sdk==0.68.0
%restart_python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import JobSettings as Job
from databricks.sdk.service.jobs import JobCluster
import os
from setup.cluster_spec import *

cluster_spec = d4sv3_single_tot_4c_16g
cluster_name = cluster_spec.as_dict()['custom_tags']['resource_type']                        
job_cluster_key= cluster_spec.as_dict()['custom_tags']['job_cluster_key'] 

copy_job = Job.from_dict(
    {
        "name": "copy_ingest_tpch",
        "tasks": [
            {
                "task_key": "copy_ingest",
                "notebook_task": {
                    "notebook_path": os.path.abspath("./transform/copy_ingest"),
                    "source": "WORKSPACE"
                }
            }
        ],
        "queue": {
            "enabled": True,
        },
        "job_clusters" : [JobCluster.from_dict(
            {"job_cluster_key": job_cluster_key, 
             "new_cluster":cluster_spec.as_dict()
            }).as_dict() 
        ],
        "tags": {
            "resource_type": cluster_name,
            "cluster_name": cluster_name
        },
        "parameters": [
            {"name": "CATALOG", "default": "1"},
            {"name": "SCHEMA", "default": "1"},
            {"name": "SCALE", "default": "0"},
            {"name": "PROFILE", "default": "1"},
            {"name": "PROFILE_DTL", "default": "1"}
        ]
    }
)

cluster_spec = d4sv3_1w_tot_8c_32g
cluster_name = cluster_spec.as_dict()['custom_tags']['resource_type']                        
job_cluster_key= cluster_spec.as_dict()['custom_tags']['job_cluster_key'] 

tpch_query_job = Job.from_dict(
    {
        "name": "tpch_query",
        "tasks": [
            {
                "task_key": "tpch_query",
                "notebook_task": {
                    "notebook_path": os.path.abspath("./transform/run_tpch_queries"),
                    "source": "WORKSPACE"
                }
            }
        ],
        "queue": {
            "enabled": True,
        },
        "job_clusters" : [JobCluster.from_dict(
            {"job_cluster_key": job_cluster_key, 
             "new_cluster":cluster_spec.as_dict()
            }).as_dict() 
        ],
        "tags": {
            "resource_type": cluster_name,
            "cluster_name": cluster_name
        },
        "parameters": [
            {"name": "CATALOG", "default": "1"},
            {"name": "SCHEMA", "default": "1"},
            {"name": "SCALE", "default": "0"},
            {"name": "Q_NUM", "default": "0"},
            {"name": "PROFILE", "default": "1"},
            {"name": "PROFILE_DTL", "default": "1"}
        ]
    }
)

w = WorkspaceClient()
# copy_job_id = w.jobs.create(**copy_job.as_shallow_dict())
# print(f"Copy job id: {copy_job_id}")

tpch_job_id = w.jobs.create(**tpch_query_job.as_shallow_dict())
print(f"Tpch job id: {tpch_job_id}")

# end of script



#end of page