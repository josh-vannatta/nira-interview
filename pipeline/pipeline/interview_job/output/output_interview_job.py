from dagster import op

@op
def output_interview_job(context, df_with_all_columns):
    output_file_path = "pipeline/pipeline/interview_job/output/results.csv"
    df_with_all_columns.to_csv(
        output_file_path, index=False, line_terminator="\n", encoding="utf-8"
    )
