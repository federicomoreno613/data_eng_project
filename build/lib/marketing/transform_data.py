import pandas as pd

def normalize_datetime_column(df, column):
    """Takes a dataframe and a column name and returns a dataframe with a normalized datetime column"""
    df[column] = pd.to_datetime(df[column])
    df["year_month"] = df[column].dt.strftime("%Y-%m")
    return df

def normalize_column_names(df):
    """Takes a dataframe and returns a dataframe with normalized column names"""
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df

def save_transformed_data(df, path):
    """Takes a dataframe and a path and saves the dataframe as a csv file"""
    df.to_csv(path, index=False)