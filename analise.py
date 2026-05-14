import pandas as pd
import matplotlib.pyplot as plt 
import plotly.express as px

#1. Carregar os dados   
df = pd.read_csv('data\supply_chain_data.csv')

#2. O que eu tenho  
print(df.shape) #quantidade de linhas e colunas
print(df.dtypes) #tipos de coluna
print(df.head(10))       # primeiras 10 linhas
print(df.isnull().sum()) # valores faltando
print(df.shape)
print(df.columns.tolist())
print(df.head(2))