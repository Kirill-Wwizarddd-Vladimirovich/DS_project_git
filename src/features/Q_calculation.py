from .features_arc import time_features, energy_features
import pandas as pd

def energy_calculation(dataframe: pd.DataFrame) -> pd.Series:
    """Read all csvs and collect them to list for futher merging

    Args:
        time_features (str): start and finish time of heating procedure
        energy_features (str): active and reactive capacity
        
    Returns:
        pd.Series: new calculated feature - expended energy on each stage
    """
    dataframe[time_features] = dataframe[time_features].astype('datetime64[ns]')
    new_feat = (((dataframe[time_features[1]] - dataframe[time_features[0]]).apply(lambda x: x.seconds)) *
                             (((dataframe[energy_features[1]] ** 2) + (dataframe[energy_features[1]] ** 2)) ** (1/2)))

    return new_feat