import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

#Carregar os dados   
df = pd.read_csv('data\supply_chain_data.csv')

# --- 1. receita por tipo de produto ---
receita = df.groupby('Product type') ['Revenue generated'].sum().reset_index()

# --- 2. estoque medio por tipo de produto ---
estoque = df.groupby('Product type') ['Stock levels'].mean().reset_index()

# --- 3. taxa de defeitos por tipo de produto ---
defeitos = df.groupby('Product type') ['Defect rates'].mean().reset_index()

# --- 4. custo medio de frete por transportadora
frete = df.groupby('Shipping carriers')['Shipping costs'].mean().reset_index()

# --- 5. distribuição de inspeções ---
inspecoes = df['Inspection results'].value_counts().reset_index()
inspecoes.columns = ['Resultado', 'Quantidade']

#graficos

fig = make_subplots(
    rows=3,cols=2,
    specs=[
        [{"type": "xy"}, {"type": "xy"}],
        [{"type": "xy"}, {"type": "xy"}],
        [{"type": "domain"}, {"type": "xy"}]
    ],
    subplot_titles=(
        'Receita por Produto',
        'Estoque Médio por Produto',
        'Taxa de Defeitos por Produto',
        'Custo Médio de Frete por Transportadora',
        'Resultados de Inspeção',
    )
    )

fig.add_trace(go.Bar(x=receita['Product type'], y=receita['Revenue generated'], name='Receita'), row=1,col=1)
fig.add_trace(go.Bar(x=estoque['Product type'], y=estoque['Stock levels'], name='Estoque'), row=1,col=2)
fig.add_trace(go.Bar(x=defeitos['Product type'], y=defeitos['Defect rates'], name='Defeitos'), row=2,col=1)
fig.add_trace(go.Bar(x=frete['Shipping carriers'], y=frete['Shipping costs'], name='Frete'), row=2,col=2)
fig.add_trace(go.Pie(labels=inspecoes['Resultado'], values=inspecoes['Quantidade'], name='Inspeções'), row=3, col=1)

fig.update_layout(height=900, title_text='Painel de Análise - Supply Chain', showlegend=False)
pio.renderers.default='browser'
fig.show()