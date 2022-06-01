from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def tts_func(dataframe: pd.DataFrame) -> pd.DataFrame:
    target = dataframe['Final Temp']
    features = dataframe.drop(['key', 'Final Temp'], axis=1)
    features_train, features_test, target_train, target_test = train_test_split(
        features, target, test_size=0.25, random_state=12345)

    return features_train, features_test, target_train, target_test