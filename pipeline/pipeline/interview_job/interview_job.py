from dagster import job

from pipeline.interview_job.ops.add_gw_available_column import add_gw_available_column
from pipeline.interview_job.ops.get_mw_available_for_each_bus_very_slow import (
    get_mw_available_for_each_bus_very_slow,
)
from pipeline.interview_job.ops.raw_buses_to_run import raw_buses_to_run
from pipeline.interview_job.output.output_interview_job import output_interview_job
from pipeline.interview_job.ops.get_existing_results import get_existing_results
from pipeline.interview_job.ops.get_unprocessed_buses import get_unprocessed_buses
from pipeline.interview_job.ops.combine_results import combine_results


@job
def interview_job():
    """
    A job to run the interview pipeline.
    """
    raw_buses = raw_buses_to_run()
    existing_results = get_existing_results(raw_buses)
    unprocessed_buses = get_unprocessed_buses(raw_buses, existing_results)
    new_results = get_mw_available_for_each_bus_very_slow(unprocessed_buses)
    combined_results = combine_results(new_results, existing_results)
    gw_available = add_gw_available_column(combined_results)
    output_interview_job(gw_available)
