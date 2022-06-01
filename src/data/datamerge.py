import pandas as pd
from .datalist import csvlist
from functools import reduce

def readcsvs(datalist: list) -> list:
    """Read all csvs and collect them to list for futher merging

    Args:
        datalist (list): list with all pathes to csvs for importing
        
    Returns:
        list: resulting list
    """
    filelist = [pd.read_csv(file) for file in datalist]
    #for file in datalist:
    #    data = pd.read_csv(file)
    #    filelist.append(data)
    return filelist


def mergecsvs(dataframe: pd.DataFrame, csv_list: list) -> pd.DataFrame:
    """Create Dataframe, that contains all csvs for futher preprocessing

    Args:
        csvlist (list): list with all imported csvs

        
    Returns:
        Dataframe: resulting dataframe 
    """
    csv_list.append(dataframe)
    final_df = reduce(lambda left,right: pd.merge(left,right,on=['key'],
                                            how='left'), csv_list)
    return final_df

#Была ошибка с появлением новой строки - сделал заплатку в виде .reset_index(drop=False).drop([0])
def dfprep(dataframe: pd.DataFrame, argtosum: str) -> pd.DataFrame:
    """Summerizes all 'Energy' for each 'key'. Drops all columns except 'Key' and 'Energy' for futher merging

    Args:
        dataframe (pd.DataFrame): dataframe with calculated feature 'Energy'
        argtosum (str): feature over which summerizing is performed

        
    Returns:
        Dataframe: resulting dataframe 
    """
    df_new = dataframe.drop(columns=dataframe.columns[2:5], axis = 1).groupby([argtosum]).sum().reset_index(drop=False)
    
    return df_new
# В рамках каждого скрипта нужно ли по-новой называть переменные - df_new и final_df

#!!!
# Мне кажется, что при возвращении датафрейма я что-то делаю не так - при переприсваивании датафрейма возвращает не исходный отредактированный, а новый, который хранится в памяти, но пока не записан в переменную
#!!!
#Выглядит как полное гавно. Находил функцию для поиска именно русских слов в списке. Но как их перевести на английский не придумал
def dfprepar(dataframe: pd.DataFrame, feat_list: str) -> pd.DataFrame:
    """Rename russian columns and fills all Nans by '0'

    Args:
        dataframe (pd.DataFrame): dataframe merged with other dataframes
        featrename (str): feature to rename

        
    Returns:
        Dataframe: resulting dataframe 
    """
    dataframe.fillna(0, inplace = True)
    df_f = dataframe.rename(columns={feat_list: 'Gas'}) # не сработало dataframe = dataframe
    return df_f


def missing(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Return dataframe, that displays all missing values

    Args:
        dataframe (pd.DataFrame): final dataframe
        
    Returns:
        Dataframe: resulting dataframe 
    """

    report = dataframe.isna().sum().to_frame()
    report = report.rename(columns = {0: 'missing_values'})
    report['% of total'] = (report['missing_values'] *100 / dataframe.shape[0]).round(2)
    print(report.sort_values(by = 'missing_values', ascending = False))
    return report