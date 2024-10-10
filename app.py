import pandas as pd
import streamlit as st
import duckdb
from pygments.lexer import default

st.title ("Mon premier APP")

st.write("Hello world")
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

#tab1 = st.tabs(["text"])

#with tab1:
sql_query = st.text_area(label="entrez votre input")
result= duckdb.query(sql_query).df()
query = st.write(f"vous avez rentrez la requête suivante {sql_query}")
st.dataframe(result)



