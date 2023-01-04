import pandas as pd

df = pd.read_csv('data/year=2020/month=03/day=01/top.csv', index_col=0, parse_dates=[1])
