import pandas as pd

def convert_csv_to_parquet(csv_filepath, parquet_filepath):
    """
    Converts a CSV file to Parquet format

    Args:
        csv_filepath (str): The path to the input CSV file
        parquet_filepath (str): The path to save the output Parquet file
    """
    try:
        df = pd.read_csv(csv_filepath)
        df.to_parquet(parquet_filepath)
        print(f"Successfully converted '{csv_filepath}' to '{parquet_filepath}'")
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_filepath}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    csv_file = "motion_instructions.csv"
    parquet_file = "motion_instructions.parquet"
    convert_csv_to_parquet(csv_file, parquet_file)