from .features_arc import time_features, energy_features
import pandas as pd

def energy_calculation(dataframe: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Read all csvs and collect them to list for futher merging

    Args:
        time_features (str): start and finish time of heating procedure
        energy_features (str): active and reactive capacity
        
    Returns:
        dataframe: dataframe with new calculated feature - expended energy on each stage
    """
    dataframe[time_features] = dataframe[time_features].astype('datetime64[ns]')
    dataframe[column_name] = (((dataframe[time_features[1]] - dataframe[time_features[0]]).apply(lambda x: x.seconds)) *
                             (((dataframe[energy_features[1]] ** 2) + (dataframe[energy_features[1]] ** 2)) ** (1/2)))

    return dataframe