from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Painel Supply Chain",
    page_icon="📦",
    layout="wide",
)


@st.cache_data
def load_data() -> pd.DataFrame:
    base_dir = Path(__file__).resolve().parent
    default_path = base_dir / "data" / "supply_chain_data.csv"

    if default_path.exists():
        return pd.read_csv(default_path)

    csv_files = sorted((base_dir / "data").glob("*.csv"))
    if csv_files:
        return pd.read_csv(csv_files[0])

    raise FileNotFoundError(
        "Arquivo de dados não encontrado em data/supply_chain_data.csv. "
        "Adicione o CSV na pasta data."
    )


def aggregate_data(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    return {
        "receita": df.groupby("Product type", as_index=False)["Revenue generated"].sum(),
        "estoque": df.groupby("Product type", as_index=False)["Stock levels"].mean(),
        "defeitos": df.groupby("Product type", as_index=False)["Defect rates"].mean(),
        "frete": df.groupby("Shipping carriers", as_index=False)["Shipping costs"].mean(),
        "inspecoes": (
            df["Inspection results"]
            .value_counts(dropna=False)
            .rename_axis("Resultado")
            .reset_index(name="Quantidade")
        ),
    }


def main() -> None:
    st.title("📦 Painel de Análise - Supply Chain")
    st.caption("Dashboard interativo com métricas de receita, estoque, defeitos, frete e inspeções.")

    try:
        df = load_data()
    except FileNotFoundError as exc:
        st.error(str(exc))
        st.stop()

    product_options = sorted(df["Product type"].dropna().unique().tolist())
    carrier_options = sorted(df["Shipping carriers"].dropna().unique().tolist())

    st.sidebar.header("Filtros")
    selected_products = st.sidebar.multiselect(
        "Tipo de produto",
        options=product_options,
        default=product_options,
    )
    selected_carriers = st.sidebar.multiselect(
        "Transportadora",
        options=carrier_options,
        default=carrier_options,
    )

    filtered_df = df[
        df["Product type"].isin(selected_products)
        & df["Shipping carriers"].isin(selected_carriers)
    ]

    if filtered_df.empty:
        st.warning("Nenhum dado encontrado com os filtros selecionados.")
        st.stop()

    col1, col2, col3 = st.columns(3)
    col1.metric("Receita total", f"${filtered_df['Revenue generated'].sum():,.2f}")
    col2.metric("Estoque médio", f"{filtered_df['Stock levels'].mean():.1f}")
    col3.metric("Defeitos médios", f"{filtered_df['Defect rates'].mean():.2f}%")

    data = aggregate_data(filtered_df)
    template = "plotly_white"

    fig_receita = px.bar(
        data["receita"],
        x="Product type",
        y="Revenue generated",
        title="Receita por tipo de produto",
        color="Product type",
        template=template,
    )

    fig_estoque = px.bar(
        data["estoque"],
        x="Product type",
        y="Stock levels",
        title="Estoque médio por tipo de produto",
        color="Product type",
        template=template,
    )

    fig_defeitos = px.bar(
        data["defeitos"],
        x="Product type",
        y="Defect rates",
        title="Taxa média de defeitos por tipo de produto",
        color="Product type",
        template=template,
    )

    fig_frete = px.bar(
        data["frete"],
        x="Shipping carriers",
        y="Shipping costs",
        title="Custo médio de frete por transportadora",
        color="Shipping carriers",
        template=template,
    )

    fig_inspecoes = px.pie(
        data["inspecoes"],
        names="Resultado",
        values="Quantidade",
        title="Distribuição dos resultados de inspeção",
        hole=0.35,
        template=template,
    )

    row1_col1, row1_col2 = st.columns(2)
    row1_col1.plotly_chart(fig_receita, use_container_width=True)
    row1_col2.plotly_chart(fig_estoque, use_container_width=True)

    row2_col1, row2_col2 = st.columns(2)
    row2_col1.plotly_chart(fig_defeitos, use_container_width=True)
    row2_col2.plotly_chart(fig_frete, use_container_width=True)

    st.plotly_chart(fig_inspecoes, use_container_width=True)


if __name__ == "__main__":
    main()
