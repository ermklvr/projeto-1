# Painel de Análise - Supply Chain

Painel interativo de análise de dados de uma cadeia de suprimentos, desenvolvido como primeiro projeto de portfólio.

## Tecnologias
- Python
- Pandas
- Plotly

## Dataset
[Supply Chain Analysis - Kaggle](https://www.kaggle.com/datasets/harshsingh2209/supply-chain-analysis)

100 registros com informações de produtos, estoque, frete, fornecedores e inspeções de qualidade.

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

# Criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Executar
python analise.py
```

O painel abre automaticamente no navegador.
