# pylint:disable=missing-module-docstring

import io
import duckdb
import pandas as pd
import streamlit as st
import plotly.express as px

with st.sidebar:
    option = st.selectbox(
        "what would you like to review?",
        ("Joins", "GroupBy", "Windows functions"),
        index=None,
        placeholder="select a theme",
    )

    st.write("You selected", option)

st.title("Mon premier APP")

CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_price
cookie,2.5
choco,2.5
muffin,3
"""
food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_DF = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution_df = duckdb.sql(ANSWER_DF).df()
st.header("Entrez votre code")

query = st.text_area(label="entrez votre input", key="user_input")

if query:  # Affichage conditionnelle
    result = duckdb.sql(query).df()
    st.dataframe(result)

    if len(solution_df.columns) != len(result.columns):
        st.write("Il manque des colonnes")

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Il manque des colonnes")

    n_difference = abs(solution_df.shape[0] - result.shape[0])

    if n_difference != 0:
        st.write(f"Il y'a {n_difference} lignes de difference entre les solution")


tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    st.write("table:beverages")
    st.dataframe(beverages)
    st.write("tables: food_items")
    st.dataframe(food_items)
    st.write("expected table:")
    st.dataframe(solution_df)

with tab2:
    st.write(ANSWER_DF)

fig = px.scatter(solution_df, x="price", y="food_price")

st.plotly_chart(fig)
