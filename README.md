# Painel de Análise - Supply Chain

Painel interativo de análise de dados de uma cadeia de suprimentos, desenvolvido como projeto de portfólio com **Streamlit + Plotly**.

## Tecnologias
- Python
- Pandas
- Plotly
- Streamlit

## Dataset
[Supply Chain Analysis - Kaggle](https://www.kaggle.com/datasets/harshsingh2209/supply-chain-analysis)

O projeto usa o arquivo `data/supply_chain_data.csv` com dados de produtos, estoque, frete e inspeções de qualidade.

## Análises
- Receita total por tipo de produto
- Estoque médio por categoria
- Taxa de defeitos por produto
- Custo médio de frete por transportadora
- Distribuição dos resultados de inspeção

## Como rodar

```bash
# Clonar o repositório
git clone https://github.com/ermklvr/projeto-1
cd projeto-1

# Criar e ativar o ambiente virtual
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar dashboard
streamlit run app.py
```

Depois disso, o dashboard abre no navegador com filtros na barra lateral e gráficos interativos.
