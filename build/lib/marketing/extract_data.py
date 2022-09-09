"""Data loader are extract methods that read data from different sources and return a pandas dataframe. Its a part of ETL and a basic in Data Engenier tasks """
import pandas as pd

def read_local(path):
    """Reads a local csv file and returns a pandas dataframe"""
    df = pd.read_csv(path)
    return df

def query_postgres(query):
    """Queries a postgres database and returns a pandas dataframe"""
    df = pd.read_sql(query, con=engine)
    return df

def read_gcp_storage(gs_path):
    """reads a gcp storage file and returns a pandas dataframe"""
    df = pd.read_csv(gs_path)
    return df

def query_two_dbs():
    query1 = "SELECT * FROM table1"
    query2 = "SELECT * FROM table2"
    df1 = query_postgres(query1)
    df2 = query_postgres(query2)
    return df1, df2