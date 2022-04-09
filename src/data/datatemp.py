import pandas as pd

def dfpreptemp(dataframe_temp: pd.DataFrame, dataframe_arc: pd.DataFrame,ft_list: list, new_feat: list) -> pd.DataFrame:
    """Create 2 new features 'Init temp' and 'Final temp' for each sample, drop samples with lack of temperature data 
       'Final temp' - target feature
       Merge temperature data to major dataframe with samples
    Args:
        dataframe (pd.DataFrame): initial dataframe
        ft_list (list): dataframe columns
        new_feat (list): new columns

        
    Returns:
        Dataframe: resulting dataframe 
    """
    temp_start = dataframe_temp.sort_values(by= ft_list[1], ascending=True).drop_duplicates(subset=ft_list[0])[ft_list[0::2]]
    temp_end = dataframe_temp.sort_values(by= ft_list[1], ascending=False).drop_duplicates(subset=ft_list[0])[ft_list[0::2]]
    temp = temp_start.merge(temp_end, on=['key'])
    temp.columns = new_feat
    df_final = dataframe_arc.merge(temp, on=new_feat[0]).dropna()

    return df_final