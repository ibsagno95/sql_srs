
#pylint:disable=missing-module-docstring

import io

import duckdb
import pandas as pd
import streamlit as st

con = duckdb.connect(database="data/sql_exercises.duckdb",read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "what would you like to review?",
        ("cross_joins", "GroupBy", "Windows functions"),
        index=None,
        placeholder="select a theme",
    )

    st.write("You selected", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}' ").df()
    st.write(exercise)

st.title("Mon premier APP")


st.header("Entrez votre code")

query = st.text_area(label="entrez votre input", key="user_input")



