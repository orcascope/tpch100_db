### %pip install databricks-sdk==0.68.0
### %restart_python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import JobSettings as Job
from databricks.sdk.service.jobs import JobCluster
import os
from setup.cluster_spec import *

cluster_spec = d4sv3_single_tot_4c_16g
cluster_name = cluster_spec.as_dict()['custom_tags']['resource_type']                        
job_cluster_key= cluster_spec.as_dict()['custom_tags']['job_cluster_key'] 

datagen_job = Job.from_dict(
    {
        "name": "datagen_tpch",
        "tasks": [
            {
                "task_key": "datagen_tpch",
                "notebook_task": {
                    "notebook_path": os.path.abspath("/Workspace/Repos/tpch100_db/tpch100_db/setup/tpchgen"),
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
            {"name": "SCALE", "default": "0"},
            {"name": "PROFILE", "default": "1"},
            {"name": "PROFILE_DTL", "default": "1"}
        ]
    }
)


w = WorkspaceClient()
datagen_job_id = w.jobs.create(**datagen_job.as_shallow_dict())
print(f"datagen_job id: {datagen_job_id}")


# end of script



#end of page