import time
def watch_job_id(workspace, run_id):
    job_run_resp = workspace.jobs.get_run(run_id=run_id)
    print(f" Job Status ",job_run_resp.state.life_cycle_state.value)
    print(f" Job Params ",job_run_resp.job_parameters)
    while True:
        job_run_resp = workspace.jobs.get_run(run_id=run_id)
        if job_run_resp.state.life_cycle_state.value in ["INTERNAL_ERROR", "TERMINATED", "SKIPPED", "TERMINATING"]:
            break
        time.sleep(10)
    print(f" Job Status ",job_run_resp.state.life_cycle_state.value)