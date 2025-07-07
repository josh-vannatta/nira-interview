import pandas as pd
from dagster import op, Out, In

@op(
    ins={
        "raw_buses": In(pd.DataFrame),
        "existing_results": In(pd.DataFrame),
    },
    out=Out(
        metadata={"key": "unprocessed_buses"},
    )
)
def get_unprocessed_buses(raw_buses, existing_results):
    if existing_results.empty:
        return raw_buses

    unprocessed_buses = raw_buses[
        ~raw_buses["bus_number"].isin(existing_results["bus_number"])
    ]
    return unprocessed_buses
