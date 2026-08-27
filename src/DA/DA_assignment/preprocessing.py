import pandas as pd

def read_data_file(file_path: str) -> pd.DataFrame | None:
    """
    Read a CSV file and return it as a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame | None: The loaded DataFrame if successful,
        otherwise None.
    """
    try:
        return pd.read_csv(file_path)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' was not found.")
        return None

    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None

    except pd.errors.ParserError:
        print("Error: The file could not be read as a CSV file.")
        return None

    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return None


def drop_cols(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """
    Remove specified columns from a DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        cols (list[str]): A list of column names to remove.

    Returns:
        pd.DataFrame: A DataFrame with the specified columns removed.
    """
    return df.drop(columns=cols)


def check_data_type(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a data-quality report for the DataFrame.

    The report includes the data type and number of unique values
    for each column.

    Args:
        df (pd.DataFrame): The DataFrame to inspect.

    Returns:
        pd.DataFrame: A transposed DataFrame containing information
        about each column.
    """
    report = pd.DataFrame(
        {
            "Data Type": df.dtypes,
            "Unique Values": df.nunique()
        }
    )

    return report.T