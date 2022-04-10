from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV
import lightgbm as lgb
import seaborn as sns
from sklearn.neural_network import MLPRegressor
import numpy as np
import copy
import pandas as pd

from .parameters import *


def model_learning(dataframe: pd.DataFrame, target_ft: str) -> pd.DataFrame:
    """Function that learn models
    Args:
        dataframe (pd.DataFrame): final dataframe
        target_f (str): target feature


    Returns:
        dataframe with model name and its 'mae' results
    """
    target = dataframe[target_ft]
    features = dataframe.drop(target_ft, axis=1)
    features_train, features_test, target_train, target_test = train_test_split(
    features, target, test_size=0.25, random_state=12345)
    results = []
    for model in model_list:
        model.fit(features_train, target_train)
        model_prediction = model.predict(features_test)
        model_mae = mean_absolute_error(target_test, model_prediction)
        results.append(model_mae)
    model_df = pd.DataFrame({'Model': [type(model).__name__ for model in model_list], 'Mae_results': results}) 
    return model_df



def gridsearch_model(dataframe: pd.DataFrame, target_ft: str) -> pd.DataFrame:
    """Function where model's optimal hyperparameters are found with GridSearch

    Args:
        dataframe (pd.DataFrame): final dataframe
        target_f (str): target feature

    Returns:
         dataframe with model name and its 'mae' results after gridsearch procedure
    """
    target = dataframe[target_ft]
    features = dataframe.drop(target_ft, axis=1)
    features_train, features_test, target_train, target_test = train_test_split(
    features, target, test_size=0.25, random_state=12345)
    results = []
    best_params = []
    for model_name, model in models_dict.items():
        gs = GridSearchCV(
            model,
            model_params[model_name],
            cv=5,
            scoring=(
                "neg_mean_absolute_error",
            ),
            refit="neg_mean_absolute_error"
        )

        gs.fit(features_train, target_train)
        regressor = gs.best_estimator_
        regressor.fit(features_train, target_train)
        preds = regressor.predict(features_test)
        model_mae = mean_absolute_error(target_test, preds)
        results.append(model_mae)
        best_params.append(gs.best_params_)
        model_df = pd.DataFrame({
                                'Model': [type(model).__name__ for model in model_list], 
                                #'Best parameters' : best_params, 
                                'Mae_results': results
                                }) 


    return model_df