# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')
df.households[df['population'] == df['population'].min()].agg(['max'])

