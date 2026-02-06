import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Attribution Dashboard", layout="wide")
st.title("Atribución Multicanal")

FILES = {
    "Last Click": "outputs/contrib_last_click.csv",
    "Markov (Removal)": "outputs/contrib_markov_removal.csv",
    "Shapley": "outputs/contrib_shapley.csv",
}

model = st.selectbox("Modelo de atribución", list(FILES.keys()))
df = pd.read_csv(FILES[model])

st.subheader("Ranking de contribución")
fig = px.bar(
    df.sort_values("contribution", ascending=False),
    x="channel",
    y="contribution",
    text="contribution"
)
fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("Simulación de presupuesto")

sim = pd.read_csv("outputs/simulaciones.csv")
scenario = st.selectbox("Escenario", sorted(sim["scenario"].unique()))
sim_s = sim[sim["scenario"] == scenario]

fig2 = px.bar(
    sim_s,
    x="channel",
    y="budget",
    color="scenario"
)
st.plotly_chart(fig2, use_container_width=True)
