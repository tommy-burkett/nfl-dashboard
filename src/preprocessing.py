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

    return df

