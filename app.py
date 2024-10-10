import streamlit as st
import pandas as pd
import duckdb


st.title ("Mon premier APP")

st.write("SQL repetition practice")

option = st.selectbox(
    "what would you like to review?",
    ("Joins","GroupBy","Windows functions"),
    index=None,
    placeholder = "select a theme"
)

st.write("You selected",option)

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

#tab1 = st.tabs(["text"])

#with tab1:
sql_query = st.text_area(label="entrez votre input")
result= duckdb.query(sql_query).df()
query = st.write(f"vous avez rentrez la requête suivante {sql_query}")
st.dataframe(result)



