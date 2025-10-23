# Upgrade Databricks SDK to the latest version and restart Python to see updated packages
%pip install --upgrade databricks-sdk==0.68.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job


tpch_query = Job.from_dict(
    {
        "name": "tpch_query",
        "tasks": [
            {
                "task_key": "tpch_query",
                "notebook_task": {
                    "notebook_path": "/Workspace/Repos/tpch100_db/tpch100_db/transform/run_tpch_queries",
                    "source": "WORKSPACE",
                },
            },
        ],
        "job_clusters": [
            {
                "job_cluster_key": "d4sv3_11c2d680",
                "new_cluster": {
                    "spark_version": "17.3.x-scala2.13",
                    "azure_attributes": {
                        "availability": "SPOT_AZURE",
                        "spot_bid_max_price": 100
                    },
                    "node_type_id": "Standard_D4s_v3",
                    "custom_tags": {
                        "resource_type": "d4sv3_1w_tot_8c_32g",
                        "job_cluster_key": "d4sv3_11c2d680"
                    },
                    "policy_id": "000B459B335BC2B2",
                    "data_security_mode": "DATA_SECURITY_MODE_AUTO",
                    "runtime_engine": "STANDARD",
                    "kind": "CLASSIC_PREVIEW",
                    "num_workers": 1
                },
            },
        ],
        "tags": {
            "cluster_name": "d4sv3_1w_tot_8c_32g",
            "resource_type": "d4sv3_1w_tot_8c_32g",
        },
        "queue": {
            "enabled": True,
        },
        "parameters": [
            {
                "name": "CATALOG",
                "default": "1",
            },
            {
                "name": "SCHEMA",
                "default": "1",
            },
            {
                "name": "SCALE",
                "default": "0",
            },
            {
                "name": "Q_NUM",
                "default": "0",
            },
            {
                "name": "PROFILE",
                "default": "1",
            },
            {
                "name": "PROFILE_DTL",
                "default": "1",
            },
        ],
        "performance_target": "PERFORMANCE_OPTIMIZED",
    }
)

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.jobs.reset(new_settings=tpch_query, job_id=171430988934981)


# or create a new job using: w.jobs.create(**tpch_query.as_shallow_dict())

