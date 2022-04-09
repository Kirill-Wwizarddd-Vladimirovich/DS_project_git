import pandas as pd
from matplotlib import pyplot as plt

def boxplotss(df, dfcolumns, dirname):
    for col in dfcolumns:
        plt.figure(figsize=(18,18))
        boxplot_C  = plt.boxplot(df[col].values)
        outliers = list(boxplot_C["fliers"][0].get_data()[1])
        plt.ylabel('Количество ' +  str(col))
        plt.title(f"Выбросов в значении {col} всего {len(outliers)}")
        plt.savefig(f"{dirname}/{col}.png")
        plt.show() 
        