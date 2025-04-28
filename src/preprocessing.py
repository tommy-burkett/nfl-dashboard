# Imports
import pandas as pd
import numpy as np
import os


def clean_data(filepath: str, 
               year: int, 
               side: str
              ) -> pd.DataFrame:
    
    """
        Clean the data from the given filepath.

        Args:
            filepath (str): The path to the data file.
            year (int): The year of the data.
            side (str): The side of the data ('left' or 'right').
        Returns:
            pd.DataFrame: The cleaned NFL data for dashboard.
    """

    # Read in csv, skip the section header row
    df = pd.read_csv(filepath, skiprows=1)

    # Drop rows with team names that are league totals
    removed_rows = ['Avg Team', 'League Total', 'Avg Tm/G']
    df = df[~df['Tm'].isin(removed_rows)]

    # List of all columns before renaming 
    df_columns = ['Tm', 'G', 'PF', 'Yds', 'Ply', 'Y/P', 
                  'TO', 'FL', '1stD', 'Cmp', 'Att', 'Yds.1', 
                  'TD', 'Int', 'NY/A', '1stD.1', 'Att.1', 
                  'Yds.2', 'TD.1', 'Y/A', '1stD.2', 'Pen', 
                  'Yds.3', '1stPy', 'Sc%', 'TO%', 'EXP'
                  ]
    
    # List of sections
    df_sections = ['Tot Yds & TO', 'Passing', 'Rushing', 'Penalties']
    
    # Create a dictionary to rename the columns based on sections
    rename_columns_dict = {
        # General stats
        'Tm': 'Team',
        'G': 'Games Played',
        'PF': 'Points For',
        'PA': 'Points Allowed',
        'Yds': 'Total Yards',
        '1stD': '1st Downs',
        'Sc%': 'Scoring Percentage',
        'TO%': 'Turnover Percentage',
        'EXP': 'Expected Points',

        # Total Yards & Turnovers
        'Ply': 'Total Plays',
        'Y/P': 'Yards Per Play',
        'TO': 'Total Turnovers',
        'FL': 'Total Fumbles Lost',

        # Passing
        'Cmp': 'Completions',
        'Att': 'Passing Attempts',
        'Yds.1': 'Passing Yards',
        'TD': 'Passing Touchdowns',
        'Int': 'Interceptions',
        'NY/A': 'Net Yards Per Pass Attempt',
        '1stD.1': '1st Downs Passing',

        # Rushing
        'Att.1': 'Rushing Attempts',
        'Yds.2': 'Rushing Yards',
        'TD.1': 'Rushing Touchdowns',
        'Y/A': 'Rushing Yards Per Attempt',
        '1stD.2': '1st Downs Rushing',

        # Penalties
        'Pen': "Penalties",
        "Yds.3": "Penalty Yards",
        "1stPy": "1st Downs by Penalty"
    }

    # Add to dataframe
    df.rename(columns=rename_columns_dict, inplace=True)

    # Add the year and side columns
    df['Year'] = year
    df['Side'] = side
    
    return df

def combine_dataframes(data_dir: str, output_path: str) -> None:
    
    """
        Combine all of the dataframes in the directory into one dataframe and save it to a CSV file.

        Args:
            directory (str): The path to the directory containing the NFL data files.
            output_path (str): The path to save the combined CSV file.
        Returns:
            None
    """

    # List of all dataframes in the data directory
    all_dfs = []

    # Loop through the files in the data directory
    for filename in os.listdir(data_dir):
        # Check if the file is a CSV file
        if filename.endswith(".csv"):
            # Grab the year and side from the filename and clean the data
            try:
                year = int(filename.split("_")[0])
                side = filename.split("_")[1].split(".")[0]
                filepath = os.path.join(data_dir, filename)
                df = clean_data(filepath, year, side)
                all_dfs.append(df)
            # If the file is not valid, print an error message
            except Exception as e:
                print(f"Cannot clean {filename} due to error: {e}")

    # Combine all dataframes into one dataframe and save it as a CSV file
    if all_dfs:
        combined_df = pd.concat(all_dfs, ignore_index=True)
        combined_df.to_csv(output_path, index=False)
        print(f"Combined NFL Data CSV saved to: {output_path}")
    # If no valid CSV files were found, print a message
    else:
        print("No valid CSV files found.")

# Main
if __name__ == "__main__":
    combine_dataframes('data', 'data/2020-2024_combined_nfl_data.csv')