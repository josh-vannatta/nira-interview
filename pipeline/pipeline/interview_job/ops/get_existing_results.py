import os
import pandas as pd
from dagster import op, Out, In

@op(
    ins={'start': In(None)},
    out=Out(
        metadata={"key": "existing_results"},
    )
)
def get_existing_results(start):
    """
    An op to load the results from the previous run from a fixed file path.
    """
    output_file = "pipeline/pipeline/interview_job/output/results.csv"
    if not os.path.exists(output_file):
        return pd.DataFrame(columns=['bus_number', 'mw_available'])
    
    return pd.read_csv(output_file)
