import pandas as pd
import bigquery as bq


def insert_into_bigquery(df, table_name):
    """Takes a dataframe and a table name and inserts the dataframe into a bigquery table"""
    df.to_gbq(table_name, project_id="data-eng-project", if_exists="append", token=".gcp/token.json")
    return None