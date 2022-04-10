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

model_params = {
    'parameters_RFR' : {'max_depth' : list(range(2, 10, 2)),
                    'n_estimators': list(range(50, 200, 50)),
                    'criterion' : ['mae'],
                    },
                    
    'parameters_LGB' : {
        'learning_rate': [0.01, 0.03, 0.05],
        'n_estimators': [50, 100],
    },

    'parameters_CTB' : {'learning_rate': list(np.arange(0.01, 0.1, 0.01)),
                'depth': [4, 6, 8]
                    }
}

rfr = RandomForestRegressor(random_state=12345)
lgbm = lgb.LGBMRegressor(random_state = 12345)
ctb = CatBoostRegressor(random_state = 12345, 
                         iterations = 1000, 
                         loss_function = 'MAE')
model_list = [rfr, lgbm
            ,ctb]

models_dict = dict(zip(model_params.keys(), model_list))

