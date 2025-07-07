What Changed:

-pipeline/interview_job/ops/get_existing_results
Loads the previous output CSV. If it's missing it returns an empty DataFrame so the rest of the pipeline still works.

-pipeline/interview_job/ops/get_unprocessed_buses
Compares the incoming bus list with the ones already in the existing results file and returns only the new ones.

-pipeline/interview_job/ops/combine_results
Merges the old results and the newly processed data into one DataFrame, which then gets written back out as the updated CSV.

-pipeline/interview_job/ops/raw_buses_to_run.py
Updated to use new_raw_buses.csv as instructed, which contains one new bus (15a).

-pipeline/interview_job/ops/get_mw_available_for_each_bus_very_slow.py
Added 15a to the dummy return data to avoid a KeyError during processing.

-Simplified file I/O
I dropped the use of Dagster's IOManager for now—it added complexity without real benefits for this use case. Instead, each op reads/writes directly to results.csv.

Final Result:
The pipeline now only processes buses it hasn't seen before and merges them with what's already been run. It still produces a single clean CSV in the pipeline/output folder.







