from urllib import response
from databricks.sdk.service.compute import ClusterSpec
import uuid

d4sv3_single_tot_4c_16g = ClusterSpec.from_dict({
                            "data_security_mode": "DATA_SECURITY_MODE_AUTO",
                            "custom_tags": {
                                "resource_type": "d4sv3_single_tot_4c_16g",
                                "job_cluster_key": "d4sv3"+"_"+str(uuid.uuid1())[:8]
                            },
                            "kind": "CLASSIC_PREVIEW",
                            "azure_attributes": {
                                "availability": "SPOT_WITH_FALLBACK_AZURE"
                            },
                            "runtime_engine": "STANDARD",
                            "spark_version": "16.4.x-scala2.12",
                            "node_type_id": "Standard_D4s_v3",
                            "is_single_node": True
                        })

d4sv3_1w_tot_8c_32g = ClusterSpec.from_dict({
                            "data_security_mode": "DATA_SECURITY_MODE_AUTO",
                            "custom_tags": {
                                "resource_type": "d4sv3_1w_tot_8c_32g",
                                "job_cluster_key": "d4sv3"+"_"+str(uuid.uuid1())[:8]
                            },
                            "kind": "CLASSIC_PREVIEW",
                            "azure_attributes": {
                                "availability": "SPOT_AZURE"
                            },
                            "runtime_engine": "STANDARD",
                            "spark_version": "16.4.x-scala2.12",
                            "node_type_id": "Standard_D4s_v3",
                            "is_single_node": False,
                            "num_workers": 1
                        })

d4sv3_2w_tot_12c_48g = ClusterSpec.from_dict({
                            "data_security_mode": "DATA_SECURITY_MODE_AUTO",
                            "custom_tags": {
                                "resource_type": "d4sv3_2w_tot_12c_48g",
                                "job_cluster_key": "d4sv3"+"_"+str(uuid.uuid1())[:8]
                            },
                            "kind": "CLASSIC_PREVIEW",
                            "azure_attributes": {
                                "availability": "SPOT_AZURE"
                            },
                            "runtime_engine": "STANDARD",
                            "spark_version": "17.3.x-scala2.13",
                            "node_type_id": "Standard_D4s_v3",
                            "is_single_node": False,
                            "num_workers": 2,
                            "spark_conf": {
                                "spark.sql.shuffle.partitons": "360",
                                "spark.databricks.io.cache.enabled": "true",
                                "spark.sql.adaptive.enabled":  "true",
                            }
                        })

d8sv3_single_8c_32g = ClusterSpec.from_dict({
                            "data_security_mode": "DATA_SECURITY_MODE_AUTO",
                            "custom_tags": {
                                "resource_type": "d8sv3_single_8c_32g",
                                "job_cluster_key": "d8sv3"+"_"+str(uuid.uuid1())[:8]
                            },
                            "kind": "CLASSIC_PREVIEW",
                            "azure_attributes": {
                                "availability": "SPOT_AZURE"
                            },
                            "runtime_engine": "STANDARD",
                            "spark_version": "17.3.x-scala2.13",
                            "node_type_id": "Standard_D8s_v3",
                            "is_single_node": True,
                            "spark_conf": {
                                "spark.sql.shuffle.partitons": "360",
                                "spark.databricks.io.cache.enabled": "true",
                                "spark.sql.adaptive.enabled":  "true",
                            }
                        })

d16sv3_single_16c_64g = ClusterSpec.from_dict({
                            "data_security_mode": "DATA_SECURITY_MODE_AUTO",
                            "custom_tags": {
                                "resource_type": "d16sv3_single_16c_64g",
                                "job_cluster_key": "d16sv3"+"_"+str(uuid.uuid1())[:8]
                            },
                            "kind": "CLASSIC_PREVIEW",
                            "azure_attributes": {
                                "availability": "SPOT_AZURE"
                            },
                            "runtime_engine": "STANDARD",
                            "spark_version": "17.3.x-scala2.13",
                            "node_type_id": "Standard_D16s_v3",
                            "is_single_node": True,
                            "spark_conf": {
                                "spark.sql.shuffle.partitons": "360",
                                "spark.databricks.io.cache.enabled": "true",
                                "spark.sql.adaptive.enabled":  "true",
                            }
                        })

# from databricks.sdk import WorkspaceClient
# w = WorkspaceClient()
# response = w.clusters.spark_versions()
# for ver in response.versions:
#     if ver.key.startswith("17"):
#         print(ver.key, ver.name)