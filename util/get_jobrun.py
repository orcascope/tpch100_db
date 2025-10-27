# ...existing code...
import re
from databricks.sdk import WorkspaceClient
from databricks.sdk.service import jobs
import datetime
import json

w = WorkspaceClient()

run_id_list = [642138342309952,
981048324540200,
222903888417673,
222903888417673,
807407784886795,
529824949354019,
812068169785503,
105517411451052,
628093778830316,
628093778830316,
192034966929427,
12613702183315,
366407825161942,
816246483494874,
766526162713280,
340576208576819,
259800519608464,
573215555503660,
573215555503660,
989042071963859,
1112327203797671,
377142897911703,
750166025944524,
1084734025023123,
1030005675026722,
61969756674894,
1053108489080466,
1053108489080466,
830882571063009
]



def _get_field(obj, key):
    # try attribute then dict-style access
    if obj is None:
        return None
    if hasattr(obj, key):
        return getattr(obj, key)
    try:
        return obj.get(key)
    except Exception:
        return None

def _to_iso_ms(ms):
    if ms is None:
        return None
    try:
        # sample payload uses milliseconds since epoch
        return datetime.datetime.fromtimestamp(ms / 1000.0, tz=datetime.timezone.utc).isoformat()
    except Exception:
        return None

def _to_dict_maybe(obj):
    if obj is None:
        return None
    if isinstance(obj, dict):
        return obj
    # databricks-sdk models may expose attributes
    try:
        return {k: v for k, v in vars(obj).items() if not k.startswith("_")}
    except Exception:
        return str(obj)

# extract fields
def get_job_run_details(run_dtl):
    execution_duration = _get_field(run_dtl, "execution_duration")
    setup_duration = _get_field(run_dtl, "setup_duration")
    start_time_ms = _get_field(run_dtl, "start_time")

    job_id = _get_field(run_dtl, "job_id")
    run_id = _get_field(run_dtl, "run_id")
    run_name = _get_field(run_dtl, "run_name")

    # job_parameters may be list of {name,value}
    raw_params = _get_field(run_dtl, "job_parameters")
    if isinstance(raw_params, list):
        job_parameters = {p.name: p.value for p in raw_params}
    else:
        job_parameters = _to_dict_maybe(raw_params)

    # state and status
    state = (_get_field(run_dtl, "state"))
    status =(_get_field(run_dtl, "status"))

    result = {
        "execution_duration_min": execution_duration/1000/60,
        "setup_duration_min": setup_duration/1000/60,
        "start_time_iso": _to_iso_ms(start_time_ms),
        "job_id": job_id,
        "run_id": run_id,
        "PROFILE": job_parameters["PROFILE"],
        "PROFILE_DTL": job_parameters["PROFILE_DTL"],
        "state": state.life_cycle_state.value ,
        "status": status.termination_details.code.value,
        "run_name": run_name
    }
    return result

# print(json.dumps(result, indent=2))

with open('util/jobrun_dtl.json', 'w') as f:
    for run_id in set(run_id_list):
        run_dtl = w.jobs.get_run(run_id)
        result = get_job_run_details(run_dtl)
        f.write(json.dumps(result) + "\n")
    f.close()