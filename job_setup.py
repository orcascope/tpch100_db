from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import JobSettings as Job
from databricks.sdk.service.jobs import JobCluster
import os
from setup.cluster_spec import *

cluster_spec = d4sv3_1w_tot_8c_32g
cluster_name = cluster_spec.as_dict()['custom_tags']['resource_type']                        
job_cluster_key= cluster_spec.as_dict()['custom_tags']['job_cluster_key'] 

copy_job = Job.from_dict(
    {
        "name": "copy_ingest_tpch_concurrent",
        "tasks": [
            {
                "task_key": "copy_ingest",
                "notebook_task": {
                    "notebook_path": "/Workspace/Repos/tpch100_db/tpch100_db/transform/copy_ingest_concurrent",
                    "source": "WORKSPACE"
                },
                ## this matters to assign the cluster to task.
                "job_cluster_key": job_cluster_key
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
            {"name": "SCALE", "default": "100"},
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
                    "notebook_path": "/Workspace/Repos/tpch100_db/tpch100_db/transform/run_tpch_queries",
                    "source": "WORKSPACE"
                },
                "job_cluster_key": job_cluster_key 
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
            {"name": "SCALE", "default": "100"},
            {"name": "Q_NUM", "default": "0"},
            {"name": "PROFILE", "default": "1"},
            {"name": "PROFILE_DTL", "default": "1"}
        ]
    }
)

cluster_spec = d4sv3_1w_tot_8c_32g
cluster_name = cluster_spec.as_dict()['custom_tags']['resource_type']                        
job_cluster_key= cluster_spec.as_dict()['custom_tags']['job_cluster_key'] 

tpch_query_concurrent_job = Job.from_dict(
    {
        "name": "tpch_query_concurrent",
        "tasks": [
            {
                "task_key": "tpch_query_concurrent",
                "notebook_task": {
                    "notebook_path": "/Workspace/Repos/tpch100_db/tpch100_db/transform/run_tpch_queries_concurrent",
                    "source": "WORKSPACE"
                },
                "job_cluster_key": job_cluster_key 
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
            {"name": "MAX_WORKERS", "default": "0"},
            {"name": "PROFILE", "default": "1"},
            {"name": "PROFILE_DTL", "default": "1"},
            {"name": "DESC", "default": "0"}
        ]
    }
)

cluster_spec = d4sv3_2w_tot_12c_48g
cluster_name = cluster_spec.as_dict()['custom_tags']['resource_type']                        
job_cluster_key= cluster_spec.as_dict()['custom_tags']['job_cluster_key'] 

tpch_query_conc_2wrkr_job = Job.from_dict(
    {
        "name": "tpch_query_conc_2wrkr",
        "tasks": [
            {
                "task_key": "tpch_query_conc_2wrkr",
                "notebook_task": {
                    "notebook_path": "/Workspace/Repos/tpch100_db/tpch100_db/transform/run_tpch_queries_concurrent",
                    "source": "WORKSPACE"
                },
                "job_cluster_key": job_cluster_key 
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
            {"name": "MAX_WORKERS", "default": "0"},
            {"name": "PROFILE", "default": "1"},
            {"name": "PROFILE_DTL", "default": "1"},
            {"name": "DESC", "default": "0"}
        ]
    }
)

w = WorkspaceClient()
# copy_job_id = w.jobs.create(**copy_job.as_shallow_dict())
# print(f"Copy job id: {copy_job_id}")

tpch_job_id = w.jobs.create(**tpch_query_conc_2wrkr_job.as_shallow_dict())
print(f"tpch_query_conc_2wrkr_job id: {tpch_job_id}")

# tpch_job_concurrent_id = w.jobs.update(job_id=963957780768035,
#                 new_settings = tpch_query_concurrent_job)
# print(f"Tpch job concur id: {tpch_job_concurrent_id}")

# end of script



#end of page