import pandas as pd
from dagster import op, Out, In

@op(
    ins={
        "new_results": In(pd.DataFrame),
        "existing_results": In(pd.DataFrame),
    },
    out=Out(
        metadata={"key": "combined_results"},
    )
)
def combine_results(new_results, existing_results):
    """
    An op to merge the old and new results.
    """
    if existing_results.empty:
        return new_results

    return pd.concat([existing_results, new_results])
